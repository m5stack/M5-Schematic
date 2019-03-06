# Camera Units Comparison

**[English](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/CameraComparison_en.md)** - **[中文](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/CameraComparison_zh_CN.md)** - 日本語

現在、M5Stackには4つのタイプのカメラユニットがあります。それぞれ[ESP32CAM](https://docs.m5stack.com/#/ja/unit/esp32cam)、[M5Camera (A Model)](https://docs.m5stack.com/#/ja/unit/m5camera)、[M5Camera (B Model)](https://docs.m5stack.com/#/ja/unit/m5camera)、M5CameraX、[M5CameraF](https://docs.m5stack.com/#/ja/unit/m5camera_f)。

主な違いは **メモリ**、**インターフェース**、**レンズ**、**オプションのハードウェア**、**ケース**です。

以下に比較表を示します。(<mark>ノート:</mark>インターフェースのピン配列なども異なるので、比較するために別の表を作成しました。)

- もし比較表を**参照**したい場合は[こちら](https://shimo.im/sheets/gP96C8YTdyjGgKQC)。

- もし比較表を**ダウンロード**したい場合は[こちら](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/M5%20Camera%20Detailed%20Comparison.xlsx)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/camera_comparison/camera_main_comparison_ja.png">

### インターフェース比較

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_table/camera_comparison/CameraPinComparison_en.png">

**<mark>ファームウェアリンク</mark>**

- ESP32Cam ファームウェア: https://github.com/m5stack/m5stack-cam-psram/tree/NoPsram

- M5Camera ファームウェア ( A model ): https://github.com/m5stack/m5stack-cam-psram/tree/ModeA

- M5Camera ファームウェア ( B model ): https://github.com/m5stack/m5stack-cam-psram/tree/master

- M5CameraX ファームウェア: https://github.com/m5stack/m5stack-cam-psram/tree/master

- M5CameraF ファームウェア: https://github.com/m5stack/m5stack-cam-psram/tree/FishEye

**A model と B modelの違い**

![Image text](https://github.com/m5stack/M5-Schematic/blob/master/Units/m5camera/diff_A_B.png)
