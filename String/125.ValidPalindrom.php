<?php 
class Solution {
    function isPalindrome($s) {
        $string = strtolower(preg_replace('/[^a-z0-9]/i', '', $s));

        $reversed = strrev($string);

        if ($string === $reversed) {
            return true;
        } else {
            return false;
        }
    }
}

$s = "A man, a plan, a canal: Panama";
$string = new Solution();
$result = $string->isPalindrome($s);
echo $result;
?>