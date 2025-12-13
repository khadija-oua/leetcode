# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        M={}
        if ! head : return False
        node = head.next
        pos=-1
        while node :
            if node.next in M:
                return True 
            else :
                M[node.next] = pos
            pos+=1
            node = node.next
        return False