from nodes.node import Node_V3
class BST:
    def __init__(self):
        self.root = None
    
    def _insert(self, data):
        
        if not self.root:
            self.root = Node_V3(data)
            return
        
        ant, parent_ant = self.root, None
        while ant:
            parent_ant = ant
            if data < ant.data:
                ant = ant.left
            elif data > ant.data:
                ant = ant.right
            else:
                ant = ant.left
                break
        
        if data < parent_ant.data:
            parent_ant.left = Node_V3(data)
        elif data > parent_ant.data:
            parent_ant.right = Node_V3(data)
        else:
            new_ant = Node_V3(data)
            new_ant.left = ant
            parent_ant.left = new_ant 
    
    def _delete(self, key):
        """if not self.root:
            print(f"BST is empty")
            return
        
        parent_ant, ant = None, self.root
        while ant:
            parent_ant = ant
            if key < ant.data:
                ant = ant.left
            elif key > ant.data:
                ant = ant.right
            else:
                pass"""
        print("Not yet implemented")
        return
    
    def __inorder_traversal(self, p):
        if p:
            self.__inorder_traversal(p.left)
            print(p.data, end=",")
            self.__inorder_traversal(p.right)

    def __preorder_traversal(self, p):
        if p:
            print(p.data, end=",")
            self.__preorder_traversal(p.left)
            self.__preorder_traversal(p.right)
    
    def __postorder_traversal(self, p):
        if p:
            self.__postorder_traversal(p.left)
            self.__postorder_traversal(p.right)
            print(p.data, end=",")
    
    def show_bst(self, how="inorder"):
        print(f"Current BST : ")
        if how == "inorder":
            self.__inorder_traversal(self.root)
        elif how == "preorder":
            self.__preorder_traversal(self.root)
        else:
            self.__postorder_traversal(self.root)
