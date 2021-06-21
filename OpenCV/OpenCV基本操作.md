# OpenCV基本操作

##  1.图像的基本操作

### 报错总结：

1.cv.imshow()错误

原因：文件读取错误

解决：将文件正确读取到即可（没有其他错误的前提下=。=）

复现：

```python
import cv2 as cv

img1_0 = cv.imread("C:/Users/y/Desktop/rili.jpg")

cv.imshow('image', img1_0)
cv.waitKey(0)
cv.destroyAllWindows()
```

```python
C:\Users\y\anaconda3\python.exe D:/OpenCV_Deeper/20210607/flow.py
Traceback (most recent call last):
  File "D:/OpenCV_Deeper/daima/flow.py", line 23, in <module>
    cv.imshow('image',img1_0)
cv2.error: OpenCV(3.4.8) C:\projects\opencv-python\opencv\modules\highgui\src\window.cpp:382: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'


Process finished with exit code 1
```

debug发现

![image-20210607201429920](C:\Users\y\AppData\Roaming\Typora\typora-user-images\image-20210607201429920.png)

当文件读取不到以后，img1_0为None，但是不会报错，只有当遇到显示的时候调用了img1_0才会报错。

将路径改正为正确路径，![image-20210607201513477](C:\Users\y\AppData\Roaming\Typora\typora-user-images\image-20210607201513477.png)

图像正确显示。  



2.cv.imshow()错误

原因：参数缺失

解决：cv.imshow(参数一，参数二)

复现：

```python
import cv2 as cv

# 以彩色的模式加载图像，忽略所有透明度（下面三种效果一样）
img1_0 = cv.imread("C:/Users/y/Desktop/img/rili.jpg")
cv.imshow(img1_0)
```

```python
C:\Users\y\anaconda3\envs\opencv\python.exe D:/OpenCV_Deeper/20210607/flow.py
Traceback (most recent call last):
  File "D:/OpenCV_Deeper/daima/flow.py", line 34, in <module>
    cv.imshow(img1_0)
TypeError: Required argument 'mat' (pos 2) not found
```

更改为![image-20210607203815573](C:\Users\y\AppData\Roaming\Typora\typora-user-images\image-20210607203815573.png)



### 读取图像+展示图像+保存图像

```python
"""
Author:-Y-
Date:2021/06/07
Summary:读取图像+展示图像+保存图像
"""
import cv2 as cv

# 读取图像
# 语法：cv.imread(图像所在路径,图像加载模式)
# 以彩色的模式加载图像，忽略所有透明度（下面三种效果一样）
img1_0 = cv.imread("C:/Users/y/Desktop/img/rili.jpg")#图像加载模式不写默认为彩色
img1_1 = cv.imread("C:/Users/y/Desktop/img/rili.jpg", cv.IMREAD_COLOR)
img1_2 = cv.imread("C:/Users/y/Desktop/img/rili.jpg", 1)

# 以灰度的模式加载图像（下面三种效果一样）
img2_0 = cv.imread("C:/Users/y/Desktop/img/rili.jpg", cv.IMREAD_GRAYSCALE)
img2_1 = cv.imread("C:/Users/y/Desktop/img/rili.jpg", 0)

# 以带有透明度的模式加载图像（下面三种效果一样）
img3_0 = cv.imread("C:/Users/y/Desktop/img/rili.jpg", cv.IMREAD_UNCHANGED)
img3_1 = cv.imread("C:/Users/y/Desktop/img/rili.jpg", -1)

# 展示图像
# 语法：cv.imread(窗口名字, 想要展示的图像变量)
cv.imshow("img1_0", img1_0)
cv.imshow("img1_1", img1_1)
cv.imshow("img1_2", img1_2)

cv.imshow("img2_0", img2_0)
cv.imshow("img2_1", img2_1)

cv.imshow("img3_0", img3_0)
cv.imshow("img3_1", img3_1)

# 保存图像
# 会将图像保存到和运行程序一样的目录下,并起名字为img2_0
cv.imwrite("img2_0.png", img2_0)

# @param delay Delay in milliseconds. 0 is the special value that means "forever".
cv.waitKey(0)
# 销毁窗口
cv.destroyAllWindows()

```

