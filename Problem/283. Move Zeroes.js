var moveZeroes = function(nums) {
    let lastNonZeroFountAt = 0; 
    for(let i = 0; i < nums.length; i++){
        if(nums[i] !== 0){
            if(i !== lastNonZeroFountAt){
                let temp = nums[i];
                nums[i] = nums[lastNonZeroFountAt];
                nums[lastNonZeroFountAt] = temp;
            }
            lastNonZeroFountAt++;
        }
    }
    return nums;
};

const result = moveZeroes([0,1,0,3,12]);
console.log(result);