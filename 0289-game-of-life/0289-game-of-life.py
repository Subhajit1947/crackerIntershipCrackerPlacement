class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neighbour(r,c):
            nei=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if ((i==r and j==c) or i<0 or j<0 or 
                        i==len(board) or j==len(board[0])):
                        continue
                    if board[i][j]==1:
                        nei+=1
            return nei
        arr=copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                n=neighbour(i,j)
                if board[i][j]==1:
                    if n<2 or n>3:
                        arr[i][j]=0
                elif board[i][j]==0:
                    if n==3:
                        arr[i][j]=1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=arr[i][j]