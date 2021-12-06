package practice;

import java.util.HashMap;

public class SingleNumber {

  //find the only non-repeating number in the array
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MoveZeroes m = new MoveZeroes();
		int[] val = { 4, 1, 1, 3, 3 };
		System.out.println(m.findSingleNumber1(val));
	}

	public int findSingleNumber(int[] nums) {
		HashMap<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
		}
		for (Integer key : map.keySet()) {
			if (map.get(key) == 1)
				return key;
		}
		return 0;
	}

	public int findSingleNumber1(int[] nums) {
		int result = nums[0];
		for (int i = 1; i < nums.length; i++) {
			result = result ^ nums[i];
		}
		return result;
	}
}
