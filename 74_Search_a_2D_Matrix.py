# The matrix can be treated as a flattened sorted array.
# We use binary search by treating the matrix as a 1D array and adjusting indices accordingly to perform the search in O(log(m * n)) time.
# The algorithm compares the middle element and narrows down the search range based on whether the target is greater or less than the middle element.
# TC: O(log(m * n)) m is the no of rows and n is no of columns.
# SC: O(1)

# Did this code successfully run on Leetcode : Yes

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start binary search across the matrix treated as a 1D sorted array
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1  # Initialize the search space as a flat array

        while left <= right:
            mid = (left + right) // 2  # Find the middle index
            mid_value = matrix[mid // n][mid % n]  # Convert mid to row and column indices

            if mid_value == target:  # If the middle value is the target, return True
                return True
            elif mid_value < target:  # If the middle value is less than target, move right
                left = mid + 1
            else:  # If the middle value is greater than target, move left
                right = mid - 1

        return False