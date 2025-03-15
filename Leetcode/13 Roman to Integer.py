#https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
    def romanToInt(self, s):
        
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total=0
        prev=0
        for roman in reversed(s):
            val=romanDict[roman]

            if val<prev:
                total-=val
            else:
                total+=val
            prev=val
        return total
            
        

print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))