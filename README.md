# 100題影像處理練習
日文原文：[画像処理100本ノック!!](https://github.com/ryoppippi/Gasyori100knock)

英文翻譯：[Image Processing 100 Questions](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master)

中文翻譯：[图像处理 100 问！！](https://github.com/gzr2017/ImageProcessing100Wen)

## 說明
此專案為個人練習tkinter、opencv、函式外部化用，因此不會有詳細解說，若想學習更多，請參考原作者的教學。
1. 至functions資料夾創建所需功能的py檔案，內含同名的函式。
2. 至主資料夾執行generate_init.py，產生一個init.py檔案，裡面包含所有函式的參考。
3. 至主資料夾執行main.py，即可執行各題的程式碼。

## 目前更新
- 第一題：通道轉換  
  - 程式碼：Q1_Channle_Swapping.py
  - 說明：將BGR三通道的影像轉換成RGB三通道的影像。
- 第二題：灰階化
  - 程式碼：Q2_Grayscale.py
  - 說明：將RGB三通道的影像轉換成灰階影像。灰階化公式 \(Y = 0.2126R + 0.7152G + 0.0722B\) 是基於人眼對不同顏色敏感度的加權，將彩色圖像轉換為灰度圖像，其中綠色影響最大，藍色最小，紅色居中。
- 第三題：二值化
  - 程式碼：Q3_Binarization.py
  - 說明：將影像二值化，只有黑白兩色。
- 第四題：大津二值化
  - 程式碼：Q4_Binarization_of_Otsu.py
  - 說明：大津二值化是一種自動決定閥值以把圖片上的物體和背景清晰分開的方法。
- 第五題：色彩空間轉換
  - 程式碼：Q5_HSV_Conversion.py
  - 說明：將RGB三通道的影像轉換成HSV色彩空間的影像，反轉H色相(+180)後轉回RGB以顯示影像。
- 第六題：Discretization of Color
  - 程式碼：Q6_Discretization_of_Color.py
  - 說明：將RGB三通道的影像轉換成8種顏色的影像。
- 第七題：Average Pooling
  - 程式碼：Q7_Average_Pooling.py
  - 說明：平均池化是一種影像處理技術，它會將影像的大小縮小，並取出影像中某一區域的平均值，以降低影像的分辨率。