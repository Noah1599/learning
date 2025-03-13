#https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])  

        position = {mat[r][c]: (r, c) for r in range(m) for c in range(n)}

        row_count = [0] * m
        col_count = [0] * n

        for index, num in enumerate(arr):
            r, c = position[num]  
            row_count[r] += 1
            col_count[c] += 1
            
            if row_count[r] == n or col_count[c] == m:
                return index  


arr = [1,3,4,2]
mat = [[1,4],[2,3]]
sol=Solution()
print(sol.firstCompleteIndex(arr,mat))