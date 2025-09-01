var findMaxAverage = function(nums, k) {
    var windowSum = 0;

    for(i = 0; i < k; i++){
        windowSum +=nums[i];
    }
    
    let maxSum = windowSum;

    for(i = k; i < nums.length; i++){
        windowSum = windowSum - nums[i - k] + nums[i];
        maxSum = Math.max(maxSum, windowSum);
    }

    let result = maxSum / k;
    return result; 
};

const nums = [1,12,-5,-6,50,3], k = 4;
const result = findMaxAverage(nums, k);
console.log(result);