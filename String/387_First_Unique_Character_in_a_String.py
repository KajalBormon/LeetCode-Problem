class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char] = 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i           
        return -1


#Test
s = "loveleetcode"
sol = Solution()
result = sol.firstUniqChar(s)
print(result)
