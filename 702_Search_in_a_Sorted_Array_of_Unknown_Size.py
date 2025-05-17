# We perform a modified binary search on the array by first determining an upper bound
# for the search range by exponentially increasing the `right` bound until we find an element
# greater than or equal to the target. Once we have the range, we apply standard binary search
# within that range to find the target. This ensures a time complexity of O(log n).
# Time Complexity: O(log n)
# Space Complexity: O(1)


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        # Rreading from the array and return Integer.MAX_VALUE for out of bounds indices
        if index < 0 or index >= len(self.arr):
            return 231 - 1  # equivalent to Integer.MAX_VALUE
        return self.arr[index]

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Find the upper bound by exponentially increasing the range
        left, right = 0, 1
        while reader.get(right) < target and reader.get(right) != 231 - 1:
            left = right
            right *= 2

        # Apply binary search within the determined range
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = reader.get(mid)

            if mid_value == target:
                return mid  # Return the index if target is found
            elif mid_value < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return -1  # Return -1 if the target is not found


# Testing the code

# Test 1: Search for target = 9 in secret = [-1, 0, 3, 5, 9, 12]
reader = ArrayReader([-1, 0, 3, 5, 9, 12])
solution = Solution()
# Expected output is 4, as 9 is found at index 4
assert solution.search(reader, 9) == 4

# Test 2: Search for target = 2 in secret = [-1, 0, 3, 5, 9, 12]
# Expected output is -1, as 2 is not present in the array
assert solution.search(reader, 2) == -1

print("All tests passed!")