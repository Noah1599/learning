#https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        current=dummy

        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next

        #now attatch rest if 1 line is linger than other
        current.next= list1 if list1 else list2

        return dummy.next
    
list1 = ListNode(1, ListNode(2, ListNode(4)))  # Creating list1: 1 -> 2 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))  # Creating list2: 1 -> 3 -> 4

merged_list = Solution().mergeTwoLists(list1, list2)

#stuopid node list 
while merged_list:
    print(merged_list.val, end=" -> " if merged_list.next else "\n")
    merged_list = merged_list.next
