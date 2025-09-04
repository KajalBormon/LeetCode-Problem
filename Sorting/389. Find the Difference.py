class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for ch in t:
            if s.count(ch) != t.count(ch):
                return ch


s = "a"
t = "aa"
sol = Solution()
result = sol.findTheDifference(s, t)
print(result)