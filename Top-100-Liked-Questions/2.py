class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    l1 = node1
    l2 = node4
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))            