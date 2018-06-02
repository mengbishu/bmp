# BMP388 Library for Arduino/ESP32/RaspberrayPi
This is a Library for BMP388, the function is to read temperature and pressure.
Put the SVG here
## Table of Contents

* [Summary](#summary)
* [Use](#use)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)


<snippet>
<content>

## Summary
* BMP388 can read temperature and pressure.
* 这个库支持SPI与I2C通信
* The sensor is more accurate than its predecessors, covering a wide measurement range from 300 hPa to 1250 hPa.
* This new barometric pressure sensor exhibits an attractive price-performance ratio coupled with low power consumption.

## Methods

### Arduino
```C++

#include <DFRobot_BMP388.h>
/*
 * @brief bmp388的i2c的构造函数
 */
DFRobot_BMP388();

/*
 * @brief bmp388的spi的构造函数
 *
 * @param cs spi的片选引脚
 */
DFRobot_BMP388(int cs);

/*
 * @brief Initialize bmp388, check for chip id, reset the sensor, read the calibration data and config sensor
 *
 * @return 0 if success
 */
int8_t begin();

/*
 * @brief Read temperature
 *
 * @return temperature
 */
uint8_t float readTemperature();

/*
 * @brief Read pressure.
 *
 * @return pressure
 */
float readPressure();
```

### micropython
```python

import bmp388

/*
 * @brief BMP388的i2c的构造函数
 *
 * @param i2c I2C object.
 */
DFRobot_BMP388_I2C(i2c)

/*
 * @brief BMP388的spi的构造函数
 *
 * @param spi SPI object.
 *        cs  SPI的片选引脚
 */
DFRobot_BMP388_SPI(spi,cs)

/*
 * @brief Read temperature
 *
 * @return temperature
 */
readTemperature()

/*
 * @brief Read pressure.
 *
 * @return pressure
 */
readPressure()

```
### Raspberry Pi
```python

import bmp388

/*
 * @brief BMP388的i2c的构造函数
 */
DFRobot_BMP388_I2C()

/*
 * @brief BMP388的spi的构造函数
 *
 * @param cs SPI的片选引脚
 */
DFRobot_BMP388_SPI(cs)

/*
 * @brief Read temperature
 *
 * @return temperature
 */
readTemperature()

/*
 * @brief Read pressure.
 *
 * @return pressure
 */
readPressure()
```


## Compatibility

MCU                | Work Well | Work Wrong | Untested  | Remarks
------------------ | :----------: | :----------: | :---------: | -----
FireBeetle-ESP32 |      √       |             |            | 
RaspberrayPi |      √       |             |            | 只支持python3
Arduino |      √       |             |            | 

## History

- data 2018-6-2
- version V0.1


## Credits

- author [Luyuhao  <yuhao.lu@dfrobot.com>]
