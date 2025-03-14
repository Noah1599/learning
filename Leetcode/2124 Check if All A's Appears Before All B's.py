#https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
class Solution(object):
    def checkString(self, s):
        st=""
        for i in s:
            if i =='a' and 'b' in st:
                return False
            st+=i
        return True

    print(checkString(0,"aabba"))
    print(checkString(0,"aabb"))