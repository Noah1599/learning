##https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/
#
#class Solution(object):
#    def checkXMatrix(self, mat):
#        """
#        :type grid: List[List[int]]
#        :rtype: bool
#        """      
#        center=None
#        if len(mat)%2==1:
#            center=int(len(mat)/2)            
#        #now we calculate the diagonal
#        i=0
#        for rows in mat:
#            sum=0
#            if i==center:
#                if rows[i]==0: return False
#                for j in rows:
#                    sum+=j
#                if sum-rows[i]!=0:return False
#            else:
#                if rows[i]==0 or rows[-i-1]==0: return False
#                for k in rows:
#                    sum+=k
#                if sum-rows[i]-rows[-i-1]!=0:
#                    return False
#            i+=1          
#        return True
#    
#    print(checkXMatrix(0,[[5,0,0,1],[0,4,1,5],[0,5,2,0],[4,1,0,2]]))
#    print(checkXMatrix(0,[2, 0, 0, 1]))


class Solution(object):
    def checkXMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: bool
        """      
        n = len(mat)

        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:  # Check diagonal elements
                    if mat[i][j] == 0:  
                        return False
                else:  # Check non-diagonal elements
                    if mat[i][j] != 0:  
                        return False
                        
        return True

# Example Usage:
sol = Solution()
print(sol.checkXMatrix([[5, 0, 0, 1], [0, 4, 1, 5], [0, 5, 2, 0], [4, 1, 0, 2]]))
