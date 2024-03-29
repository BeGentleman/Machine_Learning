# 这个文件主要用于模型搭建，并可视化模型结构和参数

from torch import nn
import torch as t
from torch.nn import functional as F
import cv2

class ResdiualBlock(nn.Module):
    """
    实现子module：Residual Block
    """
    def __init__(self, inchannel, outchannel, stride=1, shortcut=None):
        super(ResdiualBlock, self).__init__()
        self.left = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, 3, stride, 1, bias=False),
            nn.BatchNorm2d(outchannel),
            nn.ReLU(inplace=True),
            nn.Conv2d(outchannel, outchannel, 3, 1, 1, bias=False),
            nn.BatchNorm2d(outchannel)
        )

        self.right = shortcut

    def forward(self, x):
        out = self.left(x)
        residual = x if self.right is None else self.right(x)
        out += residual
        return F.relu(out)


class ResNet(nn.Module):
    """
    实现主Module：ResNet34
    ResNet34包含多个layer， 每个layer又包含多个residual block
    用子module实现residual block， 用_make_layer函数实现layer
    """

    def __init__(self, num_classes=1000):
        super(ResNet, self).__init__()
        # 图像转换
        self.pre = nn.Sequential(
            # in_channel, out_channel, kernel_size, stride, padding
            nn.Conv2d(3, 64, 7, 2, 3, bias=False, ),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(3, 2, 1)
        )

        # 重复的layer， 分别有3，4，6，3 个residual block
        self.layer1 = self._make_layer(64, 128, 3)
        self.layer2 = self._make_layer(128, 256, 4, stride=2)
        self.layer3 = self._make_layer(256, 512, 6, stride=2)
        self.layer4 = self._make_layer(512, 512, 3, stride=2)

        # 全连接分类
        self.fc = nn.Linear(512, num_classes)

    def _make_layer(self, inchannel, outchannel, block_num, stride=1):
        """
        构建residual block
        """
        shortcut = nn.Sequential(
            nn.Conv2d(inchannel, outchannel, 1, stride, bias=False),
            nn.BatchNorm2d(outchannel)
        )

        layers = []
        layers.append(ResdiualBlock(inchannel, outchannel, stride, shortcut))
        for i in range(1, block_num):
            layers.append(ResdiualBlock(outchannel, outchannel))
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.pre(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = F.avg_pool2d(x, 7)
        x = x.view(x.size(0), -1)
        return self.fc(x)


model = ResNet()
# input = t.autograd.Variable(t.randn(1,2,244,244))
# out = model(input)

print(model)

from torchvision import models
from torchsummary import summary

resnet = models.resnet101()
print(resnet)
summary(resnet, (3, 224, 224), device='cpu')
