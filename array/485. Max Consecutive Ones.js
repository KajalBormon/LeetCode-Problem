var findMaxConsecutiveOnes = function(nums) {
    var count = 0;
    var maxCount = 0;
    for(num of nums) {
        if(num === 1){
            count++;
            if(count > maxCount){
                maxCount = count; 
            }
        } else {
            count = 0;
        }
    }
    return maxCount;
};

$result = findMaxConsecutiveOnes([1,1,0,1,1,1]);
console.log($result);