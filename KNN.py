import numpy as np
import math
import random
import pandas as pd

# 定义数据点类
class ShuJuDian():
# 类方法 __init__(self, index, coordinate)
    def __init__(self, index, coordinate):
        # 类属性：self.index = 0 保存该元素在原数据集中的索引
        self.index = index
        # 类属性：self.coordinate = [x, y] 使用传入的coordinate初始化类属性坐标[x, y]
        self.coordinate = coordinate
        # 类属性：self.distance = {index：distance}所有点到该点的距离
        self.distance = []
        # 对于距离属性建议使用元组（index，distance）或字典{index: distance}格式存储

        # 类方法：calculate_all_distance(distance_matrix)
        # 接收一个存储所有数据点坐标的列表，计算所有点对应此点的欧氏距离，将结果按照格式{index: distance}存入distance

    def calculate_all_distance(self, distance_matrix):
        for element in enumerate(distance_matrix):
            self.coordinate = np.array(self.coordinate)
            element = np.array(element)

            temp={}
            result = math.sqrt(sum((self.coordinate - element[1])**2))
            temp["index"] = element[0]
            temp["distance"] = result
            self.distance.append(temp)

    # 类方法：sort_and_cut(k)
    # 将distance进行升序排序，并通过传入的k值选取距离最近的k个元素
    def sort_and_cut(self, k):
        # temp中存放的是距离升序的列表，
        # 格式： [{"index":1, "distance":1},
        #        {"index":2, "distance":3}]

        self.distance.sort(key=lambda x: x["distance"])
        return self.distance[:k]

    # 结束类定义

if __name__ == "__main__":
    # 读取数据
    data_set = pd.read_csv("D:\数据集\iris.data", header=None)
    data_set = np.array(data_set)
    np.random.shuffle(data_set)
    data_set = pd.DataFrame(data_set)
    data_label = np.array(data_set.iloc[:, -1])
    data_label = np.unique(data_label).tolist()
    # print("AKSDJLASKDJSLKD::::", data_label)
    # print("data_set:", data_set)
    # 数据预处理

    # 截取数据集的前80%作为训练集train_set，剩余20%作为测试集test_set
    mark = int(len(data_set)*0.8)
    train_set = data_set.iloc[:mark, :]
    test_set = data_set.iloc[mark:, :]

    # train_set处理
    # 截取训练集最后一列作为标签
    train_label = np.array(train_set.iloc[:, -1]).tolist()
    # 截取训练集剩余部分作为特征
    train_feature = np.array(train_set.iloc[:, :-1]).tolist()


    # test_set处理
    # 截取测试集最后一列作为标签
    test_label = np.array(test_set.iloc[:, -1]).tolist()
    # print("label:", test_label)
    # 截取测试集剩余部分作为特征
    test_feature = np.array(test_set.iloc[:, :-1]).tolist()
    # print("test_feature: ", test_feature)

    # 随机从test_set中选取一个元素test_sample作为测试用例
    random_index = random.randint(0, len(test_set))
    test_data_feature = test_feature[random_index]
    test_data_label = test_label[random_index]
    # 使用test_sample的所有特征的作为coordinate实例化一个数据点对象
    point = ShuJuDian(random_index, test_data_feature)
    print(point.index, point.coordinate)

    # 计算所有点到test_sample的距离
    point.calculate_all_distance(train_feature)
    print(point.distance)
    # 排序并选取最近的k的元素

    k_cut = point.sort_and_cut(5)
    print(k_cut)

    # 统计这5个元素中各个类别分别包含多少元素
    temp = []
    for i in k_cut:
        if train_label[i["index"]] == data_label[0]:
            temp.append(data_label[0])
        elif train_label[i["index"]] == data_label[1]:
            temp.append(data_label[1])
        elif train_label[i["index"]] == data_label[2]:
            temp.append(data_label[2])

    result = max(temp, key=temp.count)
    print(result)
    print(test_label[point.index])

    # 返回拥有最多元素的类名

    # 查看是否准确
    # 通过该元素的索引，在标签集中查看结果

    pass
