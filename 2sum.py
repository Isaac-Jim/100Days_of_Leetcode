"""
Problem:
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers 
such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# i will first   try brute force , after i will optimise my solution
def two_sum(nums, target):
    for  i in range(len(nums)):
        for  j in range (i+1,len(nums)):
            if nums[i] + nums[j]== target:
                return[i,j]
    return  []

print(two_sum([2,7,11,15],22))