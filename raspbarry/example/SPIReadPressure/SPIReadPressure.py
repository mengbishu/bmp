import bmp388
import time

cs = 22
bmp388 = bmp388.DFRobot_BMP388_SPI(cs)
while 1:
  pres = bmp388.readPressure()
  print("Temperature : %s" %pres)  
  time.sleep(0.5)