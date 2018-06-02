# 通过SPI连接bmp388和esp32
#
# elevation is calculated based on temperature and sea level pressure
# 这个示例只能计算一个大概的海拔高度
# 计算公式：
# P=P0*(1-H/44300)^5.256
#
# warning:
#   this demo 只支持python3
#   run this demo : python3 SPICountElevation.py
#
# connect:
#   raspberry       bmp388
#   CS  (15)        CSB
#   3.3v(17)        VCC
#   MOSI(19)        SDI
#   MISO(21)        SDO
#   SCLK(23)        SCK
#   GND (25)        GND

import bmp388
import time

#define chip selection pins
cs = 22

#create SPI通信的bmp388 object
bmp388 = bmp388.DFRobot_BMP388_SPI(cs)

#read pressure and count elevation
while 1:
  pressure = bmp388.readPressure()
  elevation = round(44330 * (1.0 - pow(pressure / 101325, 0.1903)),2)
  print("Elevation : %s" %elevation)  
  time.sleep(0.5)
