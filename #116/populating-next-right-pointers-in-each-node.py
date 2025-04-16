# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        curr, nxt = root, root.left if root else None

        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
            
        return root