#https://leetcode.com/problems/valid-number/description/

class Solution(object):
    def isNumber(self, s): 
        try:
            float(s)
            return not s.lower() in {"inf", "+inf", "-inf", "infinity", "+infinity", "-infinity","nan","+nan","-nan"}
        except ValueError: return False



sol=Solution()

print(sol.isNumber("2"))               # True
print(sol.isNumber("-0.1"))            # True
print(sol.isNumber("+3.14"))           # True
print(sol.isNumber("-90E3"))           # True
print(sol.isNumber("53.5e93"))         # True
print(sol.isNumber("3e+7"))            # True
print(sol.isNumber("-123.456e789"))    # True
print(sol.isNumber("abc"))             # False
print(sol.isNumber("+inf"))             # False
print(sol.isNumber("inf"))             # False
print(sol.isNumber("infinity"))             # False
print(sol.isNumber("1a"))             # False