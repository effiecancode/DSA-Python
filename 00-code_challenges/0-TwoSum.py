# Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int] list datatype
        :type target: int
        :rtype: List[int] new list
        """
        num_indices = {} #empty hash map to store numbers and their indices
        for index, num in enumerate(nums): #iterate
            match = target - num #do this at every index iterated

            if match in num_indices:
                return [num_indices[match], index] #found a solution return its indices
            else:
                num_indices[num] = index
        #if non found return an empty list
        return []


nums = [3, 4, 5, 6]
target = 10
instance = Solution()
result = instance.twoSum(nums, target)
print(result)

