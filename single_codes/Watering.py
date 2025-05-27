from machine import Pin, ADC
import time

relay_pin = 26 

relay = Pin(relay_pin, Pin.OUT)


def pump_on():
    relay.on()


def pump_off():
    relay.off()

sensor_pin = 35  
adc = ADC(Pin(sensor_pin))  
adc.width(ADC.WIDTH_12BIT)  
adc.atten(ADC.ATTN_11DB)  

while True:
    sensor_analog = adc.read()  
    moisture = 100 - ((sensor_analog / 4095.0) * 100)  
    print("Moisture =", moisture, "%")  
    time.sleep(1)
    if moisture > 40:
        pump_on()
        time.sleep(5)
    else:
        pump_off()
