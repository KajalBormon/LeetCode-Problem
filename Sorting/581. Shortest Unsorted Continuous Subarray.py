class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        start = len(nums)
        end = 0

        for i in range(start):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end - start >= 0 else 0        
        
        


sol = Solution()
result = sol.findUnsortedSubarray([2,6,4,8,10,9,15])
print(result)