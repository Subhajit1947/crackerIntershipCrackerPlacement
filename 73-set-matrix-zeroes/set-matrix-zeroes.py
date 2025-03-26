import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr=copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for k in range(len(matrix[0])):
                        arr[i][k]=0
                    for k in range(len(matrix)):
                        arr[k][j]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=arr[i][j]   
        