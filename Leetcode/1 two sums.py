
#this takes O(n^2)
#class Solution(object):
#    def twoSum(self,nums,target):
#        n = len(nums)
#        for i in range(n - 1):
#            for j in range(i + 1, n):
#                if nums[i] + nums[j] == target:
#                    return [i, j]
#        return []
#
#    print(twoSum(0,[2,7,11,15],9)) 
# 
# making faster now

class Solution(object):
    def twoSum(self,nums,target):   
        hashmap={} #val : index

        for i, n in enumerate(nums): #using enumerate i get index and value n
            diff=target-n
            if diff in hashmap:
                return [hashmap[diff],i]
            print(n)
            hashmap[n]=i
        return
    print(twoSum(0,[2,7,11,15],9)) 