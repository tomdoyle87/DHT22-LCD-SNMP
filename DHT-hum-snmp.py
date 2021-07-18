import adafruit_dht
from board import pin 

# Initial the dht device, with data pin connected to:
dht_device = adafruit_dht.DHT22(17)

temperature = dht_device.temperature
humidity = dht_device.humidity

if humidity is not None and temperature is not None:
    shumidity = str(humidity)
    f = open("/home/pi/humid.txt", "w")
    f.write(shumidity)
    f.close()

else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
