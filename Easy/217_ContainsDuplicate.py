"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}

        for n in nums:
            if n in dic:
                return True
            else:
                dic[n]=1
        
        return False

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4],  # No duplicates
        [1, 2, 3, 1],  # Duplicates present
        [3, 3, 3, 3, 3],  # All elements are the same
        [4, 5, 6, 7],  # No duplicates
        []  # Empty list
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.containsDuplicate(case)
        print(f"Test Case {i}: Input = {case}, Contains Duplicate? {result}")