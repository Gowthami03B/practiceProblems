// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

// Find and return the maximum profit you can achieve.
package practice;

public class bestTimeToBuyStock2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		bestTimeToBuyStock2 m = new bestTimeToBuyStock2();
		int[] nums = {7,1,5,3,6,4};
		System.out.println(m.maxProfitOptimal(nums));
	}
	
	public int maxProfitOptimal(int[] prices) {
        int profit = 0;
        int n = prices.length;
        for(int i = n -1; i > 0 ; i--) {
        	int diff = prices[i] - prices[i - 1];
        	if(diff > 0)
        		profit+= diff;
        }
        return profit;
    }

}
