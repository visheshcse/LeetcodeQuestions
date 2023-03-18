class Solution {
public:
    int stair(int n, int a[]){
        if(n < 0)
            return 0;
        if(n == 0)
            return 1;
        if(a[n]!= -1)
            return a[n];
        return a[n] = stair(n-1, a)+stair(n-2, a);
    }
    int climbStairs(int n) {
        int a[n+1];
        for(int i = 0; i <= n; i++)
            a[i] = -1;
        return stair(n, a);
    }
};