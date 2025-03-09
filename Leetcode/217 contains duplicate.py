class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i=0
        j=0
        while i <=len(nums)-1:
            j+=1
            print(str(j)+" "+str(i))
            while j <=len(nums)-1:
                if nums[i] == nums[j]:
                    return True
                    break
                j+=1
            i+=1
        else:
            return False

    print(containsDuplicate(0,[1,2,3,4,4]))
    print(containsDuplicate(0,[2,14,18,22,22]))