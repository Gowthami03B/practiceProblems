package practice;

public class bestTimeToBuyStock {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		bestTimeToBuyStock m = new bestTimeToBuyStock();
		int[] nums = {7,1,5,3,6,4};
		System.out.println(m.maxProfitOptimal(nums));
	}
	
	public int maxProfit(int[] prices) {
        int end  = prices.length - 1;
        int maxprofit = 0;
        for(int i = end; i >= 1; i--) { //>= when array has only 2 numbers
        	int start = 0;
            while(start < i){
                maxprofit = Math.max(maxprofit, prices[i] - prices[start]);
                System.out.println(prices[i] + " " + maxprofit);
                start++;
            }
        }
        return maxprofit < 0? 0: maxprofit;
    }
	
	public int maxProfitOptimal(int[] prices) {
        int profit = 0, min = prices[0];        
        for(int price: prices) {
          profit = Math.max(profit, price - min);
          min = Math.min(min, price);
        }        
        return profit;
    }

}
