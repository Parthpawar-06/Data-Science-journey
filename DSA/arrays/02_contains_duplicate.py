# Problem: Contains Duplicate
# Platform: LeetCode | Difficulty: Easy | #217
# Link: https://leetcode.com/problems/contains-duplicate
#
# Approach 1 — Set comparison: O(n) time, O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!= len(set(nums))


#Approach 2- using hashmap : O(n) time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in nums:
            ans[i] = ans.get(i,0)+1
            if(ans[i]==2):
                return True 
        return False
