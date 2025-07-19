class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowel:
                left+=1
                continue
            if s[right] not in vowel:
                right-=1
                continue

            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return ''.join(s)
                

#Test 
s = "leetcode"
result = Solution().reverseVowels(s)
print(result)