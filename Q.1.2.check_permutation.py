import unittest
from collections import Counter

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
# other.
# Clarification: It should have the same characters with same frequency.
# Example: Python - YhonPy should return True.
# Assumption: Uppercase - lowercase sensitive. So, abc and BCA are not permutations of each other. 
#             The same strings are permutations of each other. No need to return any special thing.

# Approach 1: SORT strings and check if they are the same.
             # Time: O(nlogn), no additional space is used.

def checkEqualBySort(s, q):

    if len(s) != len(q):  # O(1) in Python
        return False
    
    if sorted(s) != sorted(q): # O(nlon(n)) where n is the length of s or q.
        return False
    return True

# Approach 2: COUNT FREQUENCIES.
#             Time: O(n), Space: O(1)

def checkEqualByCount(s, q):

    if len(s) != len(q):
        return False
    
    arr = [0] * 128 # Assuming ASCII characters

    for elem in s:
        arr[ord(elem)] +=1
    
    for elem in q:
        arr[ord(elem)] -=1
    
    if arr.count(0) != 128:
        return False

    return True

def checkEqualByCount2(s, q):

    if len(s) != len(q):
        return False
    
    counter = Counter()

    for elem in s:
        counter[elem] +=1
    
    for elem in q:
        if counter[elem] == 0:
            return False
        counter[elem] -=1 
   
    return True


class Test(unittest.TestCase):
    notPerm = ['abcd', 'aBdc']
    perm = ['123sdf__', '_s1d2f3_']


    def test_permutation_sort(self):
        # true check
        actual = checkEqualBySort(self.perm[0], self.perm[1])
        self.assertTrue(actual)

    def test_permutation_count(self):
        # true check
        actual = checkEqualByCount(self.perm[0], self.perm[1])
        self.assertTrue(actual)
    
    def test_permutation_count2(self):
        # true check
        actual = checkEqualByCount2(self.perm[0], self.perm[1])
        self.assertTrue(actual)

    def test_not_permutation_sort(self):
        # false check
        actual = checkEqualBySort(self.notPerm[0], self.notPerm[1])
        self.assertFalse(actual)

    def test_not_permutation_count(self):
        # false check
        actual = checkEqualByCount(self.notPerm[0], self.notPerm[1])
        self.assertFalse(actual)

    def test_not_permutation_count2(self):
        # false check
        actual = checkEqualByCount2(self.notPerm[0], self.notPerm[1])
        self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()