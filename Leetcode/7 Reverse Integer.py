#https://leetcode.com/problems/reverse-integer/description/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN_32BIT = -2147483648
        MAX_32BIT = 2147483647
        num=0
        val=str(x)[::-1]
        if x<0: num=int(val[:len(val)-1])*-1
        else: num=int(val)
        if num>MAX_32BIT or num<MIN_32BIT: return 0
        return num
        
    print(reverse(0,-234534))
    print(reverse(0,120))