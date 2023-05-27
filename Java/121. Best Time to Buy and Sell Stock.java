//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int profit = 0;
        for(int i = 0; i < prices.length; i++){ 
            if(prices[i] < min){
                min = prices[i];
            }
            int temp = prices[i] - min;
            if(temp > profit){
                profit = temp;
            }
        }
        return profit;
    }
}