class Solution {
    public int expressiveWords(String s, String[] words) {
		int stretchyWordCnt = 0;
		for(String c : words) {
			if(checkStretchyWords(s, c))
				stretchyWordCnt++;
		}
		return stretchyWordCnt;
	}
	
	public boolean checkStretchyWords(String s, String wrd) {
		//if chars equal
		//find lengths
		//length constraint
		int i = 0,j = 0;
		while(i < s.length() && j < wrd.length()) {
			int lenS = 0, lenWrd = 0;
			if(s.charAt(i) == wrd.charAt(j)) {
				lenS = findLength(s, i);
				lenWrd = findLength(wrd, j);
				if(lenS == lenWrd) {
					i += lenS;
					j += lenWrd;
					continue;
				}else if(lenWrd < lenS && lenS >= 3){
					
				}else { 
					return false;
				}
			}else { 
				return false;
			}
			i += lenS;
			j += lenWrd;
		}
		return i ==s.length() && j == wrd.length();
	}
	
	public int findLength(String s, int i) {
		int len = 1;
		i++;
		for(; i < s.length(); i++) {
			if(s.charAt(i) == s.charAt(i - 1))
				len++;
			else 
				break;
		}
		return len;
	}
}