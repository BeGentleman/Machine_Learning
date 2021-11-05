import torch
from torch import nn

'''
说明：
nn.Linear(input, output, bias=True)
paramter: input为输入图像尺寸，为tensor张量
paramter: output为输出图像尺寸，为tensor张量
paramter: bias默认值为True，有偏置
'''

m = nn.Linear(20, 30, bias=True)
input = torch.randn(128, 20)

out = m(input)
print("权重：", m.weight, "SIZE是：", m.weight.size())
print("偏置：", m.bias, "SIZE是：", m.bias.size())
print("输出尺寸：", out.size())

final = torch.mm(input, m.weight.t())+m.bias
print("也是输出尺寸，是为了验证公式y=kx+b:", final, "SIZE是：", final.size())

if torch.equal(out, final):
    print("公式成立")
else:
    print("公式不成立")