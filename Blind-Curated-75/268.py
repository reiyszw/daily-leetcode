# 式 n * (n + 1) // 2 は
#「0からnまでのすべての数を足した合計」を高速に求める公式。
# その差分で「欠けている1つの数字」が一発でわかる

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        excepted = n * (n + 1) // 2
        actual = sum(nums)
        return excepted - actual

if __name__ == '__main__':
    nums = [3,0,1]
    solution = Solution()
    print(solution.missingNumber(nums))            