# We apply binary search to the rotated sorted array, identifying which half of the array is sorted in each step.
# Based on the comparison with the middle element, we determine if the target lies in the sorted half or the unsorted half.
# By adjusting the search range accordingly, we achieve a time complexity of O(log n) for the search.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Did this code successfully run on Leetcode : Yes


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right= 0,len(nums) -1

        while left<= right:
            mid = (left+right)// 2

            # Check if the middle element is the target
            if nums[mid] ==target:
                return mid

            # Determine if the left half is sorted
            if nums[left]<= nums[mid]:
                # Target is in the sorted half
                if nums[left]<= target < nums[mid]:
                    right =mid - 1
                else:
                    left =mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left =mid + 1
                else:
                    right =mid - 1

        return -1