<?php 
class Solution {

    /**
     * @param string $columnTitle
     * @return integer
     */
    function titleToNumber($columnTitle) {
        $length = strlen($columnTitle);
        $result = 0;

        for($i = 0; $i < $length; $i++){
            $characterValue = ord($columnTitle[$i]) - (ord('A')) + 1; 

            $result = $result * 26 + $characterValue;
        }
        return $result;
    }
}

$column = new Solution();
echo $column->titleToNumber("A");
?>