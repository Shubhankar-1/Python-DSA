import numpy as np


class Solution:
    def matrixReshape(mat, r, c):
        new_matrix = []
        no_of_col = len(mat)
        no_of_row = len(mat[0])
        if (no_of_col*no_of_row) == (r*c):
            new_matrix = np.reshape(mat, (r, c))
            return new_matrix
        else:
            return mat


if __name__ == "__main__":
    s = Solution
    x = s.matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4)
    print(x)
