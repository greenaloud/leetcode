class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        mul = 1
        while n:
            add += n % 10
            mul *= n % 10
            n //= 10
        return mul - add
