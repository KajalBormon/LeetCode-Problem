var majorityElement = function(nums) {
    const times = Math.floor(nums.length / 2);

    let freqMap = {};

    for(num of nums){
        freqMap[num] = (freqMap[num] || 0) + 1;
    }

    const number = Object.keys(freqMap).find(num => freqMap[num] > times);

    return Number(number);
};

const result = majorityElement([2,2,1,1,1,2,2]);
console.log(result);