var canPlaceFlowers = function(flowerbed, n) {
    for(let i = 0; i < flowerbed.length; i++){
        if(flowerbed[i] == 0) {
            const prev = i === 0 ? 0 : flowerbed[i-1];
            const next = i === flowerbed.length -1 ? 0 : flowerbed[i+1];
            if(prev === 0 && next === 0) {
                flowerbed[i] = 1;
                n--;
            }
        }
    }
    if(n > 0){
        return false;
    }
    return true; 
};

var result = canPlaceFlowers([1,0,0,0,1], 2);
console.log(result);