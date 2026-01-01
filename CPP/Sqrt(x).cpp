class Solution {
public:
    int mySqrt(int x) {
        if(x == 0 || x == 1)
            return x;
        double i = 1;
        while(i*i < x){
            i++;
        }
        if(i*i > x)
            return i-1;
        return i;
    }
};