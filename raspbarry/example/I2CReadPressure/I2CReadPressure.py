import bmp388
import time

bmp388 = bmp388.DFRobot_BMP388_I2C()

while 1:
  pres = bmp388.readPressure()
  print("Pressure : %s" %pres)
  time.sleep(0.5)