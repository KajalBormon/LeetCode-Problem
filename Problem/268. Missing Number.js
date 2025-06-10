var missingNumber = function(nums) {
    const size = nums.length;
    let sortArr = nums.sort((a,b) => a-b);
    for(let i = 0; i <= size; i++){
        if(i !== sortArr[i]){
            return i;
        }
    }
};

const result = missingNumber([3,0,1]);
console.log(result);