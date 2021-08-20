# 常用方法：
1.dnn.blobFromImage
根据输入的图像创建通道数为C，高H,宽W的图像

参数有
~~~python
cv2.dnn.blobFromImage(img,
                      scalefactor=None,
                      size=None,
                      mean=None,
                      swapRB=None,
                      crop=None,
                      ddepth=None)

# img: 读取的目标图像
# scalefactor: 缩放像素值，比如将[0,255]缩小到[0,1]之间
# size: 输出blob图像的尺寸，格式如 size=(宽, 高)
# mean: 从各通道减均值，输入的image如果是从opencv读取来的，顺序是BGR，需要将swapRB置为True，通道变为(mean-R, mean-G, mean-B)
# crop: **表示将图像resize后是否进行剪裁，如果剪裁就置为True。剪裁的时候，先固定一个短的，然后去裁剪长的，因为只有这样才能符合逻辑（没有根本剪裁不了）**这个可能不对，有待验证，不能用作参考
# TODO:补充完整
~~~
