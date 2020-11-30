import numpy as np
from numpy import array, insert
from prettytable import PrettyTable
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

class matrix_basics():
    def __init__(self, _matrix):
        self.rows, self.columns = _matrix.shape
        self.matrix = _matrix
        self.create_table()
    def create_table(self):
        self.table = PrettyTable()
        names = [str(i) for i in range(self.columns + 1)]
        names[0] = "indices"
        self.table.field_names = names
        for i in range(self.rows):
            row = self.matrix[i].copy()
            row = insert(row, 0, i + 1)
            self.table.add_row(row)
    def same_size(self, B):
        return B.rows == self.rows and B.columns == self.columns
    def __eq__(self, B):
        if not self.same_size(B):
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != B.matrix[i][j]:
                    return False
        return True
    def __add__(self, B):
        if not self.same_size(B):
            print("You cant add those two matrices")
            return 0
        self.new_matrix = self.matrix
        for i in range(self.rows):
            for j in range(self.columns):
                self.new_matrix[i][j] += B.matrix[i][j]
        return matrix_basics(self.new_matrix)
    def __sub__(self, B):
        if not self.same_size(B):
            print("You cant add those two matrices")
            return 0
        self.new_matrix = self.matrix
        for i in range(self.rows):
            for j in range(self.columns):
                self.new_matrix[i][j] -= B.matrix[i][j]
        return matrix_basics(self.new_matrix)
    def __mul__(self, B):
        if self.columns != B.rows:
            print("You can't multiply those matrices")
            return 0
        self.new_matrix = np.array([[0.0 for x in range(B.columns)] for l in range(self.rows)])
        for i in range(self.rows):
            for j in range(B.columns):
                cell = 0
                for l in range(B.rows):
                    cell += self.matrix[i][l] * B.matrix[l][j]
                self.new_matrix[i][j] = cell
        return matrix_basics(self.new_matrix)
    def transpose(self):
        self.new_matrix = np.array([[0.0 for x in range(self.rows)] for l in range(self.columns)])
        for i in range(self.columns):
            for j in range(self.rows):
                self.new_matrix[i][j] = self.matrix[j][i]
        self.matrix = self.new_matrix
        self.rows, self.columns = self.columns, self.rows
        self.create_table()
    def __str__(self):
        return str(self.table)
    def getMatrix(self):
        return self.matrix
    def is_symmetric(self):
        self.save = self.matrix.copy()
        self.transpose()
        self.save_2 = self.matrix.copy()
        self.transpose()
        return self.save == self.save_2
    def determinate(self, matrix):
        rows, cols = matrix.shape
        if rows != cols or rows < 2 or cols < 2:
            print("You can't find a determinate for a non square matrix")
            return 0
        if rows == 2 and cols == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        ret = 0
        for i in range(cols):
            sub_matrix = np.array([[0 for i in range(cols - 1)] for j in range(rows - 1)])
            index_col = 0
            index_row = 0
            curr = matrix[0][i]
            for l in range(1, rows):
                for j in range(cols):
                    if j == i:
                        continue
                    sub_matrix[index_row][index_col] = matrix[l][j]
                    index_col = (index_col + 1) % (cols - 1)
                    index_row += 1 if index_col == 0 else 0
            ret = ret + curr * self.determinate(sub_matrix) if i % 2 == 0 else ret - curr * self.determinate(sub_matrix)
        return ret
    def inverse(self):
        if self.rows != 2 or self.columns != 2:
            print("I did not implement matrices other than 2 * 2")
            return 0
        curr = self.matrix.copy()
        curr[0][0], curr[1][1] = curr[1][1], curr[0][0]
        curr[0][1] *= -1
        curr[1][0] *= -1
        det = self.determinate(self.getMatrix())
        for i in range(2):
            for j in range(2):
                curr[i][j] /= det
        return matrix_basics(np.array(curr))

arr = [[2.0, 2.0],[0.0, -1.0]]
matrix = matrix_basics(np.array(arr))
matrix_inv = matrix.inverse()
print(matrix)
print(matrix_inv)
mat = matrix * matrix_inv
print(mat)


