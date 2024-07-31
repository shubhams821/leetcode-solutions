# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        rightSide = None
        res = []
        while q:
            qLen= len(q)
            rightSide = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.right)
                    q.append(node.left)
            if rightSide:
                res.append(rightSide.val)
        return res[-1]