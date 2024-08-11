# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        slow = head
        while slow:
            tmp = slow.next 
            slow.next = prev
            prev = slow
            slow = tmp
            print(prev.val)
        return prev      