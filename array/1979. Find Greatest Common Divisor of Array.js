var findGCD = function(nums) {
    let a = Math.max(...nums);
    let b = Math.min(...nums);
    while(b !== 0){
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a; 
};

$result = findGCD([2,5,6,9,10]);
console.log($result);