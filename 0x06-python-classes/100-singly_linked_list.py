#!/usr/bin/python3
"""Singly Linked List"""


class Node:
    """Defines a node of singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes the node of the linked list"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets the value of the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """validates and sets the value for data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """validates and sets the value of the next node"""
        if  value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initializes the singly linked list"""
        self.__head = None
    
    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
        in the list (increasing order)
        """
        node = Node(value)
        if self.__head is None or value < self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            curr = self.__head
            while (curr.next_node is not None and
                   curr.next_node.data < value):
                curr = curr.next_node
            node.next_node = curr.next_node
            curr.next_node = node
            
    def __str__(self):
        """
        String representation of the list (one node per line)
        """
        values = []
        curr = self.__head
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(values)
