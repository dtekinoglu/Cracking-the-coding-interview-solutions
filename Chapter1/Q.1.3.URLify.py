import unittest
# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string 
#has sufficient space at the end to hold the additional characters, and that you are given the "true" 
#length of the string. (Note: If implementing in Java, please use a character array so that you can 
#perform this operation in place.)

# Clarify: For each space letter, I will put three characters instead: '%20'
#          Example: Mr John Smith ", 13 is input
#                    Output: Mr%20John%20Smith
#          Question: Can I use additional space? Or should I perform the operation in place?


# Plan: In-place modification
#       1. Count the spaces in the actual length of the string.
#       2. Start from the end. 
#               If not space: IndexElement = IndexElement + 2*spaceCount
#               Else: spaceCount -= 1, Add %20 starting from that position

# Complexity: Time O(n), no additional space is used.


# PYTHON STRING IS IMMUTABLE. WE CAN IMPLEMENT THIS IN-PLACE MODIFICATION IN C++ USING THE SAME ALGORITHM. 


def URLify(s, n):

    s = list(s)

    spaceCount = s[:n].count(" ")
    for i in range(n-1, -1,-1):
        if s[i] == " ":
            spaceCount -=1
            s[i+spaceCount*2:i+spaceCount*2+3] = "%20"
        else:
            s[i+spaceCount*2] = s[i]
    
    return ''.join(s)

class Test(unittest.TestCase):
    data = [
        (("much ado about nothing      "), 22,
         ("much%20ado%20about%20nothing")),
        (("Mr John Smith    "), 13, ("Mr%20John%20Smith"))]

    def test_Urlify(self):
        for [test_string, length, expected] in self.data:
            actual = URLify(test_string, length)
            self.assertEqual(actual, expected)

     
if __name__ == "__main__":
    unittest.main()