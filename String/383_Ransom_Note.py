class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letter_count = {}
        for char in magazine:
            if char in letter_count:
                letter_count[char] +=1
            else:
                letter_count[char] = 1

        for char in ransomNote:
            if char not in letter_count or letter_count[char] == 0:
                return False
            else:
                letter_count[char] -=1
        return True


ransomNote = "a" 
magazine = "b"
result = Solution().canConstruct(ransomNote, magazine)
print(result)