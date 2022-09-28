# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root is not None:
            self.ans.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.ans


a = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
ans = a.preorderTraversal(root)
print(ans)