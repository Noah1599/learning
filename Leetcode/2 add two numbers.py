#medium

#class Solution(object):
#    def addTwoNumbers(self, l1, l2):
#        for n in range(len(l1)):
#            
#            if l1[n]+l2[n]<10:
#                l1[n]+=l2[n]
#            else:
#                l1[n]+=l2[n]
#                l1[n+1]+=1
#                l1[n]-=10
#        return l1
 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0 #is overflow
        head = ListNode(0)  # Dummy node
        current = head  

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)#here it atatches the the overflow to the next node
            carry //= 10#here it removes the overflow from the current node
            current = current.next

        return head.next  # Return the actual result (skip dummy node)
    