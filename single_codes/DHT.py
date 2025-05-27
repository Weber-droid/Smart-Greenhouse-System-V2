import dht
import machine

d = dht.DHT11(machine.Pin(22))



while True:
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")


