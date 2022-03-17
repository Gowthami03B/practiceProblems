package practice;

import java.util.LinkedList;

public class InsertInterval {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int val[][] = {{1,3},{6,9}};
		int inserted[] = {2,5};
		InsertInterval c = new InsertInterval();
		System.out.println(c.insert(val, inserted));
	}
	
	public int[][] insert(int[][] intervals, int[] newInterval) {
        //[[1,3],[6,9]] - [2,5]
        int idx = 0, n = intervals.length;
        int newstart = newInterval[0], newend = newInterval[1];
        int[] lastInterval = new int[2];
        LinkedList<int[]> node = new LinkedList<int[]>();
        while(idx < n && newstart > intervals[idx][0]){
            node.add(intervals[idx++]);
        }
        if(node.isEmpty() || newstart > node.getLast()[1]){
            node.add(newInterval);
        }else{
            lastInterval = node.removeLast();
            lastInterval[1] = Math.max(newend, lastInterval[1]);
            node.add(lastInterval);
        }
        while(idx < n){
            lastInterval = intervals[idx++];
            int start = lastInterval[0], end = lastInterval[1];
            if(start > node.getLast()[1]){
                node.add(lastInterval);
            }else{
            lastInterval = node.removeLast();
            lastInterval[1] = Math.max(end, lastInterval[1]);
            node.add(lastInterval);
        }
    }
    return node.toArray(new int[node.size()][2]);
}

}
