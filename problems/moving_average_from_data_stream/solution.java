class MovingAverage {
    int size;
	ArrayList<Integer> nums = new ArrayList<>();
    public MovingAverage(int size) {
        this.size = size;
    }
    
    public double next(int val) {
      nums.add(val);
		double sum = 0;
		int div = nums.size() <= size? nums.size() : size;
		int start = nums.size() <= size? 0 : nums.size() - size;
		for(int i = start; i < nums.size(); i++) {
			sum += nums.get(i);
		}
		return sum/div;  
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */