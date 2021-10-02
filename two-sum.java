package practice;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class TwoSum {
	
	public static void main(String[] args) {
		System.out.println("Enter target sum ");
		Scanner scanner = new Scanner(System.in);
		int targetNum = scanner.nextInt();
		int result[] = findTwoSumHashMap(targetNum);
		if (result.length == 2) {
            System.out.println(result[0] + " " + result[1]);
        } else {
            System.out.println("No solution found!");
        }
		scanner.close();
	}
	
	public static int[] findTwoSumBruteForce(int targetNum) {
		int arr[] = {3,6,20,34,45,89};
		//using addition (O(n^2))
		for(int i = 0; i < arr.length; i++) {
			for(int j = 1; j< arr.length; j++) {
				if(arr[i] + arr[j] == targetNum)
					return new int[] {i , j};
			}
		}
		return new int[] {};
	}
	
	public static int[] findTwoSumHashMap(int targetNum) {
		int arr[] = {3,6,20,34,45,89};
		//using subtraction O(n)
		//subtract number from expected sum, the value is the other number to add with current number
		Map<Integer, Integer> inthashMap = new HashMap<>();
		for (int i = 0; i < arr.length; i++) {
            int complement = targetNum - arr[i];
            if (inthashMap.containsKey(complement)) {
                return new int[] { inthashMap.get(complement), i };
            } else {
            	inthashMap.put(arr[i], i);
            }
        }
        return new int[] {};
	}
}
