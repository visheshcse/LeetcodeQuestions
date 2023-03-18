//https://leetcode.com/problems/plus-one/

class Solution {
    public int[] plusOne(int[] digits) {
        int add = 1;
        for(int i = digits.length -1; i >=0 ; i--){
            int temp = digits[i] + add;
            if(temp !=10){
                digits[i] = temp;
                add = 0;
                break;
            }
            else{
                digits[i] = 0;
                add = 1;
            }   
        }
        if(add == 1){
            int[] newDigits= new int[digits.length + 1];
            newDigits[0] = 1;
            for(int i = 0; i < digits.length ; i++){
                newDigits[i+1] = digits[i];
            }
            return newDigits;
        }
        return digits;        
    }
}