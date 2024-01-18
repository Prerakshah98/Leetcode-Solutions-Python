"""Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        count = 0
        target = nums[len(nums)//2]

        for n in nums:
            count += abs(target-n)

        return count
    

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3],
        [1, 10, 2, 9]
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.minMoves2(case)
        print(f"Test Case {i}: nums = {case}, Minimum Moves = {result}")