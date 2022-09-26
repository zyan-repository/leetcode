# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
# 示例 1:
# 输入:[1,2,3,null,5,null,4]
# 输出:[1,3,4]
#
# 示例 2:
# 输入:[1,null,3]
# 输出:[1,3]
#
# 示例 3:
# 输入:[]
# 输出:[]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        import queue
        q = queue.Queue()
        q.put(root)
        ans = [root.val]
        while True:
            lst = []
            while not q.empty():
                lst.append(q.get())
            if not len(lst):
                break
            ap = None
            for node in lst:
                if node.left is not None:
                    ap = node.left.val
                    q.put(node.left)
                if node.right is not None:
                    ap = node.right.val
                    q.put(node.right)
            if ap is not None:
                ans.append(ap)
        return ans


a = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(None)
root.left.right = TreeNode(5)
root.right.left = TreeNode(None)
root.right.right = TreeNode(4)
ans = a.rightSideView(root)
print(ans)
