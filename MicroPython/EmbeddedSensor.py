from machine import Pin, ADC

class EmbeddedSensor:
    def __init__(self, pin_number):
        self.sensor = ADC(pin_number)
    
    def read_temperature(self):
        adc_value = self.sensor.read_u16()
        volt = (3.3 / 65535) * adc_value
        temperature = 27 - (volt - 0.706) / 0.001721
        return round(temperature, 1)
