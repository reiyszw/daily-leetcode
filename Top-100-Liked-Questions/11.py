# 高さが上がる可能性がある
# 幅は狭くなるけど、min(height[l], height[r]) が上がれば「面積」が増える可能性がある
# このアルゴリズムの核心は「改善の可能性がある方だけ動かす」という貪欲法の発想

class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0

        while l <= r:
            width = r - l
            min_height = min(height[l], height[r])
            max_area = max(max_area, width * min_height)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(height))            