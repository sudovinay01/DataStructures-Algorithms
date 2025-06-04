class Node_V1:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Node_V2(Node_V1):
    def __init__(self, data, prev, next):
        super().__init__(data, next)
        self.prev = prev