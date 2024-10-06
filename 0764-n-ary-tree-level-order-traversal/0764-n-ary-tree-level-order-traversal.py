"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque([root])
        res = []
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    for child in node.children:
                        q.append(child)
                    temp.append(node.val)
            if temp:
                res.append(temp)
        return res