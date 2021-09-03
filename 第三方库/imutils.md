# 主要作用：
对opencv进行封装，让 图像的平移，旋转，缩放，提取骨架一系列操作更加简单

# 安装：
pip install imutils

# 用法：
## 图像平移
~~~python
translated = imutils.translate(img, x, y)
# img:要移动的目标图像
# x:沿x轴方向移动的像素个数
# y:沿y轴方向移动的像素个数
~~~

## 图像旋转
~~~python
rotated = imutils.rotate(img, 90)
rotated_round = imutils.rotate_bound(img, 90)
# img:要旋转的目标图像
# imutils.rotate是逆时针旋转，第二个参数是旋转的角度
# imutils.rotate_bound是顺时针旋转，第二个参数是旋转的角度
~~~

## 图像缩放
~~~python
resized = imutils.resize(img, width=shuzi)
# img:要缩放的目标图像
# width:这里的width也可以是height，因为在imutils中，是宽高比保持不变的缩放，因此指定一个就可以了
~~~

## 图像提取骨架
*注意：不是所有的图像都可以进行骨架提取
提取的骨架一般用于结构光（日后补充）
~~~python
# 首先要将要提取的图像转换成灰度图
# 然后才能进行骨架提取
skeleton = imutils.skeletonize(gray, size=(3, 3))
# gray:时已经转化为灰度图的目标图像
# size(3, 3):表示要提取骨架的细粒程度，这个数字越小，表示越细，需要的时间就越长。（日后查询更加细节的资料补充上）
~~~
