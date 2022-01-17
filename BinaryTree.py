class BinaryTree:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, data):
        if self.value:
            if self.value > data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

    def PrintTreeInOrder(self):
        if self.left:
            self.left.PrintTreeInOrder()
        print(self.value),
        if self.right:
            self.right.PrintTreeInOrder()

    def PrintTreePreOrder(self):
        print(self.value)
        if self.left:
            self.left.PrintTreePreOrder()
        if self.right:
            self.right.PrintTreePreOrder()

    def PrintTreePostOrder(self):
        if self.left:
            self.left.PrintTreePostOrder()
        if self.right:
            self.right.PrintTreePostOrder()
        print(self.value)
        

root =BinaryTree(100)
root.insert(10)
root.insert(110)
root.insert(70)
root.PrintTreeInOrder()
root.PrintTreePostOrder()
root.PrintTreePreOrder()
