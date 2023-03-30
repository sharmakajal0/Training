#!/usr/bin/python3

COUNT = [3]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value is already present in the tree")
    
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
        
    
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
    
    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)
    
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False
    
    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._search(value, cur_node.right)
        return False

    def print_in_2D(self, cur_root, space):
        if cur_root == None:
            return
        
        space += COUNT[0]
        self.print_in_2D(cur_root.right, space)

        for i in range(COUNT[0], space):
            print(end = " ")
        print(cur_root.value)

        self.print_in_2D(cur_root.left, space)
    
    def print2D(self):
        self.print_in_2D(self.root, 0)


def fill_tree(tree, num_elements = 10, max_int=100):
    from random import randint
    for _ in range(num_elements):
        cur_ele = randint(0, max_int)
        tree.insert(cur_ele)
    return tree

tree = binary_search_tree()
tree.insert(5)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)

#tree = fill_tree(tree)
# tree.print2D()
# tree.print_tree()
print("Tree Height: ", tree.height())
print(tree.search(10))
print(tree.search(6))