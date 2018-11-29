# Schematic difference

*This document will introduct the difference between those m5cores(i.e. M5Core Basic(the Black one), M5Core GRAY, M5Fire(the Red one), M5Core WHITE)*

Currently, we have 4 kinds of M5Cores and one minicore(*named M5Stick*). They are simliar to each other.

**Be carefull, the arly version of M5Fire was built in MPU6050 + MAGE3110, but we change MPU6050 + MAGE3110 to MPU9250.**

*IIC Address*

*MPU9250: 0x68*

*IP5360:  0x0E*

## Difference

**Camera Interface PinMap**

| *Difference*          | *M5Core Basic*    | *M5Core GRAY*                 | *M5Core WHITE*    | *M5Fire*      |
| :-------------------  | :--------:        | :-------------------------:   | :--------:        | :------:      |
| MEMS                  | No MEMS           | MPU9250                       | MPU9250           |MPU9250        |
| RAM                   | 520KB             | 520KB                         | 520KB             |520KB+4M             |
| FLASH                 | 4M                | 4M                            | 4M+16M                |4M+16M            |


## 1. M5Core Basic

M5Core Basic = main board + m5core base

![M5Core Basic](basic.jpg)

https://m5stack.github.io/m5-docs/#/en/product_documents/m5stack-core/m5core_basic

## 2. M5Core GRAY

M5Core GRAY = main board + m5core base

![M5Core GRAY](gray.jpg)

https://m5stack.github.io/m5-docs/#/en/product_documents/m5stack-core/m5core_gray

## 3. M5Core WHITE

M5Core WHITE = main board + m5go base

![M5Core WHITE](m5go.png)

https://m5stack.github.io/m5-docs/#/en/product_documents/m5stack-core/m5core_white

## 4. M5Core M5Fire

M5Core M5Fire = main board + m5go base

![M5Core M5Fire](fire.jpg)

https://m5stack.github.io/m5-docs/#/en/product_documents/m5stack-core/m5core_fire
