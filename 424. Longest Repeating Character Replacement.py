# Time Complexity :  O(n)
# Space Complexity : O(1)
class Solution(object):
    def characterReplacement(self, s, k):
        maxlen,largestcount = 0,0
        arr = collections.Counter()
        for idx in range(len(s)):
            arr[s[idx]] +=1
            largestcount = max(largestcount, arr[s[idx]])
            if maxlen - largestcount >= k:
                arr[s[idx - maxlen]] -=1
            else:
                maxlen += 1
        return maxlen
 