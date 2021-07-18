import adafruit_dht
from board import pin 

# Initial the dht device, with data pin connected to:
dht_device = adafruit_dht.DHT22(17)

temperature = dht_device.temperature
humidity = dht_device.humidity

if humidity is not None and temperature is not None:
    rtemperature = round(temperature)
    stemperature = str(rtemperature)
    f = open("/home/pi/temp.txt", "w")
    f.write(stemperature)
    f.close()
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
