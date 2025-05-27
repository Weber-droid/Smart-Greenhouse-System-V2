from machine import Pin, PWM


led_pwm = PWM(Pin(22), freq=1000, duty=1023)


while True:
    pass  
