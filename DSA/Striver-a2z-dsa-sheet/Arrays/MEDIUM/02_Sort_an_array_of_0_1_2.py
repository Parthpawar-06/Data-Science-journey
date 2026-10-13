#Question Link : https://leetcode.com/problems/sort-colors/description/
# You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function. 
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Explanation:
# The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Explanation:
# The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

#Solutions:  Brut-Force:

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
  
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


#Optimise approach 1 : with 2 loop pass


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0  
        end = n-1
        for i in range(n):
            if nums[i]==0:
                nums[i],nums[j] = nums[j],nums[i]
                j = j+1
    
        while(j<end):
            if nums[j]==2 and nums[end]==2:
                end-=1
            elif nums[j]==2 and nums[end]==1:
                nums[j],nums[end]=nums[end],nums[j]
                j+=1
                end-=1
            elif nums[j]==1 and nums[end]==1:
                j+=1
            else:
                j+=1
                end-=1


#Optimise Approach 2: with only one loop pass

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0
        mid = 0
        high = len(nums)-1

        while(mid<=high):
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
