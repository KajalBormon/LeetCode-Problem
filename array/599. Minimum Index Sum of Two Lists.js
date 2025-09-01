var findRestaurant = function (list1, list2) {
    var countMap = {};
    var result = [];
    var minSum = Infinity;

    for (let i = 0; i < list1.length; i++) {
        countMap[list1[i]] = i;
    }

    for (let j = 0; j < list2.length; j++) {
        let item = list2[j];
        if (countMap.hasOwnProperty(item)) {
            let indexSum = j + countMap[item];

            if (indexSum < minSum) {
                result = [item];
                minSum = indexSum;
            } else if (indexSum === minSum) {
                result.push(item);
            }
        }
    }

    return result;

};

var result = findRestaurant(["happy", "sad", "good"], ["sad", "happy", "good"]);
console.log(result);