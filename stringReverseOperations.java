package practice;

public class stringReverseOperations {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "   Welcome to   geeksforgeeks  ";
        System.out.println(200 + 'B' + "");
        System.out.println("" + 200 + 'B');//when concatenating other types with String, u need to explicitly convert
        System.out.println(reverseWords(s));
        System.out.println(reverseCharsInWordsSb(s));
	}
	
	//reverse the words in a string and remove extra spaces
	public static String reverseWords(String s) {
		String[] temp = s.trim().split(" ");
		//splitting when extra spaces are there would result in the array containing spaces - [Welcome, to, , , geeksforgeeks]
		String finalstr = "";
		String str = "hello dear";
		System.out.println(str.hashCode());
		str+= " gow";
		System.out.println(str);
		System.out.println(str.hashCode());
		for(int i = temp.length-1 ; i >= 0; i--) {
			if(!temp[i].isEmpty()) //hence check if its empty or length != 0
				finalstr += temp[i].trim() + " ";//inefficient as it creates a new string object every time and assigns the reference to finalstr
			System.out.println(finalstr);//always use string builder
		}
		return finalstr.trim();
	}
	
	//More explanation - https://levelup.gitconnected.com/java-algorithms-reverse-words-in-string-leetcode-b6d180252e28
	
	//reverse each word characters using string builder
	public static String reverseCharsInWordsSb(String s) {
		StringBuilder reverseString = new StringBuilder();
		return reverseString.append(s.trim()).reverse().toString().trim();
	}

	//other methods - convert String to character array/byte array and loop and attach words back
}
