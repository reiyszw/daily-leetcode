class Solution(object):
    def isValid(self, s):
        stack = []
        char_pairs = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in char_pairs:
                if stack and stack[-1] == char_pairs[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)

        return True if not stack else False

if __name__ == '__main__':
    s = "()"
    solution = Solution()
    print(solution.isValid(s))            