# 摄像头 Unit 之间的对比

**[English](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/CameraComparison_en.md)**

目前，M5Stack 有四种类型的摄像头 Unit，分别是 [ESP32CAM](https://docs.m5stack.com/#/zh_CN/unit/esp32cam), [M5Camera (A Model)](https://docs.m5stack.com/#/zh_CN/unit/m5camera), [M5Camera (B Model)](https://docs.m5stack.com/#/zh_CN/unit/m5camera), M5CameraX, [M5CameraF](https://docs.m5stack.com/#/zh_CN/unit/m5camera_f)。

这些摄像头主要差异是**内存**、**接口**、**镜头**、**可选配置的硬件**和**外壳**。下图是他们的对比表格 (<mark>注意</mark>：因为接口有很多引脚不相同，所以还单独做了表格来对比。)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/camera_comparison/camera_main_comparison_zh_CN.png">

### 接口对比

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/camera_comparison/CameraPinComparison_zh_CN.png">


**<mark>固件地址</mark>**

- ESP32Cam 固件地址：https://github.com/m5stack/m5stack-cam-psram/tree/NoPsram

- M5Camera 固件地址 ( A model )：https://github.com/m5stack/m5stack-cam-psram/tree/ModeA

- M5Camera 固件地址 ( B model )：https://github.com/m5stack/m5stack-cam-psram/tree/master

- M5CameraX 固件地址：https://github.com/m5stack/m5stack-cam-psram/tree/master

- M5CameraF 固件地址：https://github.com/m5stack/m5stack-cam-psram/tree/FishEye

<!-- ## 管脚对比

**摄像头驱动芯片 OV2640 接口**

| *接口*             | *OV2640 引脚*| *Alternate ESP32 Pin Mapping* | *ESP32Cam*    | *M5Camera(A 版本)*  | *M5Camera(B 版本)*  |
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

**GROVE 接口**

| *Grove*         | *ESP32Cam*    | *M5Camera(A 版本)*  | *M5Camera(B 版本)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| SCL           | IO13        | IO13      | IO13      |
| SDA           | IO4        | **IO12**      | **IO4**      |
| 5V            | 5V          | 5V        | 5V        |
| GND           | GND         | GND       | GND       |

**BME280 接口**

`Note: the pinmap of BME280 on the old version of M5Camera is SCL -> GPIO23, SDA -> GPIO22, and it's iic address is 0x76. Thanks the issues of [sige1](https://github.com/sige1)(issues#1)`

| *BME280*         | *ESP32Cam*    | *M5Camera(A 版本)*  | *M5Camera(B 版本)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| SCL           | IO4         | IO23      | IO23      |
| SDA           | IO13        | IO22      | IO22      |


**MPU6050 接口**

| *MPU6050*         | *ESP32Cam*    | *M5Camera(A 版本)*  | *M5Camera(B 版本)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| SCL           | IO4         | IO23      | IO23      |
| SDA           | IO13        | IO22      | IO22      |

**MIC(SPM1423) 接口**

| *MPU6050*     | *ESP32Cam*        | *M5Camera(A 版本)*  | *M5Camera(B 版本)*  |
| :-----------: | :------:  | :------:  | :------:  |
| SCL           | *see Note 2*      |IO2|IO2|
| SDA           | *see Note 2*      |IO4|IO4|

**MIC(SPQ2410) 接口**

| *MPU6050*            | *ESP32Cam*  | *M5Camera(A 版本)*  | *M5Camera(B 版本)*  |
| :-----------: | :------:  |:------:  | :------:  |
| SCL           | IO32      |*see Note 2*|*see Note 2*|

**LED 接口**

| *LED*         | *ESP32Cam*    | *M5Camera(A 版本)*  | *M5Camera(B 版本)*  |
| :-----------: | :--------:  | :------:  | :------:  |
| LED_Pin           | IO16        | IO14      | IO14      |

Notes:

1. **Camera Power Down 引脚** 没必要连接到 ESP32 的引脚。

2. **麦克风引脚** ESP32Cam 上的麦克风 IC 是 SPQ2410，连接到 GPIO32 引脚。M5Camera 上的麦克风 IC 是 SPM1423，连接到 GPIO2 和 GPIO4 引脚。

![Image text](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/m5camera_B.png) -->

**A model 和 B model 的图片**

![Image text](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/diff_A_B.png)
