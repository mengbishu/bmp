import bmp388
import time

cs = 22
bmp388 = bmp388.DFRobot_BMP388_SPI(cs)
while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s" %temp)  
  time.sleep(0.5)