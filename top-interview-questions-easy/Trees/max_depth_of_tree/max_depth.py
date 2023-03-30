#!/usr/bin/python3

class Node:
    def __init__(self, data: int = None) -> None:
        self.data = data
        self.left = None
        self.right = None

    
class Tree:
    def __init__(self) -> None:
        self.root = None

    def addNode(self, data: int):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            parent = None

            while True:
                parent = current_node
                if data < current_node.data:
                    current_node = current_node.left

                    if current_node is None:
                        parent.left = new_node
                        return
                else:
                    current_node = current_node.right

                    if current_node is None:
                        parent.right = new_node
                        return
    
    def preOrderTraversal(self, head):
        if head is not None:
            print(head.data, end=" ")
            self.preOrderTraversal(head.left)
            self.preOrderTraversal(head.right)

tree = Tree()
tree.addNode(50)
tree.addNode(25)
tree.addNode(75)
tree.addNode(12)
tree.addNode(37)
tree.addNode(43)
tree.addNode(30)
tree.preOrderTraversal(tree.root)

