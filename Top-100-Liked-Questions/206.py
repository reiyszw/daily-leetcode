# temp でcur.next を一時保存（つなぎ替える前に残しておく）
# cur は None になる（末尾まで到達）
# prev は反転されたリストの新しい先頭を指している

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    print(solution.reverseList(node1))            