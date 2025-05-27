from machine import Pin, SoftI2C
from time import sleep
from d1motor import Motor

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)

motor = Motor(0, i2c)

motor.speed(100)
                                        
sleep(5)

motor.speed(0)

sleep(2)
