# Problem statement
# Given an array 'v' of 'n' numbers.
# Your task is to find and return the highest and lowest frequency elements.
# If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element.
# Example:
# Input: ‘n' = 6, 'v' = [1, 2, 3, 1, 1, 4]
# Output: 1 2

# Explanation: The element having the highest frequency is '1', and the frequency is 3. The elements with the lowest frequencies are '2', '3', and '4'. Since we need to pick the smallest element, we pick '2'. Hence we return [1, 2].
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 6
# 1 2 3 1 1 4
# Sample Output 1 :
# 1 2
# Sample Explanation 1:
# Input: ‘n' = 6, 'v' = [1, 2, 3, 1, 1, 4]
# Output: 1 2

# Explanation: The element having the highest frequency is '1', and the frequency is 3. The elements with the lowest frequencies are '2', '3', and '4'. Since we need to pick the smallest element, we pick '2'. Hence we return [1, 2].
# Sample Input 2 :
# 6
# 10 10 10 3 3 3
# Sample Output 2 :
# 3 3
# Sample Explanation 2:
# Input: ‘n' = 6, 'v' = [10, 10, 10, 3, 3, 3]

# Output: 3 3

# Explanation: Since the frequency of '3' and '10' is 3. Therefore, the element with the maximum and minimum frequency is '3'.
# Expected Time Complexity :
# The expected time complexity is O(n), where n is the size of the array.
# Expected Space Complexity :
# The expected time complexity is O(n), where n is the size of the array.
# Constraints :
# 2 <=  n <= 10^4
# 1 <= v[i] <= 10^9
# There are at least two distinct elements in the array.
# Time Limit: 1 sec 

from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    maxx = -1
    minn = float('inf')
    max_element = -1
    min_element = -1
    freq={}

    for i in v:
        freq[i]=freq.get(i,0)+1


    for element,count in sorted(freq.items(),key = lambda x:x[0]):
        if maxx<count:
            maxx = count
            max_element = element
        if minn>count:
            minn = count
            min_element = element
        
    return [max_element,min_element]
    pass

## optimised solution with O(n) time complexity :

from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    maxx = -1
    minn = float('inf')
    max_element = -1
    min_element = -1
    freq={}

    for i in v:
        freq[i]=freq.get(i,0)+1


    for element,count in freq.items():
        if maxx<count or (maxx==count and element<max_element):
            maxx = count
            max_element = element
        if minn>count or (minn == count and element<min_element):
            minn = count
            min_element = element
        
    return [max_element,min_element]
    pass
