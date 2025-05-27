# 「ダミーノード」を最初に1つ用意しておくと、headの扱いが楽になる
# tail は常に「現在の最後のノード」を指します。
# 新しいノードを tail.next = 新しいノード として追加し、そのあと tail = tail.next と進めます。
# dummy自体はダミーで中身は意味がないので、実際のリストの先頭は dummy.next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2
        return dummy.next
        
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    node4.next = node5
    node5.next = node6

    list1 = node1
    list2 = node4
    solution = Solution()
    print(solution.mergeTwoLists(node1, node4))            