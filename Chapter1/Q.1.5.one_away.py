import unittest
# There are three types of edits that can be performed on strings: insert a character, 
#remove a character, or replace a character. Given two strings, write a function to check if 
# they are one edit (or zero edits) away

#EXAMPLE 
#pale, ple -> true 
#pales, pale -> true 
#pale, bale -> true 
#pale, bake -> false 

# 1. Clarification: case sensitive? Assuming yes.
                  # Empty string is one edit away for any string of length 1? Yes.
                  # No restriction on character replacement?
# Observation: Difference of lengths must be <= 1. 
# if len(s) > len(t): then it means that a character was removed from s. 
#  set flag= False. Start iterating over the longer string. When you find a different character, 
# set flag = true and keep iterating. If you find another different character stop and return False.
# if len(s) == len(t): Same idea.
# Time compl: O(n) , space O(1) -> only for flag.

def check_one_away(s,t):

    if len(s) - len(t) > 1 or len(t) - len(s) > 1: # O(1)
        return False
    
    if len(s)+len(t) <=1:
        return True
    
    flag = False
    if len(s) == len(t):
        for i in range(len(s)):  # O(n)
            if s[i] != t[i] and flag:
                return False
            elif s[i] != t[i] and not flag:
                flag = True
    
    else:
        if len(s) > len(t): # O(1)
            longer = s
            shorter = t
        else:
            longer = t
            shorter = s
        
        j = 0
        for i in range(len(longer)):  # O(n)
            if i == len(longer)-1 and j == len(shorter) and not flag: # If the last element is missing.
                return True
            elif longer[i] != shorter[j] and flag:
                return False
            elif longer[i] != shorter[j] and not flag:
                flag = True
            else:
                j+=1
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = check_one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()