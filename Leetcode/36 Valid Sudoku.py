#https://leetcode.com/problems/valid-sudoku/description/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #to calculate lateral rows for duplicates
        for rows in board:
            count ={}
            for i in rows:
                if i in count:
                    return False
                if i !=".":
                    count[i]=1
                    
        #now we calculate vertical rows for duplicates
        for i in range(9):
            count={}
            for j in range(9):        
                if board[j][i]!=".":
                    if board[j][i] in count:
                        return False
                    count[board[j][i]]=1
                
        #now for the 3X3 boxes
        for boxRow in range(3):
            for boxVer in range(3):
                count={}
                for row in range(boxRow*3,boxRow*3+3):#steep into small boxes
                    for ver in range(boxVer*3,boxVer*3+3):
                        if board[row][ver] != ".":
                            if board[row][ver] in count:
                                return False
                            count[board[row][ver]] = 1 
        return True                       




        
                

                
            
                
        
    
    board1=[["5","3",".",".","7",".",".",".","."],["6","3",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    board2=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    print(isValidSudoku(0,board1))
    print(isValidSudoku(0,board2))