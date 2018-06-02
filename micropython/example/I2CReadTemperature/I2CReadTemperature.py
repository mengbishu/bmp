import bmp388
import time
from machine import Pin,I2C

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
bmp388 = bmp388.DFRobot_BMP388_I2C(i2c)

while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s" %temp)
  time.sleep(0.5)
