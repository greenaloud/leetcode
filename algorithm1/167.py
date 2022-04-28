class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = dict()
        for i, x in enumerate(numbers):
            memo[x] = i + 1
        for i, x in enumerate(numbers):
            comp = target - x
            print(x, comp)
            if comp in memo:
                return [i + 1, memo[comp]]
        return []