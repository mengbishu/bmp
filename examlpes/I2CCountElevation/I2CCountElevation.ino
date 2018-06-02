 /*!
  * file I2CCountElevation.ino
  * 
  * 将BMP388连接到Arduino的I2C接口上, 下载程序
  * elevation is calculated based on temperature and sea level pressure
  * 这个示例只能计算一个大概的海拔高度
  * 计算公式：
  * P=P0*(1-H/44300)^5.256
  * @n 打开 serial monitor, 查看海拔高度.
  *
  * Copyright   [DFRobot](http://www.dfrobot.com), 2016
  * Copyright   GNU Lesser General Public License
  *
  * version  V0.1
  * date  2018-5-29
  */
#include "DFRobot_BMP388.h"
#include "Wire.h"
#include "math.h"

/*创建一个I2C通信的bmp388对象*/
DFRobot_BMP388 bmp388;

void setup(){
  /*串口初始化*/
  Serial.begin(9600);
  /*bmp388初始化*/
  bmp388.begin();
}

void loop(){
  /*读取大气压,计算海拔*/
  float pressure = bmp388.readPressure();
  float elevation = 44330 * (1.0 - pow(pressure / 101325, 0.1903));
  Serial.print("Elevation : ");
  Serial.println(elevation);
  delay(100);
}

