# *coding:utf-8 *
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target % 2 == 0:
            res = int(target / 2)
            rtype = []
            for idx, i in enumerate(nums):
                if i == res:
                    rtype.append(idx)
            if len(rtype) == 2:
                return rtype
        lst = []
        dic = {}
        for idx, i in enumerate(nums):
            lst.append(target - i)
            dic[i] = idx
        for idx, i in enumerate(lst):
            if i in dic and idx != dic[i]:
                rtype = [idx, dic[i]]
                break
        return rtype


a = Solution()
print(a.twoSum([-1, -2, -3, -4, -5], -8))
print(a.twoSum([3, 2, 4], 6))
