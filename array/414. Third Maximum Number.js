var thirdMax = function(nums) {
    const unique = [...new Set(nums)];
    unique.sort((a, b) => b-a);

    if(unique.length >= 3){
        return unique[2];
    }
    return unique[0];
};

const result = thirdMax([-2147483648,1,2]);
console.log(result);