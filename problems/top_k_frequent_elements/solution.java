class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if(k == nums.length){
            return nums;
        }
        //creating hashmap with counts
        Map<Integer,Integer> count = new HashMap();
        for(int n : nums){
            count.put(n, count.getOrDefault(n,0) + 1);
        }
        
        //Prioriy queue is min heap by default - hence least frequent elements will be at the head
        //create min heap and add unique elements
        Queue<Integer> pq = new PriorityQueue<>((n1,n2) -> count.get(n1) - count.get(n2));
        //by defalult its a priority queue, but here we need ordering based om frequency of elements
        for(int n : count.keySet()){
            pq.add(n);
            if(pq.size() > k)
                pq.poll();
        }
        
        //create an output array with most occurring elements in descending order
        int[] top = new int[k];
        for(int i=k-1; i >= 0; i--){
            top[i] = pq.poll();
        }
        return top;
    }
}