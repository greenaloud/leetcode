class Solution:
    def hammingWeight(self, n: int) -> int:
        comp = 1
        count = 0
        for _ in range(32):
            if n & comp:
                count += 1
            comp <<= 1
        return count
