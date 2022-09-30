import unittest
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of 
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to 
# just dictionary words. 

#EXAMPLE 
#Input: Tact Coa 
#Output: True (permutations: "taco cat", "atco eta", etc.)

# Clarification: Since it is not limited to dictionary words, conditions for a valid permutation
# can be stated as follows:
# There will be at most one character whose number of occurence is odd.
# Questions: What about empty string? What should I return?
#            Strings with one character?
#            Do we consider spaces? Or only alphabetic characters?
#            If a string is already a palindrome, is it still considered as a permutation of palindrome?
#            Uppercase-lowercase? According to the example -> NOT case-sensitive

# Assumptions: Don't consider spaces. Assume that only alphabetic characters are important.

# APPROACH 1: 1. Create a frequency dictionary, count number of occurences of each alphabetic character.
#             2. If there are more than one character with odd frequency return False.
# Complexity: Time O(n), Space O(1)

# APPROACH 2: 1. Sort the string.
#             2. If there are more than one character with odd frequency return False.
# Complexity: Time O(nlogn), Space O(1)

def check_palindrome_by_dict(s):
    counts = {}
    s = s.lower()
    for ch in s:
        if ch.isalpha():
            if ch not in counts:
                counts[ch] =1
            else:
                counts[ch] +=1
    """
    Another option:
     
    from collections import Counter
    counts = Counter(s)
    """
    
    flag = False
    for key in counts:
        if counts[key] %2 == 1 and flag:
            return False
        if counts[key] %2 == 1 and not flag:
            flag = True
    
    return True


def check_palindrome_by_sort(s):
    
    s = sorted(s.lower())
    flag = False
    countCurrent = 0

    for i in range(len(s)):
        if s[i].isalpha() == False:
            continue
        if i == 0:
            countCurrent =1
        else:
            if s[i] == s[i-1]:
                countCurrent+=1
            else:
                if countCurrent % 2 ==1 and flag:
                    return False
                elif countCurrent %2 and not flag:
                    flag = True
                    countCurrent = 1
                else:
                    countCurrent = 1
    if countCurrent % 2 ==1 and flag:
        return False
    
    return True

class Test(unittest.TestCase):
    valid = ["Tact Coa      "," ", "Aa","Able was I ere I saw Elba","jhsabckuj ahjsbckj","no x in nixon"]
    invalid = ["ob", "b S","Random Words saaa"] 

    def test_check_palindrome_by_dict_true(self):
        for test_string in self.valid:
            actual = check_palindrome_by_dict(test_string)
            self.assertTrue(actual)
    
    def test_check_palindrome_by_sort_true(self):
        for test_string in self.valid:
            actual = check_palindrome_by_sort(test_string)
            self.assertTrue(actual)

    def test_check_palindrome_by_dict_false(self):
        for test_string in self.invalid:
            actual = check_palindrome_by_dict(test_string)
            self.assertFalse(actual)
    
    def test_check_palindrome_by_sort_false(self):
        for test_string in self.invalid:
            actual = check_palindrome_by_sort(test_string)
            self.assertFalse(actual)
     
if __name__ == "__main__":
    unittest.main()