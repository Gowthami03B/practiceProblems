package practice;

import java.util.ArrayList;

public class MovingAverageDataStream {

	int size;
	ArrayList<Integer> nums = new ArrayList<>();
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MovingAverageDataStream m = new MovingAverageDataStream(3);
		System.out.println(m.next(1));
		System.out.println(m.next(10));
		System.out.println(m.next(3));
		System.out.println(m.next(5));
	}

	public MovingAverageDataStream(int size) {
		this.size = size;
	}

	public double next(int val) {
		nums.add(val);
		double sum = 0;
		int div = nums.size() <= size? nums.size() : size;
		int start = nums.size() <= size? 0 : nums.size() - size;
		//instead of above we can also do - i = Math.max(0, nums.size() - size) // neg no when nums.size < size, positive no when nums.size > size
		//div = Math.min(nums.size(), size) //when nums.size < size, take nums.size, else size
		for(int i = start; i < nums.size(); i++) {
			sum += nums.get(i);
		}
		return sum/div;
	}
}
