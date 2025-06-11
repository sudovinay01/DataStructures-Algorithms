from nodes.node import Node_V3
from algorithms_base.options_error import OptionNotFound
import re
class BST:
    def __init__(self):
        self.root = None

    def __insert_iteration(self, data):
        """
        Iterative version of BST insertion
        """
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
    
    def __insert_recursion(self, item, data):
        """
        Recursive version BST insertion.
        """
        if data <= item.data:
            if not item.left:
                item.left = Node_V3(data)
            else:
                self.__insert_recursion(item.left, data)
        elif data > item.data:
            if not item.right:
                item.right = Node_V3(data)
            else:
                self.__insert_recursion(item.right, data)

    def _insert(self, data, how="recursion"):
        """
        BST insertion
        Time Complexity : O(n), θ(logn)
        Space Complexity : O(1)
        """
        if not self.root:
            self.root = Node_V3(data)
            return

        if re.fullmatch(r"(iteration|i)", how, re.IGNORECASE):
            return self.__insert_iteration(data)
        if re.fullmatch(r"(recursion|r)", how, re.IGNORECASE):
            return self.__insert_recursion(self.root, data)

    def __delete_key(self, p, c):
        """
        Support code for __delete_iteration method
        """
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
    
    def __delete_iteration(self, key):
        """
        Iterative version of BST deletion
        """
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

    def __delete_recursion(self, parent, child, key):
        """
        Recursive version of BST deletion
        """
        if not child:
            print(f"Key : {key} not found")
            return
        
        if key < child.data:
            self.__delete_recursion(child, child.left, key)
        elif key > child.data:
            self.__delete_recursion(child, child.right, key)
        else:
            # If the element that needs to be deleted is a leaf node
            if not child.left and not child.right:
                if not parent:
                    self.root = None
                elif parent.left == child:
                    parent.left = None
                else:
                    parent.right = None
            # If the element don't has right child
            elif not child.right:
                if not parent:
                    self.root = child.left
                elif parent.left == child:
                    parent.left = child.left
                else:
                    parent.right = child.left
                return
            # If the element has right child
            else:
                parent = child
                memory = None
                child = child.right
                while child.left:
                    memory = child
                    child = child.left
                if not memory:
                    parent.data = child.data
                    parent.right = child.right
                else:
                    parent.data = child.data
                    memory.left = None if not child.right else child.right

    def _delete(self, key, how="recursion"):
        """
        BST deletion
        Time Complexity : O(n), θ(logn)
        Space Complexity : O(1)
        """
        if not self.root:
            print(f"BST is empty")
            return
        
        if re.fullmatch(r"(iteration|i)", how, re.IGNORECASE):
            return self.__delete_iteration(key)
        if re.fullmatch(r"(recursion|r)", how, re.IGNORECASE):
            return self.__delete_recursion(None, self.root, key) 
    
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
        if not self.root:
            print(f"BST is empty...")
            return
        
        try:
            print(f"Current BST : ")
            if re.fullmatch(r"(inorder|in)", how, re.IGNORECASE):
                self.__inorder_traversal(self.root)
            elif re.fullmatch(r"(preorder|pre)", how, re.IGNORECASE):
                self.__preorder_traversal(self.root)
            elif re.fullmatch(r"(postorder|post)", how, re.IGNORECASE):
                self.__postorder_traversal(self.root)
            else:
                raise OptionNotFound(f"Not a right choice please correct the how = {how}")
        except OptionNotFound as onf:
            print(onf)
        finally:
            print()
