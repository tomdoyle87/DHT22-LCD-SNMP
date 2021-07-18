## Readme

### Devices
#### DHT22 Probe:
https://www.amazon.co.uk/gp/product/B07FM8BMWD/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1

#### LCD Screen 
https://www.amazon.co.uk/SunFounder-Display-Ardauino-Mega2560-IIC2004/dp/B01GPUMP9C/ref=pd_rhf_ee_s_rp_c_3_2/257-5943342-5061712?pd_rd_w=bWGxe&pf_rd_p=319d03f2-5e2d-4ea1-9213-1d86496172d6&pf_rd_r=9WRVMXDGFWAKG5Q4V4PN&pd_rd_r=ea51c56e-9b1c-41c0-92bd-60cf96e6795e&pd_rd_wg=GQeoQ&pd_rd_i=B01GPUMP9C&psc=1

### Connections
#### DHT22 Probe:
Positive (+) to 3.3v</br>
Out to Gpio pin, (in this case 17)</br>
Negative (-) to Ground</br>

#### LCD Screen
GND to Ground</br>
VCC to 5v</br>
SDA to GPIO2 (SDA)</br>
SCL to GPIO3 (SCL)

### Installation

`sudo apt-get install python3-pip`<br/>
`git clone https://github.com/tomdoyle87/DHT22-LCD-SNMP.git`<br/>
`cd DHT22-LCD-SNMP` 

#### SNMP
`cp {DHT-hum-snmp.py,DHT-temp-snmp.py} ~`<br/>
`touch ~/humid.txt ~/temp.txt`<br/>
`pip3 install adafruit-circuitpython-dht`<br/>
`pip3 install board`<br/>
`sudo cp {humid,temp} /usr/local/bin/`<br/>
`sudo chmod 755 {/usr/local/bin/humid,/usr/local/bin/temp}`

Now add the following to /etc/snmp/snmpd.conf:</br>
`pass .1.3.6.1.2.1.25.1.8.2      /bin/sh         /usr/local/bin/temp`</br>
`pass .1.3.6.1.2.1.25.1.8.1      /bin/sh         /usr/local/bin/humid`

#### LCD Screen
`cp display.py ~`</br>
`sudo apt-get install i2c-tools`</br>
`pip3 install smbus`</br>
`pip3 install vcgencmd`</br>
`pip3 datetime`

#### Systemd-Timers
`sudo cp {get-temp.service,get-temp.timer,lcd-temperature.service,lcd-temperature.timer} /etc/systemd/systemd/system`</br>
`sudo systemctl enable get-temp.timer`</br>
`sudo systemctl start get-temp.timer` </br>
`sudo systemctl enable lcd-temperature.timer`</br>
`sudo systemctl start lcd-temperature.timer`

#### Sources:
http://www.kbza.org/2013/07/04/sensor-de-temperatura-snmp-con-raspberry-y-cacti/</br>
https://howchoo.com/pi/how-to-make-a-raspberry-pi-smart-alarm-clock</br>
https://github.com/fede2cr/raspberry-pi_snmp/tree/master/sensor-DHT</br>
https://osoyoo.com/2016/12/01/use-raspberry-pi-display-temperaturehumidity-to-i2c-lcd-screen/</br>







