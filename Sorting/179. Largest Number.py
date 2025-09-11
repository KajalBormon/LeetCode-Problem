class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        str_nums = [str(x) for x in nums]
    
        n = len(str_nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if str_nums[j] + str_nums[j+1] < str_nums[j+1] + str_nums[j]:
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]

        string = ''.join(str_nums)
        return "0" if string[0] == "0" else string

nums = [0,0]
sol = Solution()
result = sol.largestNumber(nums)
print(result)

        