# Find the total number of subarrays whose sum is equal to k
# if the numbers within our array can only be positive then we could use two pointers
# otherwise we need to use the prefix sum approach

class Solution:
	"""
	We use a prefix sum and hashmap approach
	"""
	def subarrayDivByK(self, A:List[int], K: int) -> int:
		res = 0
		curSum = 0
		prefixSums = { 0 : 1 }

		for n in nums:
			curSum += n
			diff = curSum - k
			res += prefixSums.get(diff, 0)		
			prefixSums[diff] = 1 + prefixSums.get(curSum, 0)

		return res	
