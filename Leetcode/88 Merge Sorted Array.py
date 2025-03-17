#https://leetcode.com/problems/merge-sorted-array/description/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 : return nums2
        if not nums2 : return nums1

        temp=[]
        while nums1[0]>0 and nums2[0]>0:
            if nums1[0]>=nums2[0]:
                temp+=nums1[0]
                nums1.pop(0)
            else:
                temp+=nums2[0]
                nums2.pop(0)
        print(temp)


    
        
nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
print(Solution().merge(nums1,m,nums2,n))

nums1, m, nums2, n = [], 0, [2], 1
print(Solution().merge(nums1,m,nums2,n))