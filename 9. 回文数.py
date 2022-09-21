# *coding:utf-8 *
# 示例 1：
#
# 输入：x = 121
# 输出：true
# 示例 2：
#
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3：
#
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        front = 0
        rear = len(x) - 1
        flag = 1
        while front < rear:
            if x[front] != x[rear]:
                flag = 0
                break
            front += 1
            rear -= 1
        if flag:
            return True
        return False
