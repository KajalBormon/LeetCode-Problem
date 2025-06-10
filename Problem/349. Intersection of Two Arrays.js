var intersection = function(nums1, nums2) {
   const countMap = {};
   const result = [];

   for(num of nums1){
    countMap[num] = (countMap[num] || 0)+1;
   }

   for(num of nums2){
    if (countMap[num] > 0){
        result.push(num);
        countMap[num]--;
    }
   }
   return result; 
};

var result = intersection([1,2,2,2,2,1], [2,2,2,2,1]);
console.log(result);