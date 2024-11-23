class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        substring = set()
        left = 0
        maxlength = 0

        for right in range(n):
            if s[right] not in substring:
                substring.add(s[right])
                maxlength = max(maxlength, right - left + 1)
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left = left + 1
                substring.add(s[right])
        return maxlength
                    
