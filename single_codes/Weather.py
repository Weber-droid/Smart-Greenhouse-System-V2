import dht
import machine
from machine import Pin, SoftI2C,PWM
from d1motor import Motor

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
motor = Motor(0, i2c)

dht11 = dht.DHT11(machine.Pin(22))

def read_dht():
    try:
        dht11.measure()
        temperature = dht11.temperature()
        humidity = dht11.humidity()
        return temperature, humidity
    except Exception as e:
        print("Error reading DHT11 sensor:", e)
        return None, None

while True:
    temp, humi = read_dht()
    if temp is not None and humi is not None:
        print("Temperature:", temp, "°C")
        print("Humidity:", humi, "%")
        if (temp > 35 ):
            motor.speed(100000)
        elif (temp <  30):
            led_pwm = PWM(Pin(5), freq=1000, duty=1023)
        else:
            motor.speed(0)
            led_pwm = PWM(Pin(5), freq=1000, duty=0)
            
    else:
        print("Failed to read from DHT11 sensor!")
