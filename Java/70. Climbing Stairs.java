//https://leetcode.com/problems/climbing-stairs/

class Solution {

    int calculatePaths(int n, int savePaths[]){
        if(savePaths[n] != -1){
            return savePaths[n];
        }
        else if(n <= 1){
            return 1;
        }
       return  savePaths[n] = calculatePaths(n-1, savePaths) + calculatePaths(n-2, savePaths);
    }
    
    public int climbStairs(int n) {
        int savePaths[] = new int[n + 1];
        Arrays.fill(savePaths, -1);
        return calculatePaths(n, savePaths);
        
    }
}