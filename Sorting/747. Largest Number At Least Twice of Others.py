class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        for i in nums:
            if i != maximum and i * 2 > maximum:
                return -1
        return nums.index(maximum)


nums = [1,2,3,4]
sol = Solution()
result = sol.dominantIndex(nums)
print(result)