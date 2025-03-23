from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dicionário para armazenar os números e seus índices(hashmap)
        for i, num in enumerate(nums):
            complement = target - num  # Complemento que falta para atingir o target
            if complement in seen:
                return [seen[complement], i]  # Retorna os índices
            seen[num] = i  # Armazena o número e seu índice
        return []  # Caso não haja solução
    
    def twoSum_mine(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                soma = nums[i] + nums[j]
                if soma == target and i<j:
                    return [i, j]
             
        return None
    
  

if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum_mine([3, 2, 4], 5)
    print(result)  # Esperado: [1, 2] (2 + 4 = 6)
