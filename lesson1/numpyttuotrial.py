import numpy as np
import pandas as pd

class Perceptron(object):
    """分类器
    变量
    -------------
    eta : float
    学习速率

    n_iter : int
    传递训练数据集

    属性
    -------------
    w_ : 数组
        计算后的权重
    errors_ : list
        错误分类集
    """
    def _init_(self, eta=0.01, n_iter=50, random_seed=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_seed = random_seed

    def fit(self, X, y):
        """
        X : 输入训练集
        y : 目标值
        self : object
        """ 
        # self.w_ = np.zeros(1 + X.shape[1])
        rgen = np.random.RandomState(self.random_seed)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for Xi, target in zip(X, y):
                update = self.eta * (target - self.predict(Xi))
                self.w_[1:] += update
                self.w_[0] += update #阀值
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:] + self.w_[0])

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
        





