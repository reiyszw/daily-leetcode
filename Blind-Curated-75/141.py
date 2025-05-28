# slow, fastは必ずどこかで重なるという概念が大事
# ポインタはノード単位だから必ず同じ位置で衝突する
# なぜ while fast and fast.next なのか → Nullチェックが重要
# fast で Nullチェックを行えば slow で行う必要はない、内包している

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    pos = 1
    solution = Solution()
    print(solution.hasCycle(node1))            