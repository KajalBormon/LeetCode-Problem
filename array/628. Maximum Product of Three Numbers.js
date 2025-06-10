var maximumProduct = function(nums) {
   nums.sort((a,b) => a - b);
   const n = nums.length; 
   product1 = nums[n-1] * nums[n-2] * nums[n-3];
   product2 = nums[0] * nums[1] * nums[n-1];

   return Math.max(product1, product2);
};

const result = maximumProduct([-1,-2,-3]);
console.log(result);