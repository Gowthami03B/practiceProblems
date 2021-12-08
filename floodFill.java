package practice;

public class FlashFloodFill {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FlashFloodFill s = new FlashFloodFill();
		int[][] image = {{0,0,0},{0,0,0}};
		System.out.println(s.floodFill(image, 0,0,2));
	}
	
	public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
    	if (null == image || image[sr][sc] == newColor) {
			return image;
		}
		return colorPixel(image, sr, sc, image[sr][sc], newColor);
	}

	private int[][] colorPixel(int[][] image, int sr, int sc, int oldColor, int newColor) {
		if (image[sr][sc] == oldColor) {
			image[sr][sc] = newColor;
			boolean downAllowed = sr + 1 < image.length;
			boolean rightAllowed = sc + 1 < image[0].length;
			boolean upAllowed = sr - 1 >= 0;
			boolean leftAllowed = sc - 1 >= 0;

			if (downAllowed) {
				colorPixel(image, sr + 1, sc, oldColor, newColor);
			}
			if (rightAllowed) {
				colorPixel(image, sr, sc + 1, oldColor, newColor);
			}
			if (upAllowed) {
				colorPixel(image, sr - 1, sc, oldColor, newColor);
			}
			if (leftAllowed) {
				colorPixel(image, sr, sc - 1, oldColor, newColor);
			}
		}
		return image;
	}
}
