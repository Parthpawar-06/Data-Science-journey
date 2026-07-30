# Question Link : https://www.geeksforgeeks.org/problems/second-largest3735/1

# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.
# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

#Solution :

class Solution:
    def getSecondLargest(self, arr):
        # code here
        ans = sorted(arr)
        n = len(arr)
        maxx = ans[n-1]
        second_largest = -1
        for i in range(n-2,-1,-1):
            if maxx==ans[i]:
                continue
            if maxx>ans[i]:
                return ans[i]
            
        return second_largest


# Optimised Solution, Time Complexity : O(n) :

class Solution:
    def getSecondLargest(self, arr):
        # code here
        l = -1
        sl = -1
        n = len(arr)
        
        for i in range(0,n):
            if (arr[i]>l):
                sl = l
                l = arr[i]
          
            elif (arr[i]>sl and l!=arr[i]):    
                sl = arr[i]
              
        return sl
