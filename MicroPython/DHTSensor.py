from machine import Pin
import dht

class DHTSensor:
    def __init__(self, pin_number):
        self.sensor = dht.DHT22(Pin(pin_number))
    
    def read_values(self, on_error=None):
        try:
            self.sensor.measure()
            return (self.sensor.temperature(), self.sensor.humidity())
        except OSError as e:
            print(f"Error reading DHT sensor: {e}. Fallback to embedded sensor.")
            if on_error:
                return on_error()
            return (None, None)
