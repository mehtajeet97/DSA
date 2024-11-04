Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

Solution 2:

Yes, an O(n) solution is possible by leveraging the fact that nums is a sorted array (presumably non-decreasing) of integers. Since the square of negative numbers will eventually be greater than the square of smaller positive numbers, we can use a two-pointer approach to efficiently build a sorted array of squared values.

Here’s the approach in detail:

Approach
Initialize two pointers: one at the beginning (left) and one at the end (right) of the array.
Compare the square of the elements at these pointers.
Since the largest squared value will be either at the left or right pointer, insert the larger square at the end of the result array (building it backwards).
Move the pointer that had the larger square inward (if left had the larger square, move left to the next element; if right had the larger square, move right to the previous element).
Continue this process until all elements are processed.
