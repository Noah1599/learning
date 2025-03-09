#firt iteration
# time o(n log n)
#class Solution(object):
#    def isAnagram(self, s, t):
#        """
#        :type s: str
#        :type t: str
#        :rtype: bool
#        """
#        s=list(s)
#        s.sort()  
#        t=list(t)
#        t.sort()
#        if s==t:
#            return True
#        else:
#            return False
#        
#    print(isAnagram(0,"anagram","nagaram"))
#    print(isAnagram(0,"rat","car"))


#i can do faster
#not my solution but takes 0(n) time
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=s.lower()
        t=t.lower()
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 #when it sees the char add the ascii value to count
            count[ord(t[i]) - ord('a')] -= 1#then removes ascII value

        for val in count:
            if val != 0: #if there is anagram then all numbers should be zero
                return False
        return True


        
    print(isAnagram(0,"Anagram","nagaram"))
    print(isAnagram(0,"rat","car"))
#https://www.shiksha.com/online-courses/articles/ord-and-chr-functions-in-python/