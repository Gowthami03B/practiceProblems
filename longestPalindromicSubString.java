package practice;

public class longestPalindromicSubString {

	public static void main(String[] args) {
		longestPalindromicSubString n = new longestPalindromicSubString();
		System.out.println(n.longestPalindrome("aabbad"));
	}

	// we can generate all the substrings of a string in O(N2) for each character in
	// the string and the find each of them is a palindrome and then find the
	// largest - O(N3)
	public String longestPalindrome(String s) {
		if (s == null || s.length() < 1)
			return "";
		int start = 0, end = 0;
		for (int i = 0; i < s.length(); i++) {
			int len1 = expandAroundCenter(s, i, i);
			int len2 = expandAroundCenter(s, i, i + 1);
			int len = Math.max(len1, len2);
			if (len > end - start) {
				start = i - (len - 1) / 2;
				end = i + len / 2;
			}
		}
		return s.substring(start, end + 1);
	}

	private int expandAroundCenter(String s, int left, int right) {
		int L = left, R = right;
		while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
			L--;
			R++;
		}
		return R - L - 1;
	}
}
