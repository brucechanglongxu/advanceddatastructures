# Given an array of N non-negative integers, task is to find the maximum size of a subarray such that the pairwise sum of the elements of this subarray
# is not divisible by a given integer, K. Also, print this subarray as well. If there are two or more subarrays that follow the above stated condition, 
# then print the first one from the left. 

# The naive approach would take O(n^4) time, where we iterate over all of the subarrays in our array. For each subarray S, we calculate the sum of all of
# the pairwise elements and check if each of them is divisible by k or not. 

class Solution:
  """
  Brute force approach to find the maximum subarray that satisfies the property
  """
  def subArrayDivbyK(arr : List[int], n, k) -> Bool:
    for i in range(len(arr)):
      for j in range(len(arr)):
        for k in range(i, j):
          for l in range(k, j):
            if (arr[k] + arr[l] % k == 0):
              return False
    return True
  
 # The more efficient solution 
 class EfficientSolution:
    """
    Efficient approach to find maximum subarray with hashmap
    """
    
