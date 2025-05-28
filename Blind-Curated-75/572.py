class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
            self.sameTree(root.right, subRoot.right))        
        return False

if __name__ == '__main__':
     # root tree
    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(1)
    node4 = TreeNode(2)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    root = node1

    # subRoot tree
    s1 = TreeNode(4)
    s2 = TreeNode(1)
    s3 = TreeNode(2)
    s1.left = s2
    s1.right = s3
    subRoot = s1

    solution = Solution()
    print(solution.isSubtree(root, subRoot))            