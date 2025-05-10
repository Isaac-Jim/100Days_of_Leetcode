'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
'''

#solution
'''
1. store elements in a set
2. for every element
3.check if element is in the set
4. if yes  return the number as a duplicate
5. if no  add the number to the set 
'''

def show_duplicate(nums):
    seen = set()
    for  number in nums:
        if number in seen:
            return number
        else:
            seen.add(number)

print(show_duplicate([1,2,2,4]))
