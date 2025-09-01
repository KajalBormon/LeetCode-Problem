class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s1 = s.lower()
        t1 = t.lower()

        if sorted(s1) == sorted(t1):
            return True
        else: 
            return False

s = "hello"
t = "HeoLL"
result = Solution().isAnagram(s, t)
print(result)