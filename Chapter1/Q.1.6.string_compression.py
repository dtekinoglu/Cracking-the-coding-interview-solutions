import unittest

# Question: : Implement a method to perform basic string compression using the counts 
#of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
#"compressed" string would not become smaller than the original string, your method should return 
#the original string. You can assume the string has only uppercase and lowercase letters (a - z)

#Clarify: Case-sensitive? Cc becomes C1c1.
         # If a character occurs only once consecutively, then compression makes the string longer.
         # Else, it makes the string shorter.
         # Are we allowed to use additional string? Or should we perform the operation in place?
         # For empty string -> I will return itself since compressed version will be longer anyway.

# Plan: Create an empty string. Iterate over the original one.
# Set currentCount to 0. And increment it as long as the same characters appears consecutively.
# Whenever the character changes, set currentCount to 0.

def string_compression(s):
    if len(s) == 0 or len(s) ==1:  # O(1)
        return s
    
    currentChar = s[0]  # O(1)
    currentCount = 1  # O(1)

    result=[]  # O(1)

    for i in range(1, len(s)):   # O(n)
        if s[i] == currentChar:
            currentCount +=1
            if i == len(s)-1:
                result.append(currentChar)
                result.append(str(currentCount))
        else:
            result.append(currentChar)
            result.append(str(currentCount))
            currentChar = s[i]
            currentCount = 1
        if len(result) > len(s):
            return s
    
    return ''.join(result)

#To compute s = s1 + s2 + ... + sn,

    # using +. A new string s1+s2 is created, then a new string s1+s2+s3 is created,..., etc, 
    # so a lot of memory allocation and copy operations is involved. In fact, s1 is copied n-1 times, s2 is copied n-2 time, ..., etc.

    # using "".join([s1,s2,...,sn]). The concatenation is done in one pass, 
    # and each char in the strings is copied only once.

# Time O(n), Space O(n)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

