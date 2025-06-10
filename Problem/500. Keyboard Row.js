var findWords = function(words) {
    const row1 = new Set("qwertyuiop");
    const row2 = new Set("asdfghjkl");
    const row3 = new Set("zxcvbnm");
    const result = [];

    for (const word of words) {
        const lowerWord = word.toLowerCase();
        const firstChar = lowerWord[0];


        let rowSet;
        if (row1.has(firstChar)) {
            rowSet = row1;
        } else if (row2.has(firstChar)) {
            rowSet = row2;
        } else {
            rowSet = row3;
        }

        if (Array.from(lowerWord).every(char => rowSet.has(char))) {
            result.push(word);
        }
    }
    return result;
};

const result = findWords(["Hello", "Alaska", "Dad", "Peace"]);
console.log(result); // ["Alaska", "Dad"]