class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def print_data(self):
        print(self.data)

newBST = BSTNode(None)
newBST.print_data()  
