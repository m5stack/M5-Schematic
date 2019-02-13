# M5Core硬件配置上的比较

**[English](https://github.com/m5stack/M5-Schematic/blob/master/Core/hardware_difference_between_cores.md)** | **中文** | **[日本語](https://github.com/m5stack/M5-Schematic/blob/master/Core/hardware_difference_between_cores_ja.md)**

*这篇文章主要是介绍M5Core硬件配置上的不同(i.e. [M5Core Basic](https://docs.m5stack.com/#/zh_CN/core/basic)(黑色版本), [M5Core GRAY](https://docs.m5stack.com/#/zh_CN/core/gray)(灰色版本), [M5Fire](https://docs.m5stack.com/#/zh_CN/core/fire)(红色版本), [M5Core WHITE](https://docs.m5stack.com/#/zh_CN/core/m5go_lite), [M5Stick White](https://docs.m5stack.com/#/zh_CN/core/m5stick), [M5Stick Gray](https://docs.m5stack.com/#/zh_CN/core/m5stick))*

目前，我们有4种Core主控和两个迷你型主控M5Stick。他们之间都很相似。

**注意，最新版本的M5Core Fire里面的姿态传感器是MPU9250，之前是配置MPU6050和MAG3110，后面都改成MPU9250了.**

*IIC地址*

*MPU9250: 0x68*

*IP5360:  0x0E*

## 差异

下图是展示了主控之间的主要区别，如果你想查看每一款主控的详细资源对比的话，点击[这里](https://shimo.im/sheets/qdPK9x6RCWQwc3WK/gO4S0)。

<img src="https://github.com/m5stack/M5-Schematic/blob/master/Core/core_comparison_04_zh_CN.png">

<img src="https://github.com/m5stack/M5-Schematic/blob/master/Core/core_comparison_05_zh_CN.png">


<!-- <img src="https://github.com/m5stack/M5-Schematic/blob/master/Core/core_comparison.png">

## 1. M5Core Basic基础套件

M5Core Basic = 黑色主控板BASIC+m5core base底座

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_basic

<img src="https://github.com/m5stack/M5-Schematic/blob/master/Core/basic.jpg" width = "500" height = "500">

## 2. M5Core GRAY

M5Core GRAY = 灰色主控板GRAY+m5core base底座

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_gray

<img src="https://github.com/m5stack/M5-Schematic/blob/master/Core/gray.jpg" width = "500" height = "500">

## 3. M5Core WHITE

M5Core WHITE = 白色主控板+m5go base底座

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_white

<img src="https://github.com/m5stack/M5-Schematic/blob/master/Core/m5go.png" width = "500" height = "500">

## 4. M5Core M5Fire

M5Core M5Fire = 红色主控板FIRE+m5go base底座

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_fire

<img src="https://github.com/m5stack/M5-Schematic/blob/master/Core/fire.jpg" width = "500" height = "500"> -->
