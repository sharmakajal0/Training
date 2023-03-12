class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None

    def setData(self, data: int):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def listLength(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        current = self.head

        while current.getNext() != None:
            current = current.next

        current.setNext(newNode)
        self.length += 1

    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 0
                    current = self.head
                    while count < pos - 1:
                        count += 1
                        current = current.getNext()

                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length += 1

    def deleteFromBeginning(self):
        if self.length == 0:
            print("List is Empty")

        else:
            self.head = self.head.getNext()
            self.length -= 1

    def deleteFromEnd(self):
        if self.length == 0:
            print("List is Empty")

        current = self.head
        previous = self.head
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        previous.setNext(None)
        self.length -= 1

    def deleteWithNode(self, node):
        if self.length == 0:
            raise ValueError("List is Empty")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked list")
                else:
                    previous = current
                    current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1

    def deleteWithValue(self, value):
        currentNode = self.head
        previousNode = self.head

        while currentNode.next != None or currentNode.data != value:
            if currentNode.data == value:
                previousNode.next = currentNode.next
                self.length -= 1
                return
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()

        print("The value provided is not provided in the list")

    def deleteAtPos(self, pos):
        count = 0
        current = self.head
        previous = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist in the list")
        else:
            while current.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previous.next = current.next
                    self.length -= 1
                    return
                else:
                    previous = current
                    current = current.next

    def removeNthFromTheEnd(self, n: int):
        fast, slow = self.head, self.head
        for _ in range(n):
            if not fast:
                return self.head.next
            fast = fast.next

        if not fast:
            return self.head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

    def reverseList(self):
        prevNode = None
        current = self.head

        while (current is not None):
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode
        self.head = prevNode

    def printList(self):
        current = self.head
        while current != None:
            if current.getNext() != None:
                print(current.getData(), end="->")
            else:
                print(current.getData(), end="")
            current = current.getNext()
        print()
