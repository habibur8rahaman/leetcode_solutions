class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        else:
            hashMap = {} #element: index

            for i, n in enumerate(nums):
                diff = target - n
                if diff in hashMap:
                    return [hashMap[diff], i]
                hashMap[n] = i  

