0x00 numpy库的作用
     最主要的功能是用来做矩阵运算。



0x01 需要掌握的基本概念
     a.什么是矩阵？
     b.什么是向量？


0x02 numpy的基本操作
     a.创建一个矩阵
     
     b.随机数种子
     >>> import numpy as np
     >>> np.random.seed(0)
     >>> a = np.random.random()
     >>> a
     0.5488135039273248
     >>> b = np.random.random()
     >>> b
     0.7151893663724195
     >>> np.random.seed(0)
     >>> c = np.random.random()
     >>> c
     0.5488135039273248
     >>>

     a和b的值相等，就是用随机数种子做到的，随机数种子用来固定生成的随机数。
     
     c.unique
     用来找到所有变量(拥有去掉重复值的功能)
     
     >>> a = np.array([[1,1,1,1,2,2,3,4]])
     >>> a
     array([[1, 1, 1, 1, 2, 2, 3, 4]])
     >>> np.unique(a)
     array([1, 2, 3, 4])

     >>> b = np.array([1,1,1,1,2,2,3,4])
     >>> b
     array([1, 1, 1, 1, 2, 2, 3, 4])
     >>> np.unique(b)
     array([1, 2, 3, 4])

     >>> c = np.array([[1,2,3,3,4],[3,4,5,5,6]])
     >>> c
     array([[1, 2, 3, 3, 4],
            [3, 4, 5, 5, 6]])
     >>> np.unique(c)
     array([1, 2, 3, 4, 5, 6])
     
