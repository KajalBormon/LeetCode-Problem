class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        longest = 0
        for x in freq: 
            if x + 1 in freq:
                longest = max(longest, freq[x] + freq[x+1])
                
        return longest
            

sol = Solution()
result = sol.findLHS([1,3,2,2,5,2,3,7])
print(result)
