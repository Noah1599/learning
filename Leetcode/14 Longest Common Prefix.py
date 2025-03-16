#https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]  # Start with the first word as the prefix

        for word in strs[1:]:  # Compare with all other words
            while not word.startswith(prefix):  # Reduce prefix until match is found
                prefix = prefix[:-1]
                print(prefix)
                if not prefix:
                    return ""

        return prefix
             
             
 
    print(longestCommonPrefix(0,["ab", "a"]))
    print(longestCommonPrefix(0,["dog","racecar","car"]))
    print(longestCommonPrefix(0,["flower","flower","floiut","flower","flower"]))    