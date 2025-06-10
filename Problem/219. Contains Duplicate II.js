var containsNearbyDuplicate = function(nums, k) {
    const indexMap = new Map();

    for(let i = 0; i < nums.length; i++){
        if(indexMap.has(nums[i])){
            const prevIndex = indexMap.get(nums[i]);
            console.log(prevIndex);
            if(i - prevIndex <= k){
                return true;
            }
        }
        indexMap.set(nums[i], i);
    }
    return false; 
};

const result = containsNearbyDuplicate([1,2,3,1,2,3], 2);
console.log(result);