from machine import Pin
import time

relay_pin = 26 

relay = Pin(relay_pin, Pin.OUT)


def pump_on():
    relay.on()


def pump_off():
    relay.off()

while True:
    pump_on()  
    time.sleep(5)  
    pump_off()  
    time.sleep(5) 
