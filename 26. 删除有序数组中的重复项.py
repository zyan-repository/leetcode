# *coding:utf-8 *
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
# 示例 2：
#
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        front = 0
        rear = 1
        dic = {}
        while True:
            if len(nums) == 1:
                return 1
            while True:
                if nums[front] != nums[rear]:
                    front += 1
                    nums[front] = nums[rear]
                    if nums[rear] not in dic:
                        ans += 1
                        dic[nums[rear]] = 1
                    break
                if rear == len(nums) - 1:
                    break
                rear += 1
            if rear == len(nums) - 1:
                break
        return ans


a = Solution()
print(a.removeDuplicates([1, 2, 3, 3, 5, 5]))
print(a.removeDuplicates([1, 1, 2]))
print(a.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(a.removeDuplicates([1]))
print(a.removeDuplicates([1, 1]))
