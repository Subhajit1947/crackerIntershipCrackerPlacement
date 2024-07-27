class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        marr=[]
        for i in range(len(matrix)):
            arr=[]
            for j in range(len(matrix[0])-1,-1,-1):
                arr.append(matrix[j][i])
            marr.append(arr)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if marr[i][j]!=matrix[i][j]:
                    matrix[i][j]=marr[i][j]
        