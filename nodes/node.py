class Node_V1:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Node_V2(Node_V1):
    def __init__(self, data, prev=None, next=None):
        super().__init__(data, next)
        self.prev = prev

class Node_V3(Node_V1):
    def __init__(self, data, left=None, right=None):
        self.data = [data]
        self.left = left
        self.right = right

class Node_V4(Node_V3):
    def __init__(self, data, left=None, right=None, height=0):
        super().__init__(data, left, right)
        self.height = height
        