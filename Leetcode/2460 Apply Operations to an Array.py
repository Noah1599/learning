#https://leetcode.com/problems/apply-operations-to-an-array/description/
#O(n) time and space
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        lists=[0]*(len(nums))
        count=0
    
        length=range(len(nums))
        for i in length:
            
            if i == len(nums)-1: 
                if nums[i]!=0:
                    lists[count]=nums[i]
                    count+=1
                    break
                else: break
            if nums[i]==nums[i+1] and nums[i]!=0:
                nums[i]=nums[i]*2
                nums[i+1]=0
                lists[count]=nums[i]
                count+=1
            elif nums[i]!=0:
                lists[count]=nums[i]
                count+=1
        return lists


sol=Solution().applyOperations
print(sol([1,2,2,1,1,0]))
print(sol([0,1]))
print(sol([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))