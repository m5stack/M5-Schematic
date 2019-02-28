# Schematic difference with ESP32CAM and M5Camera

**[中文](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/hardware_diff_with_ESP32CAM_M5Camera_zh_CN.md)**

## The firmware link

- ESP32Cam Firmware: https://github.com/m5stack/m5stack-cam-psram/tree/normal

- M5Camera(A model default) Firmware: https://github.com/m5stack/m5stack-cam-psram/tree/master

- M5CameraX Firmware: https://github.com/m5stack/m5stack-cam-psram/tree/master

- M5CameraF Firmware: https://github.com/m5stack/m5stack-cam-psram/tree/master

## PinMap

**Camera Interface PinMap**

| *Interface*             | *Camera Pin*| *Alternate ESP32 Pin Mapping* | *ESP32Cam*    | *M5Camera(A model)*  | *M5Camera(B model)*  |
| :-------------------  | :--------:| :-------------------------: | :--------:  | :------:  | :------:  |
| SCCB Clock            | SIOC      | IO23                        | IO23        |IO23       |IO23       |
| SCCB Data             | SIOD      | IO25                        | IO25        |**IO25**       |**IO22**       |
| System Clock          | XCLK      | IO27                        | IO27        |IO27       |IO27       |
| Vertical Sync         | VSYNC     | IO22                        | IO22        |**IO22**       |**IO25**       |
| Horizontal Reference  | HREF      | IO26                        | IO26        |IO26       |IO26       |
| Pixel Clock           | PCLK      | IO21                        | IO21        |IO21       |IO21       |
| Pixel Data Bit 0      | D2        | IO35                        | IO17        |IO32       |IO32       |
| Pixel Data Bit 1      | D3        | IO17                        | IO35        |IO35       |IO35       |
| Pixel Data Bit 2      | D4        | IO34                        | IO34        |IO34       |IO34       |
| Pixel Data Bit 3      | D5        | IO5                         | IO5         |IO5        |IO5        |
| Pixel Data Bit 4      | D6        | IO39                        | IO39        |IO39       |IO39       |
| Pixel Data Bit 5      | D7        | IO18                        | IO18        |IO18       |IO18       |
| Pixel Data Bit 6      | D8        | IO36                        | IO36        |IO36       |IO36       |
| Pixel Data Bit 7      | D9        | IO19                        | IO19        |IO19       |IO19       |
| Camera Reset          | RESET     | IO15                        | IO15        |IO15       |IO15       |
| Camera Power Down     | PWDN      | *see Note 1*                | *see Note 1* | *see Note 1* | *see Note 1* |
| Power Supply 3.3V     | 3V3       | 3V3                         | 3V3         | 3V3       | 3V3       |
| Ground                | GND       | GND                         | GND         | GND       | GND       |

**GROVE Interface**

| *Grove*         | *ESP32Cam*    | *M5Camera(A model)*  | *M5Camera(B model)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| SCL           | IO13        | IO13      | IO13      |
| SDA           | IO4        | **IO12**      | **IO4**      |
| 5V            | 5V          | 5V        | 5V        |
| GND           | GND         | GND       | GND       |

**BME280 Interface**

`Note: the pinmap of BME280 on the old version of M5Camera is SCL -> GPIO23, SDA -> GPIO22, and it's iic address is 0x76. Thanks the issues of [sige1](https://github.com/sige1)(issues#1)`

| *BME280*         | *ESP32Cam*    | *M5Camera(A model)*  | *M5Camera(B model)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| SCL           | IO4         | IO23      | IO23      |
| SDA           | IO13        | IO22      | IO22      |


**MPU6050 Interface**

| *MPU6050*         | *ESP32Cam*    | *M5Camera(A model)*  | *M5Camera(B model)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| SCL           | IO4         | IO23      | IO23      |
| SDA           | IO13        | IO22      | IO22      |

**MIC(SPM1423) Interface**

| *MPU6050*     | *ESP32Cam*        | *M5Camera(A model)*  | *M5Camera(B model)*  |
| :-----------: | :------:  | :------:  | :------:  |
| SCL           | *see Note 2*      |IO2|IO2|
| SDA           | *see Note 2*      |IO4|IO4|

**MIC(SPQ2410) Interface**

| *MPU6050*            | *ESP32Cam*  | *M5Camera(A model)*  | *M5Camera(B model)*  |
| :-----------: | :------:  |:------:  |:------:  |
| SCL           | IO32      |*see Note 2*|*see Note 2*|

**LED Interface**

| *LED*         | *ESP32Cam*    | *M5Camera(A model)*  | *M5Camera(B model)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| LED_Pin           | IO16        | IO14      | IO14      |

Notes:

1. **Camera Power Down** pin does not need to be connected to ESP32 GPIO. Instead it may be pulled down to ground with 10 kOhm resistor.
2. **MIC Interface** MIC IC on ESP32Cam is SPQ2410. It is mapped to GPIO32. MIC IC on M5Camera is SPM1423. It is mapped to GPIO2 and GPIO4.

![Image text](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/m5camera_B.png)

**The picture of A model and B model**

![Image text](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/diff_A_B.png)
