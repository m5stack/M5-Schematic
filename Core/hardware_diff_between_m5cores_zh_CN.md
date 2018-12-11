# M5Core硬件配置上的比较

*这篇文章主要是介绍M5Core硬件配置上的不同(包括M5Core Basic基础版(黑色), M5Core GRAY, M5Fire(红色), M5Core WHITE)*

目前，我们有4种Core主控和一个迷你型主控M5Stick。他们之间都很相似。

**注意，最新版本的M5Core Fire里面的姿态传感器是MPU9250，之前是配置MPU6050和MAGE3110，后面都改成MPU9250了.**

*IIC地址*

*MPU9250: 0x68*

*IP5360:  0x0E*

## 差异

| *不同之处*          | *M5Core Basic*    | *M5Core GRAY*                 | *M5Core WHITE*    | *M5Fire*      |
| :-------------------  | :--------:        | :-------------------------:   | :--------:        | :------:      |
| 有无姿态传感器                  | 没姿态传感器           | MPU9250                       | MPU9250           |MPU9250        |
| RAM                   | 520KB             | 520KB                         | 520KB             |520KB+4M             |
| FLASH                 | 4M                | 4M                            | 4M+16M                |4M+16M            |


## 1. M5Core Basic基础套件

M5Core Basic = 黑色主控板BASIC+m5core base底座

![M5Core Basic](basic.jpg)

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_basic

## 2. M5Core GRAY

M5Core GRAY = 灰色主控板GRAY+m5core base底座

![M5Core GRAY](gray.jpg)

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_gray

## 3. M5Core WHITE

M5Core WHITE = 白色主控板+m5go base底座

![M5Core WHITE](m5go.png)

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_white

## 4. M5Core M5Fire

M5Core M5Fire = 红色主控板FIRE+m5go base底座

![M5Core M5Fire](fire.jpg)

https://m5stack.github.io/m5-docs/#/zh_CN/product_documents/m5stack-core/m5core_fire
