#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        count=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count]=nums[i]
                count+=1
        return count

        
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))