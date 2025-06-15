from abc import abstractmethod, ABC
from algorithms_base.options_error import OptionNotFound
from queues.que import Q

import re
import math

class Tree(ABC):
    def __init__(self, type="TREE"):
        self.root = None
        self.n_elements = 0
        self.type = type
    
    @abstractmethod
    def _insert(self, data):
        pass

    @abstractmethod
    def _delete(self, key):
        pass
    
    @abstractmethod
    def _search(self, key):
        pass

    def __height_recursion(self, item):
        if not item:
            return -1
        
        if not item.left and not item.right:
            return 0
        
        return 1+ max(self.__height_recursion(item.left), self.__height_recursion(item.right))

    def __height_iteration(self, p):
        raise NotImplementedError(f"Height iteration is not implemented for {self.type} tree type.")

    def _height(self, how="recursion"):
        """
        This function finds the height of the tree
        Time Complexity : O(n)
        Space Complexity : O(n), θ(log(n))
        """
        if re.fullmatch(r"(iteration|i)", how, re.IGNORECASE):
            return self.__height_iteration(self.root)
        if re.fullmatch(r"(recursion|r)", how, re.IGNORECASE):
            return self.__height_recursion(self.root)
    
    def __inorder_traversal(self, p):
        """
        Tree Inorder traversal
        Time Complexity : O(n)
        Space Complexity : O(log(n))
        """
        if p:
            self.__inorder_traversal(p.left)
            if isinstance(p.data, list):
                for x in p.data:
                    print(x, end=",")
            else:
                print(p.data, end=",")
            self.__inorder_traversal(p.right)

    def __preorder_traversal(self, p):
        """
        Tree Preorder traversal
        Time Complexity : O(n)
        Space Complexity : O(log(n))
        """
        if p:
            if isinstance(p.data, list):
                for x in p.data:
                    print(x, end=",")
            else:
                print(p.data, end=",")
            self.__preorder_traversal(p.left)
            self.__preorder_traversal(p.right)
    
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

    def _show_tree(self, how="inorder"):
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
                self.__inorder_traversal(self.root)
            elif re.fullmatch(r"(preorder|pre)", how, re.IGNORECASE):
                self.__preorder_traversal(self.root)
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