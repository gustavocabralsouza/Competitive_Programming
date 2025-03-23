from typing import List

class Solution:
    def twoSum_hashMapOne(self, nums: List[int], target: int) -> List[int]:
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num  
            if complement in seen:
                return [seen[complement], i]  
            seen[num] = i 
        return []  
    
    def twoSum_bruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                soma = nums[i] + nums[j]
                if soma == target and i<j:
                    return [i, j]
    def twoSum_hashmapTwo(self, nums: List[int], target: int) -> List[int]:
        dic = {} 
        for idx, i in enumerate(nums):  
            if dic.get(i) is not None:
                return[dic.get(i), idx]
            dic[target - i] = idx
        return None
    
  

if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum_hashmapTwo([3, 2, 4], 6)
    print(result)  # Output: [1, 2] (2 + 4 = 6)
