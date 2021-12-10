class Solution {
    public int removeDuplicates(int[] nums) {
        Map<Integer, Integer> arr = new LinkedHashMap<>();
		for (int i = 0; i < nums.length; i++) {
			if (!arr.containsKey(nums[i]))
				arr.put(nums[i], 1);
		}
		int j = 0;
		for (Map.Entry<Integer, Integer> entry : arr.entrySet()) {
			nums[j] = entry.getKey();
			j++;
		}
		return j;
    }
}