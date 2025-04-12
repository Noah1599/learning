class Solution(object):
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        copy=[0]*length
        leftinc=0
        rightinc=0
        for i in range(len(nums)):
            if nums[i]!=0:
                copy[leftinc]=nums[i]
                leftinc+=1
            else:
                copy[length-1-rightinc]=nums[i]
                rightinc+=1
        nums=copy



    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        zerospaces=0

        for i in range(len(nums)):
            print(nums)
            if nums[i] == 0:
                zerospaces += 1
            elif zerospaces > 0:        
                nums[i - zerospaces]= nums[i] 
                nums[i]= 0
            

nums = [0,1,0,3,12,0]
print(Solution().moveZeroes(nums))