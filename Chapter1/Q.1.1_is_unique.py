import unittest

# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Question: ASCII or Unicode string

# Approach 1: Compare each element with every other element of the string
#             Time -> O(n^2) Space -> O(1)

def isUniqueBruteForce(s):

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# Approach 2: Use hash table to store frequency of each element
#             Time -> O(n) Space -> O(1)
# Instead of hash table we can use a boolen arrat of length 128 (ASCII).

# We can also argue that time compl is O(1) since the loop will never iterate more than 128.
# If you didn't want to assume the character set is fixed, you could express the complexity as 
#O( c) space and O(min ( c, n)) or O( c) time, where c is the size of the character set. 

# How about using a bit vector?

def isUniqueHashTable(s):
    
    hashTable = {}

    for elem in s:
        if elem not in hashTable:
            hashTable[elem] = 1
        else:
            return False
    return True
    
# Approach 3: Sort the array
#             Time O(nlog(n)), No additional space is used.

def isUniqueSort(s):

    s = sorted(s)

    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

class Test(unittest.TestCase):
    unique = [('abcd'), ('s4fad'), ('')]
    notUnique = [('23ds2'), ('hb 627jh=j ()')]


    def test_unique_brute_force(self):
        # true check
        for test_string in self.unique:
            actual = isUniqueBruteForce(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.notUnique:
            actual = isUniqueBruteForce(test_string)
            self.assertFalse(actual)

    def test_unique_hash_table(self):
        # true check
        for test_string in self.unique:
            actual = isUniqueHashTable(test_string)
            self.assertTrue(actual)
            
        # false check
        for test_string in self.notUnique:
            actual = isUniqueHashTable(test_string)
            self.assertFalse(actual)

    def test_unique_sorting(self):
        # true check
        for test_string in self.unique:
            actual = isUniqueSort(test_string)
            self.assertTrue(actual)
            
        # false check
        for test_string in self.notUnique:
            actual = isUniqueSort(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
