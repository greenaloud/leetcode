class Solution(object):
    def searchInsert(self, nums, target):
        lt = 0
        rt = len(nums) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if target < nums[mid]:
                rt = mid - 1
            elif target > nums[mid]:
                lt = mid + 1
            else:
                return mid
        return lt
