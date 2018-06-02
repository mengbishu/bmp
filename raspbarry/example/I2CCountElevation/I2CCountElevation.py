import bmp388
import time

bmp388 = bmp388.DFRobot_BMP388_I2C()

while 1:
  pressure = bmp388.readPressure();
  elevation = round(44330 * (1.0 - pow(pressure / 101325, 0.1903)),2)
  print("elevation : %s" %elevation)
  time.sleep(0.5)
