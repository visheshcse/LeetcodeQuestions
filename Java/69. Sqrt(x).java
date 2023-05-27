//https://leetcode.com/problems/sqrtx/

class Solution {
    int mySqrt(int x) {
        long sqrt = 0;
        if(x == 0){
            return 0;
        }
        if(x <= 2){
            return 1;
        }
        
        for(long i = 0; i <= x/2 + 1; i++){
            if((i*i) == x){
                sqrt = i;
                break;
            }
            else if((i*i) > x) {
                sqrt = i-1;
                break;
            }
        }
       return (int) sqrt; 
    }
}