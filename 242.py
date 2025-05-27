from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        hash_map = defaultdict()

        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1

        for c in t:
            if c not in hash_map:
                return False
            if c in hash_map:
                hash_map[c] -= 1
                if (hash_map[c] == 0):
                    hash_map.pop(c)
        return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))            