# Problem: Group Anagrams
# Platform: LeetCode | #49 | Medium
# Link: https://leetcode.com/problems/group-anagrams
#
# Key insight: sorting any anagram gives same string
# "eat" → "aet"  |  "tea" → "aet"  |  "ate" → "aet"
# Use sorted string as hashmap key to group them.
#
# Time: O(n * k log k) | Space: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            key = "".join(sorted(i))
        
            if key not in ans:
                ans[key] = []
            ans[key].append(i)
        return list(ans.values())
