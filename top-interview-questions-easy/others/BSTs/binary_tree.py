#!/usr/bin/python3

COUNT = [5]

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

class BTree:
    def __init__(self):
        self.root = None
    
    def add_node(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if node.data < current.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return
    
    def inorder(self, current: Node):
        if current is not None:
            self.inorder(current.left)
            print(current.data)
            self.inorder(current.right)
        print()
    
    def postorder(self, current: Node):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data)
    
    def preorder(self, current: Node):
        if current is not None:
            print(current.data)
            self.preorder(current.left)
            self.preorder(current.right)

    def levelorder(self, root_node: Node):
        h = self.maxDepth(root_node)

        output = []

        for i in range(1, h + 1):
            self.currentlevel(root_node, i, output)
    
    def currentlevel(self, current_node: Node, level, output):
        current_values = []
        if current_node is None:
            return
        if level == 1:
            current_values.append(current_node.data)
        elif level > 1:
            self.currentlevel(current_node.left, level- 1)
            self.currentlevel(current_node.right, level - 1)
        output.append(current_values)
            

    def maxDepth(self, current: Node):
        if current is None:
            return 0
        else:
            lDepth = self.maxDepth(current.left)
            rDepth = self.maxDepth(current.right)

            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1

    def printTree(self, current, space):
        if current == None:
            return
        
        space += COUNT[0]

        self.printTree(current.right, space)
        for i in range(COUNT[0], space):
            print(end=" ")
        print(current.data)
        self.printTree(current.left, space)
    
    def printTwoD(self, current):
        self.printTree(current, 0)


    def isSymmetric(self, root_node: Node):
        return self.isMirror(root_node.left, root_node.right)

    def isMirror(self, leftroot: Node, rightroot: Node):
        if leftroot and rightroot:
            return leftroot.data == rightroot.data and self.isMirror(leftroot.left, rightroot.right) and self.isMirror(leftroot.right, rightroot.left)
        
        return leftroot == rightroot
        

tree = BTree()
for i in range(int(input())):
    tree.add_node(int(input()))

tree.levelorder(tree.root)
