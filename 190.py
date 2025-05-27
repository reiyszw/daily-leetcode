class Solution(object):
    def hammingWeight(self, n):
        binary = self.to_binary(n)
        count = 0
        
        for i in binary:
            if i == "1":
                count += 1
                
        return count

    def to_binary(self, n):
        if n == 0:
            return '0'
        
        bits = []
        while n > 0:
            bits.append(str(n % 2))
            n = n // 2
        
        return ''.join(reversed(bits))
        
if __name__ == '__main__':
    n = 11
    solution = Solution()
    print(solution.hammingWeight(n))            