#https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/

class Solution(object):
    def areNumbersAscending(self, s):
        s=s.split()
        number=0
        for i in s:
            if i.isdigit():
                if int(i)<=number: return False
                number=int(i)
        return True

        


    print(areNumbersAscending(0,"1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
    print(areNumbersAscending(0,"hello world 5 x 5"))    