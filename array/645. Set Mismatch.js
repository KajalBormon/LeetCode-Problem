var findErrorNums = function(nums) {
    const n = nums.length;
    nums.sort((a,b) => a - b);
    let duplicate, missing;
    let sum = 0; 
    let expectedSum = (n*(n+1)/2);
    for(let i = 0; i < n; i++){
        sum+=nums[i];
        if(nums[i] === nums[i+1]){
            duplicate = nums[i];
        }
    }
    missing = expectedSum - (sum - duplicate);
    return [duplicate, missing];
};

const nums = [1,2,3,4,4];
const result = findErrorNums(nums);
console.log(result);