#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#class Solution(object):
#    def lengthOfLongestSubstring(self, s):
#
#        if len(s)==0:return 0
#
#        strings=[""]*len(s)
#        longest=0
#
#        for i in range(len(s)):
#            #i decides where it starts
#            for j in range(len(s)-i):
#                if   s[i+j] not in strings[i]:
#                    strings[i]+=s[i+j]
#                else:break
#            strings[i]=len(strings[i])
#            if strings[i]>longest:longest=strings[i]
#        
#        return longest

class Solution(object):
    def lengthOfLongestSubstring(self, s):      

        char_set = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            print(char_set)
            longest = max(longest, right - left + 1)

        return longest
        
        


print(Solution().lengthOfLongestSubstring("anviaj"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring("dvdf"))