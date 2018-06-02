# 通过I2C连接bmp388和esp32
#
# elevation is calculated based on temperature and sea level pressure
# 这个示例只能计算一个大概的海拔高度
# 计算公式：
# P=P0*(1-H/44300)^5.256
#
# warning:
#   this demo 只支持python3
#   run this demo : python3 I2CCountElevation.py
#
# connect:
#   raspberry       bmp388
#   3.3v(1)         VCC
#   GND(6)          GND
#   SCL(5)          SCL
#   SDA(3)          SDA

import bmp388
import time

#create I2C通信的bmp388 object
bmp388 = bmp388.DFRobot_BMP388_I2C()

#read pressure and count elevation
while 1:
  pressure = bmp388.readPressure();
  elevation = round(44330 * (1.0 - pow(pressure / 101325, 0.1903)),2)
  print("elevation : %s" %elevation)
  time.sleep(0.5)
