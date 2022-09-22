# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]
#
# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, n):
        probe = self
        while probe.next:
            probe = probe.next
        probe.next = ListNode(n)


class Solution:
    def add(self, ln, n):
        probe = ln
        while probe.next:
            probe = probe.next
        probe.next = ListNode(n)

    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        first = 1
        while True:
            if list1 and list2:
                if list1.val < list2.val:
                    if first:
                        res = ListNode(list1.val)
                        first = 0
                    else:
                        self.add(res, list1.val)
                    # res.add(list1.val)
                    list1 = list1.next
                else:
                    if first:
                        res = ListNode(list2.val)
                        first = 0
                    else:
                        self.add(res, list2.val)
                    # res.add(list2.val)
                    list2 = list2.next
            elif not list1 and list2:
                if first:
                    res = ListNode(list2.val)
                    first = 0
                else:
                    self.add(res, list2.val)
                # res.add(list2.val)
                list2 = list2.next
            elif list1 and not list2:
                if first:
                    res = ListNode(list1.val)
                    first = 0
                else:
                    self.add(res, list1.val)
                # res.add(list1.val)
                list1 = list1.next
            else:
                break
        return res


a = Solution()
l1 = ListNode(1)
l1.add(2)
l1.add(4)
l2 = ListNode(1)
l2.add(3)
l2.add(4)
l3 = ListNode()
l4 = ListNode(0)
# l1 = [1,2,4], l2 = [1,3,4]
ans = a.mergeTwoLists(l3, l4)
print(ans)
while True:
    print(ans.val)
    ans = ans.next
    if not ans:
        break
