# Given an array of N non-negative integers, task is to find the maximum size of a subarray such that the pairwise sum of the elements of this subarray
# is not divisible by a given integer, K. Also, print this subarray as well. If there are two or more subarrays that follow the above stated condition, 
# then print the first one from the left. 

# The naive approach would take O(n^4) time, where we iterate over all of the subarrays in our array. For each subarray S, we calculate the sum of all of
# the pairwise elements and check if each of them is divisible by k or not. 

class Solution:
	"""
        Brute force approach to find the maximum subarray that satisfies the property
        """
        def subArrayDivbyK(arr : List[int], n, k):
          for i in range(len(arr)):
            for j in range(len(arr)):
              for k in range(i, j):
                for l in range(k, j):
                  if (arr[k] + arr[l] % k == 0):
                    return False
          return True
  
# The more efficient solution 
# We will create an empty hash table and insert arr[0] % k into it
# We traverse the remaining elements and maintain a window such that no pair in the window 
# is divisible by k. 
class EfficientSolution:
 	"""
        Efficient approach to find maximum subarray with hashmap
    	"""
	def subarrayDivisibleByK(arr: List[int], n, k) -> Bool:
	# hash table to store the remainders obtained by dividing by K
		mp = [0] * 1000
		s = 0; e = 0; maxs = 0; maxe = 0;
		mp[arr[0] % k] = mp[arr[0] % k] + 1;
		for i in range(1, n):
			mod = arr[i] % k
			while (mp[k - mod] != 0 or (mod == 0
					   and mp[mod] != 0)) :
				mp[arr[s] % k] = mp[arr[s] & k] - 1
				s = s + 1
			# include the current element in the current subarray the 
			# ending index of the current subarray increments by one
			mp[mod] = mp[mod] + 1
			e = e + 1
			# compare the size of the current subarray with the maximum size
			# so far
			if ((e - s) > (maxe - maxs)) :
				maxe = e
				maxs = s
		print("The maximum size is {} and the subarray is as follows".format((maxe - maxs + 1)))
		for i in range(maxs, maxe + 1):
			print ("{} ".format(arr[i]), end="")
 
