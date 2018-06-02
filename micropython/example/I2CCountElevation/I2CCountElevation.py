#通过I2C连接bmp388和esp32
#download bmp388.py and downloadAndRun this demo

import bmp388
from machine import Pin,I2C
import time

#create I2C object
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)

#create I2C通信的bmp388 object
bmp388 = bmp388.DFRobot_BMP388_I2C(i2c)

#read pressure and count elevation
while 1:
  pressure = bmp388.readPressure();
  elevation = 44330 * (1.0 - pow(pressure / 101325, 0.1903))
  print("elevation : %s" %elevation)
  time.sleep(0.5)
