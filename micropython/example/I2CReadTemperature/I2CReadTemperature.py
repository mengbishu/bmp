#通过I2C连接bmp388和esp32
#download bmp388.py and downloadAndRun this demo

import bmp388
import time
from machine import Pin,I2C

#create I2C object
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

#create I2C通信的bmp388 object
bmp388 = bmp388.DFRobot_BMP388_I2C(i2c)

#read temperature and print it
while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s" %temp)
  time.sleep(0.5)
