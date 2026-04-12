# Problem: Valid Anagram
# Platform: LeetCode | #242 | Easy
# Link: https://leetcode.com/problems/valid-anagram
#
# Approach 1 — Sort: O(n log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s = sorted(s)
        t = sorted(t)
        if(s == t):
            return True
        else:
            return False
          
# Approach 2 — Frequency hashmap: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        ans_s = {}
        ans_t = {}

        for char in s:
            ans_s[char] = ans_s.get(char,0)+1
        for char in t:
            ans_t[char] = ans_t.get(char,0)+1
        if(ans_s == ans_t):
            return True
        else:
            return False



        
