<?php 
class Solution {

    /**
     * @param string $pattern
     * @param string $s
     * @return boolean
     */
    function wordPattern($pattern, $s) {
        $words = explode(" ", $s);
        $charPatterns = str_split($pattern);

        if(count($words) !== count($charPatterns)){
            return false;
        }

        $charToWord = [];
        $wordToChar = [];

        for($i = 0; $i < count($words); $i++){
            $char = $charPatterns[$i];
            $word = $words[$i];

            if(isset($charToWord[$char])){
                if($charToWord[$char] !== $word){
                    return false;
                } 
            } else {
                $charToWord[$char] = $word;
            }

            if(isset($wordToChar[$word])){
                if($wordToChar[$word] !== $char){
                    return false;
                }
            } else {
                $wordToChar[$word] = $char;
            }
        }
        return true;
    }
}

$s = "dog cat log dog";
$word = new Solution();
$result = $word->wordPattern("abba", $s);
var_export($result);
?>