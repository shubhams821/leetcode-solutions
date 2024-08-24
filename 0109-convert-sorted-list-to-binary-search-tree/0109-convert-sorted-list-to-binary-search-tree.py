# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        def helper(l,r):
            if l>r:
                return None
            m = (l+r)//2
            root = TreeNode(arr[m])
            root.right = helper(m+1,r)
            root.left = helper(l,m-1)
            return root
        return helper(0, len(arr)-1)