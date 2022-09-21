# 给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。

# 示例 1：
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2

# 示例 2：
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst = nums1 + nums2
        lst.sort()
        length = len(lst)
        if length % 2:
            return lst[int(length / 2)]
        else:
            return (lst[int(length / 2)] + lst[int(length / 2) - 1]) / 2


n1 = [1, 2]
n2 = [3, 4]
a = Solution()
ans = a.findMedianSortedArrays(n1, n2)
print(ans)
