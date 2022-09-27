import unittest

# String Rotation: Assume you have a method isSubString which checks if one word is a substring 
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only 
# one call to i5Sub5tring (e.g., "waterbottle" is a rotation of"erbottlewat"). 

# abcd -> bcda, cdab, dabc, abcd.
# Q: The string is a valid rotation of itself?
# Lengths must be the same. 

# Brute Force: Form every possible rotation. Check if s2 is one of them.
#              Takes O(n^2) time for forming rotations. For each rotation, checking if it is the same
#               with s2 takes O(n) time. Not efficient.


# Observation: let s1 = abcde,  s2 = cdeab
#               (x= ab, y= cde) then s1= xy, s2 = yx
#               s2 exist in xyxy. So we can concatenate s1 with itself and check if s2 is a substring.
#               Time O(n) assuming that isSubstring runs in O(A+B) time for strings of length A and length B,
#               Space O(n)


def string_rotation(s1,s2):

    if len(s1) != len(s2):
        return False
    
    s1 = s1 +s1
    if s2 in s1:
        return True

    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
        ('string1','string2', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()