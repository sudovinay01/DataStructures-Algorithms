from nodes.node import Node_V3
class BST:
    def __init__(self):
        self.root = None
    
    def _insert(self, data):
        """
        BST insertion
        Time Complexity : O(n), θ(logn)
        Space Complexity : O(1)
        """
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

    def __delete_key(self, p, c):
        # If key is a leaf node
        if not c.left and not c.right:
            if not p:
                self.root = None
            elif p.left == c:
                p.left = None
            else:
                p.right = None
            return
        
        # If ant.right is None that means we donot need to find
        # the element that needs to be replaced with the node 
        # that needs to be deleted
        if not c.right:
            if not p:
                self.root = c.left
            elif p.left == c:
                p.left = c.left
            else:
                p.right = c.left
            return

        # If ant.right is not None then the code comes to this part
        # Now the element that needs to be replaced with the data that
        # needs to be deleted needs to be found out
        p = c
        c = c.right
        memory_ant = None
        while c.left:
            memory_ant = c
            c = c.left

        # Replacing the element that needs to be deleted with the right element
        if not memory_ant:
            p.data = c.data
            p.right = c.right
        else:
            p.data = c.data
            memory_ant.left = None if not c.right else c.right
    
    def _delete(self, key):
        """
        BST deletion
        Time Complexity : O(n), θ(logn)
        Space Complexity : O(1)
        """
        if not self.root:
            print(f"BST is empty")
            return
        
        # Finding the key that need to be deleted...
        parent_ant = None
        ant = self.root
        while ant:
            if key < ant.data:
                parent_ant = ant
                ant = ant.left
            elif key > ant.data:
                parent_ant = ant
                ant = ant.right
            else:
                return self.__delete_key(parent_ant, ant)
        
        # If key not found
        print(f"{key} not found")
    
    def __inorder_traversal(self, p):
        """
        BST Inorder traversal
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        if p:
            self.__inorder_traversal(p.left)
            print(p.data, end=",")
            self.__inorder_traversal(p.right)

    def __preorder_traversal(self, p):
        """
        BST Preorder traversal
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        if p:
            print(p.data, end=",")
            self.__preorder_traversal(p.left)
            self.__preorder_traversal(p.right)
    
    def __postorder_traversal(self, p):
        """
        BST Post traversal
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        if p:
            self.__postorder_traversal(p.left)
            self.__postorder_traversal(p.right)
            print(p.data, end=",")
    
    def _show_bst(self, how="inorder"):
        """
        BST traversals
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        print(f"Current BST : ")
        if how == "inorder":
            self.__inorder_traversal(self.root)
        elif how == "preorder":
            self.__preorder_traversal(self.root)
        else:
            self.__postorder_traversal(self.root)
        print()
