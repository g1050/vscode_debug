import argparse
import numpy as np
from algo import matmul
def generate_matrix(rows, cols):
    """生成一个给定形状(rows, cols)的矩阵，元素为随机整数"""
    return np.random.randint(0, 10, size=(rows, cols))

def main():
    parser = argparse.ArgumentParser(description="生成两个指定形状的矩阵A和B")
    parser.add_argument('--a-shape', type=int, nargs=2, metavar=('m', 'n'), required=True,
                        help="矩阵A的形状，格式: m n")
    parser.add_argument('--b-shape', type=int, nargs=2, metavar=('n', 'p'), required=True,
                        help="矩阵B的形状，格式: n p")
    args = parser.parse_args()

    m, n_a = args.a_shape
    n_b, p = args.b_shape

    if n_a != n_b:
        raise ValueError("矩阵A的列数必须等于矩阵B的行数 (A的shape: (%d, %d), B的shape: (%d, %d))" % (m, n_a, n_b, p))

    A = generate_matrix(m, n_a)
    B = generate_matrix(n_b, p)
    print(f"A.shape {A.shape}")
    print(f"B.shape {B.shape}")
    C = matmul(A,B)
    print(f"C.shape {C.shape}")

if __name__ == "__main__":
    main()
