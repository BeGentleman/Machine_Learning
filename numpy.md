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
     
     d.矩阵的选取    
     用例子来说明：    
     >>> a = np.array([[1,2,3],[4,5,6]])    
     # 先创建一个二维矩阵    
     >>> a    
     array([[1, 2, 3],    
            [4, 5, 6]])    
     # 取矩阵当中的所有内容    
     >>> a[:]    
     array([[1, 2, 3],    
            [4, 5, 6]])    
     # 反转矩阵，因为是二维数组在同一个维度当中，所以直接反转的化，会将当前维度的所有元素整体进行反转    
     >>> a[::-1]    
     array([[4, 5, 6],    
            [1, 2, 3]])    
     # 二维数组，不能有两个::    
     >>> a[:,:,::-1]    
     Traceback (most recent call last):    
       File "<stdin>", line 1, in <module>    
     IndexError: too many indices for array: array is 2-dimensional, but 3 were indexed    
     # 第一个冒号，代表从头到尾都选取，然后进行反转    
     >>> a[:,::-1]    
     array([[3, 2, 1],    
            [6, 5, 4]])    

     e.各种常用函数    
     np.random.randint()    
     
     np.zeros()    
     
     np.ones()    
     
     np.empty()    
     
     np.shape()    
     
     np.reshape()    
     
     np.eye()    
     用法：    
     生成一个单位矩阵    
     
     举例：    
     >>> d = np.eye(3)    
     >>> d    
     array([[1., 0., 0.],    
            [0., 1., 0.],    
            [0., 0., 1.]])    
            
     np.where()    
     用法:    
     符合条件置为1，不符合条件置为-1    
     
     举例：    
     >>> cond = np.arange(10)    
     >>> cond    
     array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])    
     >>> np.where(cond, 1, -1)    
     array([-1,  1,  1,  1,  1,  1,  1,  1,  1,  1])    
     >>> np.where(cond>5, 1, -1)    
     array([-1, -1, -1, -1, -1, -1,  1,  1,  1,  1])    
     
     np.argmax()    
     用法：    
     找到第一个最大值的索引    
     
     举例：    
     >>> import numpy as np    
     >>> array_1 = np.array([1,5,68,98,2,6,452,12,7,13])    
     >>> print(np.argmax(array_1))    
     6    
     
     >>> array_2 = np.array([1,5,68,98,2,6,452,12,7,452])    
     >>> print(np.argmax(array_2))    
     6    
     >>>    
     
     np.polyfit()    
     最小二次拟合    
     
     用法：    
     
     举例：    
     
     
     
     np.mean()    
     用法：求平均值    
     举例：    
     >>> import numpy as np    
     >>> n1 = np.array([[1, 2, 3], [4, 5, 6]])    
     >>> n2 = np.mean(n1)    
     >>> n2    
     3.5    
     >>>    
     
     np.std()    
     用法：求标准差    
     举例：    
     >>> import numpy as np    
     >>> n1 = np.array([[1, 2, 3], [4, 5, 6]])    
     >>> n3 = np.std(n1)    
     >>> n3    
     1.707825127659933    
     >>>    

     
     np.multiply(参数1, 参数2)    
     用法：对应元素为相乘    
     举例：    
     >>> import numpy as np    
     >>> n1 = np.array([[1, 2, 3], [4, 5, 6]])    
     >>> n2 = np.mean(n1)    
     >>> n2    
     3.5    
     >>> n3 = np.std(n1)    
     >>> n3    
     1.707825127659933    
     >>> n4 = np.array([[0, 1, 2], [0, 1, 2]])    
     >>> n5 = np.multiply(n1, n4)    
     >>> n5    
     array([[ 0,  2,  6],    
            [ 0,  5, 12]])    



     
     f.矩阵乘法    
     用关键字 @    
     矩阵乘法流程：    
     # TODO    
