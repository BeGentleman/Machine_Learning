import torch

a = torch.randn(3, 5)
b = torch.randn(3, 5)

# 解析：where的作用在于合并两个tensor类型的数据，按照a > 0的条件来合并
torch.where(a>0, a, b)