class Solution(object):
    def firstBadVersion(self, n):
        lt = 1
        rt = n
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if isBadVersion(mid):
                rt = mid - 1
            else:
                lt = mid + 1
        return rt + 1
