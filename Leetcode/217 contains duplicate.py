# this takes O(n^2) time
##first iteration works but not good at verry large inputs
#class Solution(object):
#    def containsDuplicate(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: bool
#        """
#        i=0
#        j=0
#        iteration=0
#        while i <=len(nums)-1:
#            iteration+=1
#            j=iteration
#            while j <=len(nums)-1:
#                if nums[i] == nums[j]:
#                    return True
#                    break
#                j+=1 
#            i+=1
#        else:
#            return False
#


#solutiuon 2 this takes O(n log n)
#class Solution(object):
#    def containsDuplicate(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: bool
#        """
#        nums.sort(reverse=False)
#        i=0
#        j=0
#        iteration=0
#        while i <=len(nums)-1:
#            iteration+=1
#            j=iteration
#            while j <=len(nums)-1:
#                if nums[i] == nums[j]:
#                    return True
#                    break
#                j+=1 
#            i+=1
#        else:
#            return False
#
#    print(containsDuplicate(0,[1,2,3,4,1]))
#    print(containsDuplicate(0,[2,14,18,22,22]))
#    print(containsDuplicate(0,[2,14,13,22,32]))
#    print(containsDuplicate(0,[2,14,14,22,5]))

#best solution i can get 
#time o(n) remove sort because sort takes o(n log n) time
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        else:
            return False

    print(containsDuplicate(0,[1,2,3,4,1]))
    print(containsDuplicate(0,[2,14,18,22,22]))
    print(containsDuplicate(0,[2,14,13,22,32]))
    print(containsDuplicate(0,[2,14,14,22,5]))