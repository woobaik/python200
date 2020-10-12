class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for index in range(len(nums)):

            for j in nums[index+1:]:

                if nums[index] == j:
                    result += 1

        return result
