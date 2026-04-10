# Problem: Two Sum
# Platform: LeetCode | Difficulty: Easy | #1
# Link: https://leetcode.com/problems/two-sum
#
# Approach 1 — Brute Force: O(n²) time, O(1) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i,j] 
# Approach 2 — Hashmap: O(n) time, O(n) space
# For each num, check if (target - num) already in hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i in range(len(nums)):
            second = target - nums[i]
            if second in ans:
                return [ans[second],i]
            ans[nums[i]] = i
