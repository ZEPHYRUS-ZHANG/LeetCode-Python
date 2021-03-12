# 滑动窗口(左右两个指针同时滑动)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        right = 0
        res = 0
        for left in range(len(s)):
            if left != 0:
                hashmap.remove(s[left-1])
            while right < len(s) and s[right] not in hashmap:
                hashmap.add(s[right])
                right += 1
            res = max(res, right-left)
        return res