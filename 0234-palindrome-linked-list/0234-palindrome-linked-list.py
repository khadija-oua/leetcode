# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        Q=[]
        curr = head 
        if head.next is None : return True
        l = 0
        while curr : 
            l+=1
            curr = curr.next
        mid = l//2
        curr = head 
        while curr :
            if mid > 0 : 
                Q.append(curr.val)
            elif Q[-1] == curr.val :
                Q.pop()
            curr = curr.next
            mid -=1
        return len(Q) == 0 