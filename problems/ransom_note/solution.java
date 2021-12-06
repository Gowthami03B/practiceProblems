class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
 HashMap<Character, Integer> hashy = new HashMap<>();
		if(ransomNote.length() > magazine.length())
			return false;
		if(ransomNote == null || magazine == null)
			return false;
		for(int i =0; i < magazine.length(); i++) {
			hashy.put(magazine.charAt(i), hashy.getOrDefault(magazine.charAt(i), 0)+ 1);
		}
		for(int i =0; i < ransomNote.length(); i++) {
			if(hashy.getOrDefault(ransomNote.charAt(i), 0) >= 1)
				hashy.put(ransomNote.charAt(i) , hashy.get(ransomNote.charAt(i)) - 1);
			else
				return false;
		}
		return true;
    }
}