#Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its bottom-up level order traversal as:
#[
#  [15,7],
#  [9,20],
#  [3]
#]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversal = []
        self.inorder(root, 0, traversal)
        return traversal[::-1]

    def inorder(self, node, depth, traversal):

        if not node:
            return

        if len(traversal) == depth:
            traversal.append([])

        self.inorder(node.left, depth+1, traversal)

        traversal[depth].append(node.val)

        self.inorder(node.right, depth+1, traversal)
        