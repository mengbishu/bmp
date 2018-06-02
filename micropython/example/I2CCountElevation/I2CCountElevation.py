import bmp388
from machine import Pin,I2C
import time

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
bmp388 = bmp388.DFRobot_BMP388_I2C(i2c)

while 1:
  pressure = bmp388.readPressure();
  elevation = 44330 * (1.0 - pow(pressure / 101325, 0.1903))
  print("elevation : %s" %elevation)
  time.sleep(0.5)
