import unittest

# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.

# 1. Clarify: Are all elements integers?
# 2. Plan: 3 options:
#           - a. Store indices of all zeros -> takes O(MN) space complexity
#           - b. Store row and column indices (rowArray, columnArray) that must be converted to zero -> O(M+N) space
#           - c. We can use the first cell of every row and column as a flag. This flag would 
#               determine whether a row or column has been set to zero.

def zero_matrix(m):
    rowHasZero = False
    colHasZero = False

    for i in range(len(m)): # Check if there are zeros in the first column.
        if m[i][0] == 0:
            colHasZero = True
            break
    
    for i in range(len(m[0])): # Check if there are zeros in the first row.
        if m[0][i] == 0:
            rowHasZero = True
            break
    
    for i in range(1, len(m)):  # Replace first row and column with rowArray, columnArray
        for j in range(1, len(m[0])):
            if m[i][j] == 0:
                m[0][j] = 0
                m[i][0] = 0
    
    for i in range(len(m)):  # Setting rows to zero            
        if m[i][0] == 0:
            for j in range(1, len(m[0])):
                m[i][j] = 0

    for i in range(len(m[0])): # Setting columns to zero
        if m[0][i] == 0:
            for j in range(1, len(m)):
                m[j][i] = 0
    
    if rowHasZero:
        for col in range(len(m[0])):
            m[0][col] = 0

    if colHasZero:
        for row in range(len(m)):
            m[row][0] = 0
    return m

# Time Compl : O(MN). Space O(1)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

    


