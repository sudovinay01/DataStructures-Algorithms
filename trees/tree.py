from abc import abstractmethod, ABC
from algorithms_base.options_error import OptionNotFound
from queues.que import Q
from stacks.stack import Stack
import math

import re
import math

class Tree(ABC):
    def __init__(self, type="TREE"):
        self.root = None
        self.n_elements = 0
        self.type = type
    
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def delete(self, key):
        pass
    
    @abstractmethod
    def search(self, key):
        pass

    def __height_recursion(self, item):
        if not item:
            return -1
        
        if not item.left and not item.right:
            return 0
        
        return 1+ max(self.__height_recursion(item.left), self.__height_recursion(item.right))

    def __height_iteration(self, p):
        raise NotImplementedError(f"Height iteration is not implemented for {self.type} tree type.")

    def height(self, how="recursion"):
        """
        This function finds the height of the tree
        Time Complexity : O(n)
        Space Complexity : O(n), θ(log(n))
        """
        if re.fullmatch(r"(iteration|i)", how, re.IGNORECASE):
            return self.__height_iteration(self.root)
        if re.fullmatch(r"(recursion|r)", how, re.IGNORECASE):
            return self.__height_recursion(self.root)
    
    def __inorder_traversal_recursion(self, p):
        """
        Tree Inorder traversal recursive version
        Time Complexity : O(n)
        Space Complexity : O(log(n))
        """
        if p:
            self.__inorder_traversal_recursion(p.left)
            if isinstance(p.data, list):
                for x in p.data:
                    print(x, end=",")
            else:
                print(p.data, end=",")
            self.__inorder_traversal_recursion(p.right)

    def __inorder_traversal_iteration(self):
        """
        Tree Inorder traversal iterative
        Time Complexity : O(n)
        Space Complexity : O(log(n))
        """
        inorder_stack = Stack(math.ceil(math.log2(self.n_elements)+1))
        temp = self.root
        while temp or not inorder_stack.isEmpty():
            if temp:
                inorder_stack.push(temp)
                temp = temp.left
            else:
                temp = inorder_stack.pop()
                if isinstance(temp.data, list):
                    for x in temp.data:
                        print(x, end=",")
                else:
                    print(temp.data, end=",")
                temp = temp.right

    def __preorder_traversal_recursion(self, p):
        """
        Tree Preorder traversal recursive version
        Time Complexity : O(n)
        Space Complexity : O(log(n))
        """
        if p:
            if isinstance(p.data, list):
                for x in p.data:
                    print(x, end=",")
            else:
                print(p.data, end=",")
            self.__preorder_traversal_recursion(p.left)
            self.__preorder_traversal_recursion(p.right)
    
    def __preorder_traversal_iteration(self):
        """
        Tree Preorder traversal iterative version
        Time Complexity : O(n)
        Space Complexity : O(log(n))
        """
        preorder_stack = Stack(math.ceil(math.log2(self.n_elements)+1))
        temp = self.root
        while temp or not preorder_stack.isEmpty():
            if temp:
                if isinstance(temp.data, list):
                    for x in temp.data:
                        print(x, end=",")
                else:
                    print(temp.data, end=",")
                if temp.right:
                    preorder_stack.push(temp.right)
                temp = temp.left
            else:
                temp = preorder_stack.pop()

    def __postorder_traversal(self, p):
        """
        Tree Postorder traversal
        Time Complexity : O(n)
        Space Complexity : θ(log(n)), O(n)
        """
        if p:
            self.__postorder_traversal(p.left)
            self.__postorder_traversal(p.right)
            if isinstance(p.data, list):
                for x in p.data:
                    print(x, end=",")
            else:
                print(p.data, end=",")

    def __levelorder_traversal(self, p):
        """
        Tree Levelorder traversal
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        items_q = Q(math.ceil(self.n_elements/2))
        items_q.enqueue(p)
        while not items_q.isEmpty():
            item = items_q.dequeue()
            if item.left:
                items_q.enqueue(item.left)
            if item.right:
                items_q.enqueue(item.right)
            if isinstance(item.data, list):
                for x in item.data:
                    print(x, end=",")
            else:
                print(item.data, end=",")

    def show_tree(self, how="inorder", algo="iteration"):
        """
        Tree traversals
        Time Complexity : O(n)
        Space Complexity : O(log(n))
        """
        if not self.root:
            print(f"{self.type} is empty...")
            return
        
        try:
            print(f"Current {self.type} : ")
            if re.fullmatch(r"(inorder|in)", how, re.IGNORECASE):
                if re.fullmatch(r"(iteration|i)", algo, re.IGNORECASE):
                    return self.__inorder_traversal_iteration()
                if re.fullmatch(r"(recursion|r)", algo, re.IGNORECASE):
                    return self.__inorder_traversal_recursion(self.root)
                raise OptionNotFound("Not a right choice, please select the right choice. \
                                 The possible values of algo can be any of four values \
                                 from recursion, r, iteration, i")
            elif re.fullmatch(r"(preorder|pre)", how, re.IGNORECASE):
                if re.fullmatch(r"(iteration|i)", algo, re.IGNORECASE):
                    return self.__preorder_traversal_iteration()
                if re.fullmatch(r"(recursion|r)", algo, re.IGNORECASE):
                    return self.__preorder_traversal_recursion(self.root)
                raise OptionNotFound("Not a right choice, please select the right choice. \
                                 The possible values of algo can be any of four values \
                                 from recursion, r, iteration, i")
            elif re.fullmatch(r"(postorder|post)", how, re.IGNORECASE):
                self.__postorder_traversal(self.root)
            elif re.fullmatch(r"(levelorder|level)", how, re.IGNORECASE):
                self.__levelorder_traversal(self.root)
            else:
                raise OptionNotFound(f"Not a right choice, please select the right choice. \
                                 The possible values of how can be any of four values \
                                 from preorder, pre, inorder, in, postorder, post, levelorder, level")
        except OptionNotFound as onf:
            print(onf)
        except Exception as e:
            print("Traversal unsuccessfull...", e)
        finally:
            print()