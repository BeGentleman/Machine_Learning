import torch

'''
dim = 0 表示在第0维度进行变换（即针对于列分别求均值然后放到一行中）
dim = 1 表示在第1维度进行变换（即针对于行分别求均值然后放到每一列中）
keepdim = True 表示不改变维度，加入原始数组是 二维，那么当keepdim = True的时候，变换后的数组也是二维的
'''
a = torch.arange(12).view(3, 4).float()
print("a输出为：")
print(a)

mean_1 = torch.mean(a)
print("直接对a求均值获得:", mean_1)

mean_2 = torch.mean(a, dim=0, keepdim=True)
print("指定dim为0获得：", mean_2)

mean_3 = torch.mean(a, dim=1, keepdim=True)
print("指定dim为1获得：", mean_3)

mean_4 = torch.mean(a, dim=1)
print("不指定keepdim=True结果为：", mean_4)

'''
输出结果展示：

a输出为：
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
直接对a求均值获得: tensor(5.5000)
指定dim为0获得： tensor([[4., 5., 6., 7.]])
指定dim为1获得： tensor([[1.5000],
        [5.5000],
        [9.5000]])
不指定keepdim=True结果为： tensor([1.5000, 5.5000, 9.5000])
'''