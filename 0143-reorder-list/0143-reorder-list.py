# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow= head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        s=slow.next
        slow.next= None
        prev , curr = None ,s
        while curr:
            nxt= curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        l1= head
        l2 = prev  
        while l1 and l2 :
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1=temp1
            l2=temp2