# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。

# 示例 1:
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2

# 示例2:
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1

# 示例 3:
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if nums[mid] >= target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if nums[mid] < target:
            return mid + 1
        if nums[mid] >= target:
            return mid


a = Solution()
ans = a.searchInsert([1,3], 0)
print(ans)
