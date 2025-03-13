#https://leetcode.com/problems/palindrome-number/solutions/6325628/easyyyyy-code-clear-simple-explanation-beats-c-java-py3-js/

#this not mine but so clever

#class Solution:
#    def isPalindrome(self, x: int) -> bool:
#        if x<0:
#            return False
#        else:
#            x = str(x)
#            if x == x[::-1]:
#                return True
#            else:
#                return False
#

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        string=str(x)
        if string==string[::-1]:return True
        else: return False



#class Solution(object):
#    def isPalindrome(self, x):
#        """
#        :type x: int
#        :rtype: bool
#        """
#        if x<0: return False        
#        lis=str(x)
#
#
#        revString=[0]*len(lis)
#        indi=0
#        for i in range(len(lis)):
#            revString[len(lis)-1-indi]=lis[i]
#            indi+=1
#        string="".join(revString)
#
#        if lis==string: return True
#        else: return False



sol=Solution()

input=12132

print(sol.isPalindrome(input))