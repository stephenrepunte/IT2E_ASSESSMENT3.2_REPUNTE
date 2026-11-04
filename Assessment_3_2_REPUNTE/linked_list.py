# Assessment 3.2 - Linked List
# Last Name: REPUNTE

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

    def remove_first(self):
        if self.head is not None:
            removed = self.head.data
            self.head = self.head.next
            return removed
        return None

    def is_empty(self):
        return self.head is None


print("================================")
print("      LINKED LIST STRUCTURE")
print("================================")

name = input("Enter your last name (press ENTER for REPUNTE): ").strip().upper()

if name == "":
    name = "REPUNTE"

if not name.isalpha():
    print("Invalid input. Please enter letters only.")
else:
    linked_list = LinkedList()

    for letter in name:
        linked_list.add(letter)

    print("\nOriginal Linked List:")
    linked_list.display()

    while not linked_list.is_empty():
        input("\nPress ENTER to delete the first node...")
        removed = linked_list.remove_first()
        print("Deleted Letter:", removed)
        print("Remaining Linked List:")
        linked_list.display()

    print("\nThe linked list is now empty!")
    print("Program finished.")
