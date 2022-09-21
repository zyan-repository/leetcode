# *coding:utf-8 *
# 示例1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        ans = 1
        for st in range(len(s)):
            dic = {}
            dic[s[st]] = 1
            cnt = 1
            while True:
                try:
                    if s[st + cnt] in dic:
                        ans = max(ans, cnt)
                        break
                    else:
                        dic[s[st + cnt]] = 1
                        cnt += 1
                except:
                    if st == len(s) - 1:
                        return ans
                    return max(ans, cnt)
        return ans


a = Solution()

ans = a.lengthOfLongestSubstring("abcb")
print(ans)
