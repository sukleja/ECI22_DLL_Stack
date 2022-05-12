'''
Examples of a SLL, DLL, Stack and Queue implementations in Python

Class for holding the data, only the list will interact with the class and its object
nothing else will create a new node - > encapsulation'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


'''Class for managing the SLL'''
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        '''Here we create a node object with the given data, only our list creates this objects'''
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1 #always update the size to prevent costly iteration to get the size

    '''This function defines an iteration logic to iterate over our list items
    if we iterate over the list, this function will return us the data from the nodes, so we never 
    have to access the nodes directly'''
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size



#############################################################################################
# Exercise Part #############################################################################

    def clear(self):
        '''Deleting the head removes every reference to every other node, because we have
        no head anymore to start iterating. The list becomes effectively empty'''
        self.head = None
        self.size = 0

    def get_data(self, data):
        '''thanks to our __iter__ function we can iterate over the list
        and return the data directly'''
        for node in self:
            if node == data:
                return data
        return False

    def delete(self, data):
        current = self.head
        prev = self.head #temp variable for remembering the previous element

        while current:
            if current.data == data:
                if current == self.head:
                    '''if the element is the head, we simply remove the head by assigning it 
                    to the next element'''
                    self.head = current.next
                    self.size -= 1
                else:
                    '''if we found the element, we change the pointers, the previous element now points
                    to the element after the deleted one, now there is nothing pointing to the deleted
                    element'''
                    prev.next = current.next
                self.size -= 1
                return
            '''here update our temporary variables for the iteration'''
            prev = current
            current = current.next

'''DLL Implementiation'''
class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.prev = None #now we need a pointer to the previous element
        self.next = None


# Class for managing the list and the head
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #initializing a tail element will speed up deleting head and tail positions
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the list is empty, the new node is the head
            self.head = node
            self.tail = self.head
        else:  # if not empty append the new node directly to tail (exchange with old tail)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    #the iteration function is the same generator function like in the SLL
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size



#############################################################################################
# Exercise Part #############################################################################

    def clear(self):
        self.head = None #clearing works exactly the same
        self.size = 0

    def get_data(self, data):
        for node in self:
            if node == data:
                return data
        return False

    def delete(self, data):
        current = self.head

        '''if the element is at head or tail position we can simply jump there'''
        if current.data == data:
            self.head = current.next
            self.head.prev = None #we now have to consider the previous pointer
            self.size -= 1
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        else:
            while current:
                if current.data == data:
                    '''the next pointer of the previous element now points to the element after
                    the deleted one'''
                    current.prev.next = current.next
                    '''the previous pointer of the element after the deleted one, now points to the
                    element before the deleted one'''
                    current.next.prev = current.prev
                    self.size -= 1
                current = current.next
#5
class MyStack:

    stack = []

    '''We simply use a list to realize the stack, we just have to keep track of the correct order
    of insert and delete operations'''
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        element = self.stack[-1] #we always take the last element
        self.stack.remove(element)
        return element

    def top(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

#queue implementation from right to left
class MyQueue:

    queue = []
    '''The queue works identical just with a different order of operations'''
    def push(self,element):
        self.queue.append(element)

    def pop(self):
        element = self.queue[0] #we always want the first element
        self.queue.remove(element)
        return element

    def show_left(self):
        return self.queue[0]

    def show_right(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)


'''Code for testing the Classes'''

my_list = SinglyLinkedList()
my_list.append('first')
my_list.append("second")
my_list.append("third")
print(my_list.get_size())
my_list.delete("second")
print(my_list.get_size())
print(my_list)



