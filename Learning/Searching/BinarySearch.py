class Solution(object):
    def isBinarySearch(self, nums, search):
        low = 0
        high = len(nums)

        while(low <= high):
            mid = int((low + high) / 2)
            if(nums[mid] == search):
                return mid
            if(nums[mid] < search):
                low = mid + 1
            else: 
                high = mid -1
        return -1        


nums = [1,2,3,4,5,6,7,8,9,10]
search = 5
sol = Solution()
result = sol.isBinarySearch(nums, search)
print(result)