class Solution {
    public int majorityElement(int[] nums) {
       //  int maxTimes = nums.length/2;
       //  Map<Integer, Integer> map = new HashMap<>();
       //  for(int n : nums){
       //       map.put(n, map.getOrDefault(n,0)+1);
       //      if(map.get(n) > maxTimes){
       //          return n;
       //      }
       //  }
       //  // for(int key : map.keySet()){
       //  //     if(map.get(key) > maxTimes){
       //  //         return key;
       //  //     }
       //  // }
       // return -1; 
        int count = 0;
        int ele = 0;
        for(int num : nums){
            if(count == 0){
                ele = num;
            }
            count += (ele == num) ? 1 : -1;
        }
        return ele;
    }
}