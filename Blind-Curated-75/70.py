# n段目に行く経路のすべては「n-1から来た経路」＋「n-2から来た経路」
# 通り数は「それぞれの数を数えて、合計すればOK」

class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b

        return b

if __name__ == '__main__':
    n = 2
    solution = Solution()
    print(solution.climbStairs(n))            