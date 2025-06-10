var containsDuplicate = function(nums) {    
    const seen = new Set();
    for(const item of nums){
        // console.log(item);
        if(seen.has(item))
            return true;  
            seen.add(item);
            // console.log(seen);
    }
    return false;
};
const result = containsDuplicate([1,2,3,1]);
console.log(result);