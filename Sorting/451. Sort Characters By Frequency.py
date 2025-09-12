class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for char in s: 
            freq[char] = freq.get(char, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return ''.join(char * count for char, count in sorted_freq)

sol = Solution()
result = sol.frequencySort("tree")
print(result)