效果图

![image-20210607202827718](C:\Users\y\AppData\Roaming\Typora\typora-user-images\image-20210607202827718.png)

![image-20210607202855042](C:\Users\y\AppData\Roaming\Typora\typora-user-images\image-20210607202855042.png)

![image-20210607202920143](C:\Users\y\AppData\Roaming\Typora\typora-user-images\image-20210607202920143.png)

### 绘制几何图形

1.绘制直线

2.绘制圆

3.绘制矩形

4.绘制文字

直接用代码展示

```python
"""
Author:-Y-
Date:2021/06/10
Summary:图像绘制
"""
import cv2 as cv
import numpy as np

# 1 创建一个空白图像
img = np.zeros((512, 512, 3), np.uint8)

# 2.绘制直线
# 语法：cv.line(img,start,end,color,thickness)
cv.line(img, (0, 0), (110, 110), (255, 0, 0), 5)

# 3.绘制圆形
# 语法：cv.circle(img,centerpoint, r, color, thickness)
cv.circle(img, (50, 50), 20, (255, 0, 255), 5)

# 4.绘制矩形
# 语法：cv.rectangle(img,leftupper,rightdown,color,thickness)
cv.rectangle(img, (150, 50), (100, 200), (0, 0, 255), 30)

# 5.绘制文字
# 语法：cv.putText(img,text,station, font, fontsize,color,thickness,cv.LINE_AA)
cv.putText(img, "20210610-Y-测试", (0, 300), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)

cv.imshow("new window", img)
cv.waitKey(0)

```



效果图如下：

![绘制图像效果图](D:\OpenCV_Deeper\asset\绘制图像效果图.png)

注意：如果输入中文文字，会不识别（TODO:如果需要输入中文需要借助PIL库）



### 获取+修改图像中的像素点

图像通道：B G R

用（x, y）来确定像素在图像中的位置

```python
"""
Author:-Y-
Date:2021/06/10
Summary:像素点位置的获取和修改
"""
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('D:/OpenCV_Deeper/asset/IMG_8308.JPG')
plt.imshow(img[:,:,::-1])
plt.show()

# 获取某个像素点的值
# px = img[100, 100]
# print("px", px)
# 仅获取蓝色通道的强度值
# blue = img[100, 100, 0]
# print("blue", blue)
# 修改某个位置的像素值
# img[100, 100] = [255, 255, 255]
# print("修改后", img[100, 100, 0])

# 整体修改
for i in range(50):
    for j in range(50):
        img[1000+i, 2000+j] = [255, 255, 255]

plt.imshow(img[:,:,::-1])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
```

### 通道的拆分与合并

```python
"""
Author:-Y-
Date:2021/06/20
Summary:通道分割+合并
"""
import cv2 as cv

# 先读入图像
img = cv.imread("../asset/yi.png")

# 通道拆分
b, g, r = cv.split(img)
print(b)
print("-------------")
print(g)
print("-------------")
print(r)

cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

# 通道合并
b_g = cv.merge([b, g, g])
cv.imshow("b_g", b_g)

cv.waitKey(0)
cv.destroyAllWindows()

```



### 色彩空间的转换





## 2.算数操作

### 

# OpenCV图像处理

## 1.几何变换

### 图像缩放

```python
import cv2 as cv

# 图像缩放
cv.resize(要缩放的图像, 输出的图像, 输出图像尺寸, 沿x轴缩放系数, 沿y轴缩放系数, 插值方式)
```

插值方式：

cv2.INTER_LINEAR（双线性插值法）

cv2.INTER_NEAREST（最邻近插值法）

cv2.INTER_AREA（像素区域重采样（也是默认的方法））

cv2.INTER_CUBIC（双三次插值）



### 

2.形态学操作
3.图像平滑
4.直方图
5.边缘检测
6.模板匹配和霍夫变换

# 图像特征提取与描述

1.角点特征  
2.Harris和Shi-Tomas算法
3.SIFIT、SURF算法
4.Fast、ORB算法
5.LBP、HOG特征算子

# 视频操作

1.视频读写
2.视频追踪