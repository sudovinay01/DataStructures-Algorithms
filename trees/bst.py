from nodes.node import Node_V3
from trees.tree import Tree
from algorithms_base.options_error import OptionNotFound

import re

class BST(Tree):
    def __init__(self, type="BST"):
        super().__init__(type)

    def _insert_iteration(self, data):
        """
        Iterative version of BST insertion
        """
        ant, parent_ant = self.root, None
        while ant:
            parent_ant = ant
            if data < ant.data[0]:
                ant = ant.left
            elif data > ant.data[0]:
                ant = ant.right
            else:
                ant = ant.left
                break
        
        if data < parent_ant.data[0]:
            parent_ant.left = Node_V3(data)
        elif data > parent_ant.data[0]:
            parent_ant.right = Node_V3(data)
        else:
            parent_ant.data.append(data)
    
    def _insert_recursion(self, item, data):
        """
        Recursive version BST insertion.
        """
        if data < item.data[0]:
            if not item.left:
                item.left = Node_V3(data)
            else:
                self._insert_recursion(item.left, data)
        elif data > item.data[0]:
            if not item.right:
                item.right = Node_V3(data)
            else:
                self._insert_recursion(item.right, data)
        else:
            item.data.append(data)

    def insert(self, data, how="recursion"):
        """
        BST insertion
        Time Complexity : O(n), θ(logn)
        Space Complexity : O(1)
        """
        self.n_elements+=1
        try:
            if not self.root:
                self.root = Node_V3(data)
                return

            if re.fullmatch(r"(iteration|i)", how, re.IGNORECASE):
                return self._insert_iteration(data)
            if re.fullmatch(r"(recursion|r)", how, re.IGNORECASE):
                return self._insert_recursion(self.root, data)
            raise OptionNotFound(f"Not a right choice, please select the right choice. \
                                 The possible values of how can be any of four values \
                                 from recursion, r, iteration, i")
        except OptionNotFound as onf:
            print(onf)
            self.n_elements-=1
        except Exception as e:
            print(e)
            self.n_elements-=1

    def __search_recursion(self, item, key):
        """
        Recursive version BST search operation
        """
        # Key not found.
        if not item:
            return None
        
        # Check further
        if key < item.data[0]:
            return self.__search_recursion(item.left, key)
        elif key > item.data[0]:
            return self.__search_recursion(item.right, key)
        else:
            # Key found
            return item

    def __search_iteration(self, key):
        """
        Iterative version of BST search
        """
        item = self.root
        while not item:
            if key<item.data[0]:
                item = item.left
            elif key>item.data[0]:
                item = item.right
            else:
                return item
        return None
    
    def search(self, key, how="recursion"):
        """
        BST search
        Time Complexity : O(n)
        Space Complexity : {O(n), θ(log(n))} ---> recursion, θ(1) ---> iteration
        """
        # BST is empty
        if not self.root:
            print(f"{self.type} is empty...")
            return None
        
        try:
            if re.fullmatch(r"(recursion|r)", how, re.IGNORECASE):
                return self.__search_recursion(self.root, key)
            if re.fullmatch(r"(iteration|i)", how, re.IGNORECASE):
                return self.__search_iteration(key)
            raise OptionNotFound(f"Not a right choice, please select the right choice. \
                                 The possible values of how can be any of four values \
                                 from recursion, r, iteration, i")
        except OptionNotFound as onf:
            print(onf)
            return None

    def __delete_key(self, p, c):
        """
        Support code for __delete_iteration method
        """
        # If the element that needs to be deleted is a leaf node
        if not c.left and not c.right:
            if not p:
                self.root = None
            elif p.left == c:
                p.left = None
            else:
                p.right = None
        # If the element don't has right child
        elif not c.right:
            if not p:
                self.root = c.left
            elif p.left == c:
                p.left = c.left
            else:
                p.right = c.left
        # If the element has right child
        else:
            p = c
            c = c.right
            memory_ant = None
            while c.left:
                memory_ant = c
                c = c.left

            # Replacing the element with the inorder successor
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
            if key < ant.data[0]:
                parent_ant = ant
                ant = ant.left
            elif key > ant.data[0]:
                parent_ant = ant
                ant = ant.right
            else:
                self.n_elements-=1
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
        
        if key < child.data[0]:
            self.__delete_recursion(child, child.left, key)
        elif key > child.data[0]:
            self.__delete_recursion(child, child.right, key)
        else:
            self.n_elements-=1
            self.__delete_key(parent, child)

    def delete(self, key, how="recursion"):
        """
        BST deletion
        Time Complexity : O(n)
        Space Complexity : {O(n), θ(log(n))} ---> recursion, θ(1) ---> iteration
        """
        if not self.root:
            print(f"BST is empty")
            return
        try:
            if re.fullmatch(r"(iteration|i)", how, re.IGNORECASE):
                return self.__delete_iteration(key)
            if re.fullmatch(r"(recursion|r)", how, re.IGNORECASE):
                return self.__delete_recursion(None, self.root, key)
            raise OptionNotFound(f"Not a right choice, please select the right choice. \
                                 The possible values of how can be any of four values \
                                 from recursion, r, iteration, i")
        except OptionNotFound as onf:
            print(onf)
        except Exception as e:
            print("Deletion unsuccessfull...", e)

    def show_bst(self, how="inorder"):
        super().show_tree(how)