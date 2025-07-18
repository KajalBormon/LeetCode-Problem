<?php
class Solution {
     function convertToTitle($columnNumber) {
        $result = '';
        while($columnNumber > 0)
        {
            $columnNumber--;
            $letterIndex = $columnNumber % 26;
            $char = chr($letterIndex + 65);
            $result = $char.$result;
            $columnNumber = intdiv($columnNumber, 26);
        }
        return $result;
    }
}

$columnNumber = 28;
$solution = new Solution();
$result = $solution->convertToTitle($columnNumber);
echo $result;
?>