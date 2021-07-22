# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        tmp = []
        node = head
        while node:
            tmp.append(node.val)
            node = node.next
        
        tmp.sort()
        
        node = head
        for i in tmp:
            node.val = i
            node = node.next
        
        return head
