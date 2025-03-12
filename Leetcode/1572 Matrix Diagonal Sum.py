#time O(n)
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        center=None
        sum=0
        if len(mat)%2==1:
            center=int(len(mat)/2)
            
        #now we calculate the diagonal
        i=0
        for rows in mat:
            if i==center:
                sum+=rows[i]
            else:
                sum+=rows[i]+rows[-i-1]
            i+=1
        return sum

 

    mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    mat2 = [[1,2,3],[4,5,6],[7,8,9]]
    print(diagonalSum(0,mat))
    print(diagonalSum(0,mat2))