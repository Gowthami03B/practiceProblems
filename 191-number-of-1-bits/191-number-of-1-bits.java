public class Solution {
    // you need to treat n as an unsigned value
    // public int hammingWeight(int n) {
    //     int sum = 0;
    //     while(n!=0){
    //         sum++;
    //         n &= n-1;
    //     }
    //     return sum;
    // }
    
    public int hammingWeight(int n) {
        int sum = 0, mask = 1;
        for(int i =0; i<32; i++){
            if((n & mask) != 0){
                sum++;
            }
            mask <<= 1;
        }
        return sum;
    }
}