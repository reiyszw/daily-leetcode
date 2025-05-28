class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()

        for n in nums:
            if n in hash_set:
                return True
            else:
                hash_set.add(n)
        return False

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    solution = Solution()
    print(solution.containsDuplicate(nums))            