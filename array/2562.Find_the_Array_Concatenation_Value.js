var findTheArrayConcVal = function(nums) {
    let total = 0;
    
    while (nums.length > 1) {
        let concat = nums[0].toString() + nums[nums.length - 1].toString();
        total += parseInt(concat);
        nums = nums.slice(1, -1); // remove first and last
    }
    
    if (nums.length === 1) {
        total += nums[0];
    }

    return total;
};

$result = findTheArrayConcVal([7,52,2,4]);
console.log($result);