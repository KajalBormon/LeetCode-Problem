class Queue: 
    def isQueue(self, nums):
        items = []
        
        # Enqueue
        for i in range(len(nums)):
            items.append(nums[i])
        return items
    
    
sol = Queue()
result = sol.isQueue([1,2,3,4,5])

# Dequeue
print(result.pop(2))

