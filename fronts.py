class Node(): # this are my nodes, the building blocks of our linked lists
    def __init__(self, value):
        self.value = value
        self.next= None

first_node = Node(5)
second_node = Node(10)
third_node = Node(15)

first_node.next = second_node
second_node.next = third_node

# print(first_node, "This is my node object")
# print(first_node.value,"This is the value my node contains")
# print(first_node.next.value, "This is what my node points to")

# Front
# Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.

class SLL(): #this is my linked list, where I can add, remove and replace nodes
    def __init__ (self, head): # my constructor -- if we need to create or organize data is better to have a head to pass data in here otherwise there is no point of instantiating a list. If we don't require a head we can say self.head= None
        self.head = head # linked list only requires one attribute -head because one link points to another and the rest follow

# Add Front
# Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

    def add_front(self,value):
        # self.head = Node(value)
        temp = self.head
        self.head = Node(value)
        self.head.next = temp

# new_singly_list = SLL(Node(1)) # I created a variable, inside of variable I invoked the SLL constructor and created a linked list object and I passed in a new node that contains the value 1 as my head node for my linked list. 
# print(new_singly_list.head.value, "before") #this returns the value at the head of the list
# new_singly_list.add_front(2)
# print(new_singly_list.head.value, "after") # new node created assigned as the list head

#display your list

    def display(self):
        runner = self.head
        count = 1
        while(runner):
            print(f"This is your {count} node, it contains value {runner.value}")
            count =+ 1
            runner = runner.next
        return self


new_singly_list = SLL(Node(1)) # I created a variable, inside of variable I invoked the SLL constructor and created a linked list object and I passed in a new node that contains the value 1 as my head node for my linked list. 
new_singly_list.add_front(2).add_front(4).add_front(22).add_front(43).add_front(7)
new_singly_list.display()



# Remove Front
# Write a method to remove the head node and return the new list head node. If the list is empty, return null.

def remove_front(self):
        if (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        return self
