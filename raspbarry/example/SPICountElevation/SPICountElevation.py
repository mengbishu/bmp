import bmp388
import time

cs = 22
bmp388 = bmp388.DFRobot_BMP388_SPI(cs)

while 1:
  pressure = bmp388.readPressure()
  elevation = round(44330 * (1.0 - pow(pressure / 101325, 0.1903)),2)
  print("Elevation : %s" %elevation)  
  time.sleep(0.5)
