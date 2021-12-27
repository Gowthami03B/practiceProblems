package practice;

import java.util.PriorityQueue;

public class kthlargest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		kthlargest m = new kthlargest();
		int[] nums = { 1, 2, 9, 20, 23, 42, 8 };
		int k = 3;
		System.out.println(m.kthlargest(nums, k));
	}

	public int kthlargest(int[] nums, int k) {
		// implements a min heap (n1-n2) /max heap - n2 - n1
		// The constructor accepts a Comparator<? super E> comparator.Basically the
		// statement (n1, n2) -> n1 - n2 is just a shorthand for
//		 Comparator<Integer> result = new Comparator<Integer>() {
//        @Override
//        public int compare(Integer n1, Integer n2){
//            return n1.compareTo(n2);
//        }
//    };PriorityQueue<Integer> heap = new PriorityQueue<Integer>(result);
		PriorityQueue<Integer> heap = new PriorityQueue<Integer>((n1, n2) -> n2 - n1);
		for (int n : nums) {
			heap.add(n);
			if (heap.size() > k) {
				heap.poll();
			}
		}
		return heap.poll();
	}

}
