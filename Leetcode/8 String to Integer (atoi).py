class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  return 0
        
        s = s.lstrip()
        oF = ""
        nums = ""

        if s and s[0] in "-+":
            oF = s[0]
            s = s[1:]

        s = s.lstrip("0")

        for char in s:
            if char.isdigit(): nums += char
            else: break

        if not nums: return 0
        num = int(oF + nums)

        if num < -2147483648: num = -2147483648
        elif num > 2147483647: num = 2147483647

        return num
   
    print(myAtoi(0,'   -123'))#returns -123
    print(myAtoi(0,'   +123hello'))#returns +123
    print(myAtoi(0,'welcome-123'))#return 0
    print(myAtoi(0,'0000002welcome-123'))#returns 2
    print(myAtoi(0,"-91283472332"))#returns 2    
    print(myAtoi(0,"+-12"))#returns 0            
    print(myAtoi(0,"-+12"))#returns 0     
    print(myAtoi(0,"0-1"))#returns 0
    print(myAtoi(0,""))#returns 0    
    print(myAtoi(0,"1"))#returns 0   
    print(myAtoi(0,"00000-42a12"))#returns 0     