#https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        #to calculate lateral rows for duplicates
        for rows in matrix:
            count ={}
            for i in rows:
                if i in count:
                    return False
                if i !=".":
                    count[i]=1
                    
        #now we calculate vertical rows for duplicates
        for i in range(len(matrix)):
            count={}
            for j in range(len(matrix)):        
                if matrix[j][i]!=".":
                    if matrix[j][i] in count:
                        return False
                    count[matrix[j][i]]=1
        return True


    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    print(checkValid(0,matrix))