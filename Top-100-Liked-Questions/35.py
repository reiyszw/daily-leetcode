class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
            
        return l

if __name__ == '__main__':
    nums = [1,3,4,6]
    target = 5
    solution = Solution()
    print(solution.searchInsert(nums, target))            