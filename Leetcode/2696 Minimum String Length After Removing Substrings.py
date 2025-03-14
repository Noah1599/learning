#https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/

class Solution(object):
    def minLength(self, s):
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "").replace("CD", "")
        return len(s)
            


s = "ABFCACDB"
sol=Solution()
print(sol.minLength(s))