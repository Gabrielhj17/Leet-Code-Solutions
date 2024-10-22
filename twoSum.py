# Brief
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution
class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the indices of the numbers we've seen
        seen = {}
        
        # Enumerate through numbers in nums list
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # If the complement is in the dictionary, return the indices
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the current number with its index in the dictionary
            seen[num] = i