import numpy as np

def print_matrix(matrix, title="Matrix", precision=2):
    print(f"{title}:\n")
    with np.printoptions(precision=precision, suppress=True):
        print(matrix)
    print("\n")