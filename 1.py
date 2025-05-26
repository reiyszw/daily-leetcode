class Solution(object):
    def twoSum(self, nums, target):
        pair_dict = {}

        for i, n in enumerate(nums):
            target_num = target - n

            if target_num in pair_dict:
                return [pair_dict[target_num], i]

            pair_dict[n] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9     
    solution = Solution()
    print(solution.twoSum(nums, target))            