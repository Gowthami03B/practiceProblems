class Solution {
    public boolean isValid(String s) {
      HashMap<Character, Character> map = new HashMap<>();
		map.put('}', '{');
		map.put(')', '(');
		map.put(']', '[');
		Stack<Character> charStack = new Stack<>();
		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (map.containsKey(c)) {
				char topElement = charStack.empty() ? '#' : charStack.pop();
				if (topElement != map.get(c))
					return false;
			} else {
				charStack.push(c);
			}
		}
		return charStack.isEmpty();
	}
}
