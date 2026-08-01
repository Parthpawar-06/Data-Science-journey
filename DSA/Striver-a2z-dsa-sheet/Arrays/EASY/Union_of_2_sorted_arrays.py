# Question link: https://www.naukri.com/code360/problems/sorted-array_6613259
# Problem statement
# Given two sorted arrays, ‘a’ and ‘b’, of size ‘n’ and ‘m’, respectively, return the union of the arrays.
# The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order.
# Note: 'a' and 'b' may contain duplicate elements, but the union array must contain unique elements.
# Example:
# Input: ‘n’ = 5 ‘m’ = 3
# ‘a’ = [1, 2, 3, 4, 6]
# ‘b’ = [2, 3, 5]
# Output: [1, 2, 3, 4, 5, 6]
# Explanation: Common elements in ‘a’ and ‘b’ are: [2, 3]
# Distinct elements in ‘a’ are: [1, 4, 6]
# Distinct elements in ‘b’ are: [5]
# Union of ‘a’ and ‘b’ is: [1, 2, 3, 4, 5, 6]
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 5 3
# 1 2 3 4 6
# 2 3 5
# Sample Output 1 :
# 1 2 3 4 5 6
# Explanation Of Sample Input 1 :
# Input: ‘n’ = 5 ‘m’ = 3
# ‘a’ = [1, 2, 3, 4, 6]
# ‘b’ = [2, 3, 5]
# Output: [1, 2, 3, 4, 5, 6]
# Explanation: Common elements in ‘a’ and ‘b’ are: [2, 3]
# Distinct elements in ‘a’ are: [1, 4, 6]
# Distinct elements in ‘b’ are: [5]
# Union of ‘a’ and ‘b’ is: [1, 2, 3, 4, 5, 6]
# Sample Input 2:
# 4 3
# 1 2 3 3
# 2 2 4
# Sample Output 2:
# 1 2 3 4
# Explanation Of Sample Input 2 :
# Input: ‘n’ = 5 ‘m’ = 3
# ‘a’ = [1, 2, 3, 3]
# ‘b’ = [2, 2, 4]

# Output: [1, 2, 3, 4]

# Explanation: Common elements in ‘a’ and ‘b’ are: [2]
# Distinct elements in ‘a’ are: [1, 3]
# Distinct elements in ‘b’ are: [4]
# Union of ‘a’ and ‘b’ is: [1, 2, 3, 4]
# Expected Time Complexity:
# O(( N + M )), where 'N' and ‘M’ are the sizes of Array ‘A’ and ‘B’.
# Constraints :
# 1 <= 'n', 'm' <= 10^5
# -10^9 <= 'a'[i], 'b'[i] <= 10^9

# Time Limit: 1 sec


#Solution 1:
def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    c = a+b
    return sorted(list(set(c)))
    pass
#Solution 2:
def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    n = len(a)
    m = len(b)
    i =0
    j=0
    union = []
    while (i<n and j<m):
        if(i>0 and a[i]==a[i-1]):
            i=i+1
            continue
        if(j>0 and b[j]==b[j-1]):
            j=j+1
            continue
        if(a[i]<b[j]):
            union.append(a[i])
            i = i+1
        elif(a[i]>b[j]):
            union.append(b[j])
            j= j+1
        else:
            union.append(a[i])      
            i=i+1
            j=j+1

    while i < n:
        if i == 0 or a[i] != a[i - 1]:
            union.append(a[i])
        i += 1
    while j < m:
        if j == 0 or b[j] != b[j - 1]:
            union.append(b[j])
        j+=1
        
    return union

    pass
