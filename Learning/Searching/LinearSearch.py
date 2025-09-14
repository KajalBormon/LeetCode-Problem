class Solution(object):
    def isLinearSearch(self, nums, search):

        for i in range(len(nums)):
            if(nums[i] == search):
                return i
        return -1


nums = [2,4,5,10,15,20]
search = 10

sol = Solution()
result = sol.isLinearSearch(nums, search)
print(result)