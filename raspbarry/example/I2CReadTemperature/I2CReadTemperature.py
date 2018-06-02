import bmp388
import time

bmp388 = bmp388.DFRobot_BMP388_I2C()

while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s" %temp)
  time.sleep(0.5)