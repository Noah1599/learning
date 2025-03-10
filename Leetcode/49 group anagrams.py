
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)#makes it easy to append values
        #res={}
        for s in strs:
         
            count = [0] * 26#makes a array of 26 values
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)#makes a key for each letter frequencies if 2 words have the same frequency it will be added to same key
            
        return list(res.values())

    print(groupAnagrams(0,["act","pots","tops","cat","stop","hat"]))








#        if len(s) != len(t):
#            return False
#        
#        count = [0] * 26
#        
#        for i in range(len(s)):
#            count[ord(s[i]) - ord('a')] += 1 #when it sees the char add the ascii value to count
#            count[ord(t[i]) - ord('a')] -= 1#then removes ascII value
#
#        for val in count:
#            if val != 0: #if there is anagram then all numbers should be zero
#                return False
#        return True