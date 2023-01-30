class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def deleteNode(self, root, key):
        if not root:
            return None

        if root.val == key:
            if not root.right:
                return root.left

            if not root.left:
                return root.right

            if root.left and root.right:
                temp = root.right

                while temp.left:
                    temp = temp.left

                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


def buildTree(elements):
    root = TreeNode(elements[0])

    for i in range(1, len(elements)-1):
        root.addChild(elements[i])

    return root


if __name__ == "__main__":
    numbers = [5, 8, 7, 2, 1, 3, 6]

    tree = buildTree(numbers)

    print(tree.inorder())
    tree.deleteNode(tree, 2)
    print(tree.inorder())
