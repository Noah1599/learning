class Solution(object):
    def isValid(self, s):
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(pairs[char])  # Push expected closing
            elif not stack or char != stack.pop():
                return False
        return not stack

sol=Solution()

i="()" #true
print(sol.isValid(i))
i="([{}])"#true
print(sol.isValid(i))
i="[{]"#false
print(sol.isValid(i))
i="[(])"#false
print(sol.isValid(i))