# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root is not None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ans.append(root.val)
        return self.ans


a = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
ans = a.postorderTraversal(root)
print(ans)
