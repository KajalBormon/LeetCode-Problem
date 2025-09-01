var singleNumber = function(nums) {
    let result = 0; 
    for(let i = 0; i < nums.length; i++){
        result ^=nums[i];
    }
    return result;
};

const result = singleNumber([2,5,3,2,3,5,6]);
console.log(result);