# temp でcur.next を一時保存（つなぎ替える前に残しておく）
# cur は None になる（末尾まで到達）
# prev は反転されたリストの新しい先頭を指している

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution = Solution()
    print(solution.isPalindrome(node1))            