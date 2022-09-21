# *coding:utf-8 *
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = strs[0]
        # 遍历所有词
        for i in strs:
            for idx, k in enumerate(res):
                try:
                    if k != i[idx]:
                        if idx == 0:
                            return ""
                        res = res[:idx]
                        break
                except:
                    res = res[:idx]
                    break
        return res
