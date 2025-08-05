import numpy as np

def matmul(A, B):
    """
    计算两个矩阵A和B的乘积。
    :param A: 形状为(m, n)的numpy数组
    :param B: 形状为(n, p)的numpy数组
    :return: 形状为(m, p)的numpy数组，表示A和B的乘积
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("矩阵维度不匹配，无法相乘")
    return np.matmul(A, B)
