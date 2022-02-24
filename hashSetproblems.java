package practice;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class hashSetproblems {

	public static void main(String[] args) {
		hashSetproblems h = new hashSetproblems();
		int[] nums = { 1, 2, 2, 3, 1, 4, 3 };
		findDuplicates(nums);
		findNonRepeatingElement(nums);
		System.out.println(h.findSingleRepeatingElement(nums));
	}

	public static void findDuplicates(int[] nums) {
		Set<Integer> arrSet = new HashSet<>();
		for(int i = 0; i < nums.length; i++) {
			if(!arrSet.add(nums[i])) {
				System.out.println("Duplicate element.." + nums[i]);
			}
		}
	}
	
	////O(n), O(n) -extra space for set
	public static void findNonRepeatingElement(int[] nums) {
		Set<Integer> arrSet = new HashSet<>();
		Set<Integer> arrSet1 = new HashSet<>();
		for(int i = 0; i < nums.length; i++) {
			arrSet1.add(nums[i]);
			if(arrSet.contains(nums[i])) {
				arrSet.remove(nums[i]);
			}else {
				arrSet.add(nums[i]);
			}
		}
		arrSet1.removeAll(arrSet);
		System.out.println(arrSet + "Non repeating element");
		System.out.println(arrSet1 + "Duplicate elements");
	}
	
//	Find the element that appears once in an array with all other elements appearing twice
	//O(n), O(1) - no extra space
//   a) XOR of a number with itself is 0.
// b) XOR of a number with 0 is number itself.

// hence we do xor operation, result will be the only non-repeating element

// Let us consider the above example.  
// Let ^ be xor operator as in C and C++.

// res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

// Since XOR is associative and commutative, above 
// expression can be written as:
// res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
//     = 7 ^ 0 ^ 0 ^ 0
//     = 7 ^ 0
//     = 7 

	public int findSingleRepeatingElement(int[] nums) {
		int res = 0;
		for(int i = 0; i < nums.length; i++) {
			res = res ^ nums[i];
		}
		return res;
	}
}
