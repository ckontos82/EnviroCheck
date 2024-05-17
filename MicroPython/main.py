from machine import Pin
from DHTSensor import DHTSensor
from EmbeddedSensor import EmbeddedSensor
import time
import network
import json
import urequests
import uasyncio as asyncio

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('OTE46E47E', '\"23DiakosiA11\\PentE6693EjI\\')

led = Pin('LED', Pin.OUT)
dht_sensor = DHTSensor(22)
embedded_sensor = EmbeddedSensor(4)

def blink_led(times, sleep_duration):
    for _ in range(times):
        led.on()
        time.sleep(sleep_duration)
        led.off()
        time.sleep(sleep_duration)

def fallback_to_embedded():
    temperature = embedded_sensor.read_temperature()
    blink_led(3, 0.2)
    time.sleep(0.8)
    return (temperature, None)

async def post_data(url, json_data):
    try:
        led.on()
        response = urequests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
        print(response.text)
        response.close()
        await asyncio.sleep(1)
        led.off()
    except OSError as e:
        print("Endpoint seems down. Cannot POST.")
        blink_led(3, 0.2)  # LED blink to indicate the inability to make post request
        await asyncio.sleep(1)

async def main():
    url = "http://192.168.1.8:5001/api/records"

    while True:
        temperature, humidity = dht_sensor.read_values(on_error=fallback_to_embedded)
        print(f"Temperature: {temperature} °C")

        if humidity is not None:
            print(f"Humidity: {humidity}%")

        record = {
            "Temp": temperature,
            "Humidity": humidity
        }

        json_data = json.dumps(record)

        await post_data(url, json_data)
        await asyncio.sleep(4)

asyncio.run(main())
