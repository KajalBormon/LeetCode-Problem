class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        if len(sort_nums) < 2:
            return 0

        new_arr = []
        for i in range(len(sort_nums)-1):
            new_arr.append(sort_nums[i+1] - sort_nums[i])

        return max(new_arr)   


nums = [3,6,9,1]
sol = Solution()
result = sol.maximumGap(nums)
print(result)