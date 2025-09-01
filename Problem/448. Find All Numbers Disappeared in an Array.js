var findDisappearedNumbers = function(nums) {
    var result = [];
    const numSet = new Set(nums);
    for(i = 1; i <= nums.length; i++) {
        if(!numSet.has(i)) {
            result.push(i);
        }
    }
    return result; 
};

$result = findDisappearedNumbers([1,1]);
console.log($result);