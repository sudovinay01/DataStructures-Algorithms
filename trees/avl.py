from nodes.node import Node_V4
from stacks.stack import Stack
from trees.bst import BST

import math

class AVL(BST):
    def __init__(self):
        super().__init__(type="AVL")
    
    def __left_rotate(self, across_point:Node_V4|None):
        """
        Left rotates the AVL tree across across_point while preserving BST property
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        x = across_point.right
        x_left_branch = x.left
        x.left = across_point
        across_point.right = x_left_branch
        if self.root == across_point:
            self.root = x
        across_point.height = 1 + max(self.__get_height(across_point.left), self.__get_height(across_point.right))
        x.height = 1 + max(self.__get_height(x.left), self.__get_height(x.right))
        return x

    def __right_rotate(self, across_point:Node_V4|None):
        """
        Right rotates the AVL tree across across_point while preserving BST property
        Time Complexity : O(1)
        Space Complexity : O(1)
        """        
        x = across_point.left
        x_right_branch = x.right
        x.right = across_point
        across_point.left = x_right_branch
        if self.root == across_point:
            self.root = x
        across_point.height = 1 + max(self.__get_height(across_point.left), self.__get_height(across_point.right))
        x.height = 1 + max(self.__get_height(x.left), self.__get_height(x.right))
        return x
    
    def __get_height(self, node:Node_V4|None):
        """
        Utility function to get the height of the tree node
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if not node:
            return -1
        return node.height
    
    def __get_balance_factor(self, node: Node_V4|None):
        """
        Utility function to calculate and give the balance factor
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if not node:
            return 0
        return self.__get_height(node.left) - self.__get_height(node.right)
    
    def __adjust_parent(self, parent, after_rotate):
        """
        Utility function to attach the resultant tree after rotation
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if parent:
            if after_rotate.data[0] < parent.data[0]:
                parent.left = after_rotate
            else:
                parent.right = after_rotate
    
    def __balance_avl(self, data, insert_stack:Stack):
        """
        Utility function to balance the Tree after insertion
        Time Complexity : O(log(n))
        Space Complexity : O(1)
        """
        while not insert_stack.isEmpty():
            across_point = insert_stack.pop()
            across_point.height = 1 + max(self.__get_height(across_point.left), self.__get_height(across_point.right))
            bf = self.__get_balance_factor(across_point)
            if bf < -1 and data > across_point.right.data[0]:
                parent = insert_stack.peek()
                after_rotate = self.__left_rotate(across_point)
                self.__adjust_parent(parent, after_rotate)
            elif bf > 1 and data < across_point.left.data[0]:
                parent = insert_stack.peek()
                after_rotate = self.__right_rotate(across_point)
                self.__adjust_parent(parent, after_rotate)
            elif bf < -1 and data < across_point.right.data[0]:
                across_point.right = self.__right_rotate(across_point.right)
                parent = insert_stack.peek()
                after_rotate = self.__left_rotate(across_point)
                self.__adjust_parent(parent, after_rotate)
            elif bf > 1 and data > across_point.left.data[0]:
                across_point.left = self.__left_rotate(across_point.left)
                parent = insert_stack.peek()
                after_rotate = self.__right_rotate(across_point)
                self.__adjust_parent(parent, after_rotate)

    def _insert_iteration(self, data):
        """
        Iterative version of AVL insertion
        Time Complexity : O(logn)
        Space Complexity : O(logn)
        """
        insert_stack = Stack(2*math.ceil(math.log(self.n_elements)))
        ant, parent_ant = self.root, None
        while ant:
            parent_ant = ant
            if data < ant.data[0]:
                insert_stack.push(ant)
                ant = ant.left
            elif data > ant.data[0]:
                insert_stack.push(ant)
                ant = ant.right
            else:
                ant = ant.left
                break
        
        if data < parent_ant.data[0]:
            parent_ant.left = Node_V4(data)
        elif data > parent_ant.data[0]:
            parent_ant.right = Node_V4(data)
        else:
            parent_ant.data.append(data)
            return
        self.__balance_avl(data, insert_stack)
    
    def _insert_recursion(self, item, data):
        raise NotImplementedError(f"Recursive insertion is not implemented for {self.type} tree.")
    
    def _insert(self, data, how="iteration"):
        
        if not self.root:
            self.n_elements+=1
            self.root = Node_V4(data)
            return
        
        super()._insert(data, how)
    
    def _delete(self, key):
        raise NotImplementedError(f"Deletion is not implemented for {self.type} tree.")
    
    def _search(self, key, how="recursion"):
        return super()._search(key, how)

    def show_avl(self, how="inorder"):
        super().show_bst(how)