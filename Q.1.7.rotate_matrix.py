import unittest
# Rotate Matrix: Given an image represented by an NxN matrix, 
# where each pixel in the image is 4 bytes, write a method to 
# rotate the image by 90 degrees. Can you do this in place? 

# Clarify: Which direction? Assuming clock-wise.

# Example
# 1 2 3 0      0 7 4 1
# 4 5 6 0 ->   0 8 5 2
# 7 8 9 2      0 9 6 3
# 0 0 0 0      0 2 0 0

# Observation:  0th col became 2nd row.
# for 3x3       1st col became 1st row.
#               2nd col became 2th row.  but inverse



# inverse of i'th row will become i'th column.

def rotate_matrix1(m):

    if len(m) == 0 or len(m) == 1:
        return m

    result = []

    for col in range(n):
        result.append([])
        for row in range(n-1,-1,-1):
            result[-1].append(m[row][col])
    return result


# Complexity: Time O(n^2) , Space O(n^2) Not efficient

# How can we perform this in place to get rid of O(n^2) space complexity?
# Swap each element layer by layer.

def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1 
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()