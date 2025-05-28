# expand(i, i) と expand(i, i+1) の2つのケースに分ける理由は、回文（palindrome）には「奇数長」と「偶数長」があるからです。
# 中心から左右に広げていくというのがキー

class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        result = ""
        for i in range(len(s)):
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2
        return result

if __name__ == '__main__':
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))            