# *coding:utf-8 *
# 示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
        probe = self
        res = 0
        while probe is not None:
            res += 1
            probe = probe.next
        return res

    def add(self, other):
        probe = self
        while probe is not None:
            if probe.next is None:
                probe.next = ListNode(other)
                break
            probe = probe.next


class Solution(object):
    def get_num(self, lst):
        cnt = 0
        num = 0
        for i in lst:
            num += i * 10**cnt
            cnt += 1
        return num

    def add(self, ll, other):
        probe = ll
        while probe is not None:
            if probe.next is None:
                probe.next = ListNode(other)
                break
            probe = probe.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        probe1 = l1
        probe2 = l2
        lst1 = [probe1.val]
        while probe1.next is not None:
            lst1.append(probe1.next.val)
            probe1 = probe1.next
        lst2 = [probe2.val]
        while probe2.next is not None:
            lst2.append(probe2.next.val)
            probe2 = probe2.next
        num1 = self.get_num(lst1)
        num2 = self.get_num(lst2)
        num = num1 + num2
        lst = []
        while num:
            lst.append(num % 10)
            num = int(num / 10)
        if not lst:
            return ListNode(0)
        l = ListNode(lst[0])
        for i in range(1, len(lst)):
            self.add(l, lst[i])
        return l


a = Solution()

# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
# l1 = ListNode(9)
# for i in range(6):
#     l1.add(9)
# l2 = ListNode(9)
# for i in range(3):
#     l2.add(9)

# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# l1 = ListNode(2)
# l1.head = l1
# l1.add(4)
# l1.add(3)
# l2 = ListNode(5)
# l2.head = l2
# l2.add(6)
# l2.add(4)

l1 = ListNode(0)
l2 = ListNode(0)

# L1 = [9,9,9,9,9,9,9]
# L2 = [9,9,9,9]

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]

ans = a.addTwoNumbers(l1, l2)
print(ans)
