from tkinter import N


class LinkedList:
    def __init__(self):
        self.firstNode = None

    def traverseList(self):
        """
        This function is used to go trough all the elements 
        of the linkedList

        1. We start with the first node
        2. We look at the pointer of this node
        3. If it's null we stop, else we go to the next node

        Time complexity is O(N)
        """
        if self.firstNode is None:
            print("there's no element in the list")
            return
        else:
            n = self.firstNode
            while n is not None:
                print(n.data, " ")
                n = n.nextNode

    def addFirst(self, node):
        """
        This function is used to add a node at the first position of the linked list

        1. if the list is empty, we just add the node
        2. else we use the actual first node as the pointer reference and then we add the node

        Time complexity is O(1)
        """
        if self.firstNode is None:
            self.firstNode = node
        else:
            node.nextNode = self.firstNode
            self.firstNode = node

    def addLast(self, node):
        """
        This function is used to add a node at the last element of the linkedList

        1. if the list is empty, we simply add the node
        2. else we go trough all the elements and then add the node

        Time complexity is O(N)
        """
        if self.firstNode is None:
            self.firstNode = node
        else:
            n = self.firstNode
            while(n.nextNode is not None):
                n = n.nextNode
            n.nextNode = node

    def deleteFirst(self):
        """
        This function is used to delete the first node of the linkedList

        1. if the list is empty, we can't delete any node
        2. the list have more than 1 element, we delete the node
        3. the list only has one element
            - we delete the node and replace it with a None value 

        Time complexity is O(1)
        """
        if self.firstNode is None:
            print('The list is empty')
            return
        elif self.firstNode.nextNode is not None:
            nextNode = self.firstNode.nextNode
            del self.firstNode
            self.firstNode = nextNode

        else:
            nextNode = None
            del self.firstNode
            self.firstNode = None

    def deleteLast(self):
        """
        This function delete the last node of the linkedList

        1. If the list is empty, we can't delete any node
        2. If the list has more than 1 element
        3. if the list has only one element

        Time complexity is O(N) 

        """

        if self.firstNode is None:
            print("The list is empty")
        elif self.firstNode.nextNode is not None:
            n = self.firstNode
            while(n.nextNode.nextNode is not None):
                n = n.nextNode
            del n.nextNode
            n.nextNode = None
        else:
            self.firstNode = None

    def reverse(self):
        """
        This function is used to reverse the elements of the linkedList

        from A -> B -> C -> None
        to C -> B -> A -> None

        1. we intialise the prev, current and next pointers
        2. we link the current node to the prev pointer 
        3. we move the prev pointer to the current pointer position
        4. we move the current pointer to the next pointer position
        5. we move the next pointer to the current.next position
        finally, we set the head of the list to the previous pointer node
        """
        if self.firstNode is None:
            print("The linkedList is empty")
            return
        else:
            current = self.firstNode  # initial pointer
            previous = None  # initial pointer
            while(current is not None):
                nextNode = current.nextNode  # move next pointer
                current.nextNode = previous  # reverse the link
                previous = current  # move previous to curent
                current = nextNode  # move curent to next
            self.firstNode = previous  # head of the new list

    def addPosition(self, node, position):
        current = self.firstNode
        counter = 0
        if position == 0:
            self.addFirst(node)
            return
        while counter < position-1:
            if current is None:
                print('The position does not exist')
                return
            else:
                current = current.nextNode
                counter += 1
        node.nextNode = current.nextNode
        current.nextNode = node


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


linked = LinkedList()

A = Node("a")
B = Node("b")
C = Node("c")
D = Node("d")

linked.addLast(A)
linked.addLast(B)


linked.deleteLast()
linked.traverseList()
