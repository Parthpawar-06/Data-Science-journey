# Question link: https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_10870953
# Problem statement
# Ninja and his friend are playing a game of subarrays. They have an array ‘NUMS’ of length ‘N’. Ninja’s friend gives him an arbitrary integer ‘K’ and asks him to find the length of the longest subarray in which the sum of elements is equal to ‘K’.
# Ninjas asks for your help to win this game. Find the length of the longest subarray in which the sum of elements is equal to ‘K’.
# If there is no subarray whose sum is ‘K’ then you should return 0.
# Example:
# Input: ‘N’ = 5,  ‘K’ = 4, ‘NUMS’ = [ 1, 2, 1, 0, 1 ]
# Output: 4
# There are two subarrays with sum = 4, [1, 2, 1] and [2, 1, 0, 1]. Hence the length of the longest subarray with sum = 4 is 4.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 1 <= N <= 10^5
# -10^6 <= NUMS[ i ] <= 10^6
# -10^6 <= K <= 10^6
# Sum of N Over all the Test cases <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 2
# 3 5
# 2 3 5
# 3 1
# -1 1 1
# Sample Output 1 :
# 2
# 3
# Explanation Of Sample Input 1 :
# For the first case:
# There are two subarrays with sum = 5, [2, 3] and [5]. Hence the length of the longest subarray is 2.
# For the second case:
# Longest subarray with sum = 1 is [1, -1, 1].
# Sample Input 2 :
# 2
# 3 4
# 1 1 1
# 3 2
# -50 0 52
# Sample Output 2 :
# 0 
# 3

#Solution 1 : Brute - Force:
from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    n = len(nums)

    max_count  = 0
    for i in range(n):
        summ = 0
        for j in range(i,n):
            summ+=nums[j]
            if(summ==k):
                current_len = j-i+1
                if current_len>max_count:
                    max_count = current_len


    return max_count
    pass

#Solution 2 : Optimised Solution :

from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    n = len(nums)
    current_sum = 0
    max_len = 0
    sum_map = {}
    for i in range(n):
        current_sum +=nums[i]

        if current_sum == k:
            max_len = i+1

        elif (current_sum - k) in sum_map:
            length = i - sum_map[current_sum - k]
            if length>max_len:
                max_len = length
        
        if current_sum not in sum_map:
            sum_map[current_sum] = i 
    
    return max_len

    pass



