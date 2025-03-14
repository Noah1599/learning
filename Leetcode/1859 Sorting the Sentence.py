#https://leetcode.com/problems/sorting-the-sentence/description/

class Solution(object):
    def sortSentence(self, s):
        s=s.split()
        
        constWord=[""]*len(s)

        for word in s:
            constWord[int(word[-1])-1]=word[:-1]
        return " ".join(constWord)
       




    print(sortSentence(0,"is2 sentence4 This1 a3"))