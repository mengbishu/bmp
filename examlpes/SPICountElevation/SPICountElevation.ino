 /*!
  * file countElevation.ino
  * 
  * 将BMP388连接到Arduino的SPI接口上, 下载程序
  * elevation is calculated based on temperature and sea level pressure
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

/*创建一个spi接口的bmp388对象,spi的片选引脚为3*/
DFRobot_BMP388 bmp388(3);

void setup(){
  while(!Serial);
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
  //(8.31*(273+t)/0.28)*log(101325/p)
  delay(100);
}


