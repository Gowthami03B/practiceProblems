package practice;

import java.util.HashSet;
import java.util.Set;

public class hashSetproblems {

	public static void main(String[] args) {
		hashSetproblems h = new hashSetproblems();
		int[] nums = { 1, 2, 2, 3, 1, 4, 3 };
		int[] nums1 = {1,2,3,4,4};
		findDuplicates(nums);
		findNonRepeatingElement(nums);
		System.out.println(h.findSingleRepeatingElement(nums));
		System.out.println(h.findDuplicateEle(nums1) + "limited range array duplicate element");
		System.out.println(h.findDuplicateEle1(nums1) + "limited range array duplicate element");
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
		int res = 0;
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
		for(Integer n : arrSet) {
			res = n;
		}
		System.out.println("res" + res);
	}
	
//	  a) XOR of a number with itself is 0.
//	// b) XOR of a number with 0 is number itself.
//
//	// hence we do xor operation, result will be the only non-repeating element
//
//	// Let us consider the above example.  
//	// Let ^ be xor operator as in C and C++.
//
//	// res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4
//
//	// Since XOR is associative and commutative, above 
//	// expression can be written as:
//	// res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
////	     = 7 ^ 0 ^ 0 ^ 0
////	     = 7 ^ 0
////	     = 7 

//	Find the element that appears once in an array with all other elements appearing twice
	//O(n), O(1) - no extra space
	public int findSingleRepeatingElement(int[] nums) {
		int res = 0;
		for(int i = 0; i < nums.length; i++) {
			res = res ^ nums[i];
		}
		return res;
	}
	
	//but both the below solutions only work if the array won't have any missing elements and it has elements like
	//1 2 3 etc etc
	//Given a limited range array of size n containing elements between 1 and n-1 with one element repeating, find the duplicate number in it without using any extra space.
	//double xor
	//we also can use an array to mark indices as true or not but uses extra space
	public int findDuplicateEle(int[] nums) {
		int res = 0;
		for(int val : nums) {
			res = res ^ val;
		}
		for(int i = 1; i <= nums.length - 1; i++) {
			res = res ^ i;
		}
		return res;
	}
	
	//uses extra space for boolean array of size n
	public int findDuplicateEle1(int[] nums) {
		boolean[] visited = new boolean[nums.length];
		for(int value : nums) {
			if(visited[value]) {
				return value;
			}else {
				visited[value] = true;
			}
		}
		return -1;
	}
}
