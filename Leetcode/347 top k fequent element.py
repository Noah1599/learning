#class Solution(object):
#    def topKFrequent(self, nums, k):
#        """
#        :type nums: List[int]
#        :type k: int
#        :rtype: List[int]
#        """
#        count = {}#this is a dictionary and will store fequency
#        freq = [[] for i in range(len(nums) + 1)]
#        
#        for num in nums:
#            count[num] = 1 + count.get(num, 0)
#            
#        for num, cnt in count.items():
#            freq[cnt].append(num)
#        
#        res = []
#        for i in range(len(freq) - 1, 0, -1):
#            for num in freq[i]:
#                res.append(num)
#                if len(res) == k:
#                    return res
#        
    
#class Solution(object):
#    def topKFrequent(self, nums, k):
#        """
#        :type nums: List[int]
#        :type k: int
#        :rtype: List[int]
#        """
#        count = {}#this is a dictionary and will store fequency
#        freq = [[] for i in range(len(nums) + 1)]
#        
#        big = [[0]*2]*2
#        print(big)
#        for num in nums:
#            count[num] = 1 + count.get(num, 0)
#        
#        for i in count:
#            print(count)
#            if count[i]>= big[[0][0]]:
#                big[[1][1]]=big[[0][0]]
#                big[[0][0]]=count[i]
#            print(big)    
#
#    print(topKFrequent(0,[1,1,1,2,2,2,2,3,7],2))

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}#Counter(nums)  # Dictionary storing frequency

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]  # Bucket sort array
        for num, freq_count in count.items():#num = key freq count = value
            freq[freq_count].append(num)  # Group numbers by frequency
            

        result = []
        for i in range(len(freq) - 1, 0, -1):  # Traverse from highest frequency
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

# Example usage

    print(topKFrequent(0,[1,1,1,2,2,2,2,3,7], 2))  
