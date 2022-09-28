# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
# 示例 2：
# 输入：root = []
# 输出：[]
#
# 示例 3：
# 输入：root = [1]
# 输出：[1]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root is not None:
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
        return self.ans


a = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
ans = a.inorderTraversal(root)
print(ans)
