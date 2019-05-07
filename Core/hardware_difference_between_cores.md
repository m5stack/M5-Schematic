# Schematic difference

**English** | **[中文](https://github.com/m5stack/M5-Schematic/blob/master/Core/hardware_difference_between_cores_zh_CN.md)** | **[日本語](https://github.com/m5stack/M5-Schematic/blob/master/Core/hardware_difference_between_cores_ja.md)**

*This document will introduct the difference between those cores(i.e. [M5Core Basic](https://docs.m5stack.com/#/en/core/basic)(the Black one), [M5Core GRAY](https://docs.m5stack.com/#/en/core/gray)(the Gray one), [M5Fire](https://docs.m5stack.com/#/en/core/fire)(the Red one), [M5Core WHITE](https://docs.m5stack.com/#/en/core/m5go_lite), [M5Stick White](https://docs.m5stack.com/#/en/core/m5stick), [M5Stick Gray](https://docs.m5stack.com/#/en/core/m5stick))*

Currently, we have 4 kinds of M5Cores and two minicores(*named M5Stick*). They are simliar to each other.

**Be careful, the early version of M5Fire was built in MPU6050 + MAG3110, but we change MPU6050 + MAG3110 to MPU9250.**

*IIC Address*

*MPU9250: 0x68*

*IP5360:  0x0E*

## Difference

The following figure shows the main difference.

If you want to **view** the whole resource about cores, please click [here](https://shimo.im/sheets/7ZzkLVJNGolsB3QE/D0n0x).

If you want to **download** this detailed comparison table about cores, please click [here](https://github.com/m5stack/M5-Schematic/blob/master/Core/M5%20Core%20Detailed%20Comparison.xlsx).

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/core_comparison/core_main_comparison_04_en.png">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/core_comparison/core_main_comparison_05_en.png">
