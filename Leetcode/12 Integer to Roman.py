#https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):

        romanDict = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        

        st=""
        for value in sorted(romanDict.keys(), reverse=True):
            while num >= value:
                st += romanDict[value]
                num -= value
        
        return st
            
            
                    

print(Solution().intToRoman(3749))
print(Solution().intToRoman(58))