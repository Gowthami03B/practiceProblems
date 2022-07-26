"""
You decide to create a substitution cipher. The cipher alphabet is based on a key shared amongst those of your friends who don't mind spoilers.

Suppose the key is:
"The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!".

We use only the unique letters in this key to set the order of the characters in the substitution table.

T H E Q U I C K O N Y X G B L R A S W D J M P V Z F

(spaces added for readability)

We then align it with the regular alphabet:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T H E Q U I C K O N Y X G B L R A S W D J M P V Z F

Which gives us the substitution mapping: A becomes T, B becomes H, C becomes E, etc.

Write a function that takes a key and a string and encrypts the string with the key.

Example:
key = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!"
encrypt("It was all a dream.", key) -> "Od ptw txx t qsutg."
encrypt("Would you kindly?", key) -> "Pljxq zlj yobqxz?"

Complexity analysis:

m: The length of the message
k: The length of the key
''
"""
def encrypt(plaintext: str, key: str) -> str:
    clean_key = list(dict.fromkeys([ch.upper() for ch in key if ch.isalpha()]))
    print(clean_key)
    encrypted_list = []
    for ch in plaintext:
        if ch.isupper():
            encrypted_list.append(clean_key[ord(ch) - ord('A')])
        elif ch.islower():
            encrypted_list.append(clean_key[ord(ch) - ord('a')].lower())
        else:
            encrypted_list.append(ch)

    return ''.join(encrypted_list)


key = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!"
print(encrypt("It was all a dream.", key))  # "Od ptw txx t qsutg."
print(encrypt("Would you kindly?", key))  # "Pljxq zlj yobqxz?"
