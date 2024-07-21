# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def addChild(self, child):
        if child == self.val:
            return

        if child < self.val:
            if self.left:
                self.left.addChild(child)
            else:
                self.left = TreeNode(child)
        else:
            if self.right:
                self.right.addChild(child)
            else:
                self.right = TreeNode(child)

    def inorder(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.inorder()

        # visit base node
        elements.append(self.val)

        # visit right tree
        if self.right:
            elements += self.right.inorder()

        return elements


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ):

        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else:
                return curr


def buildTree(elements):
    root = TreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root


if __name__ == "__main__":
    numbers = [9, 8, 7, 2, 1, 3, 6, 12, 27]

    tree = buildTree(numbers)

    print(tree.inorder())

    p = TreeNode(1)
    q = TreeNode(6)

    s = Solution()
    lowest = s.lowestCommonAncestor(tree, p, q)
    if lowest:
        print(lowest.val)
    else:
        print("Lowest common ancestor not found.")
