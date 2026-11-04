# Assessment 3.2 - Queue (FIFO)
# Last Name: REPUNTE

from collections import deque

print("================================")
print("        QUEUE STRUCTURE")
print("================================")

name = input("Enter your last name (press ENTER for REPUNTE): ").strip().upper()

if name == "":
    name = "REPUNTE"

if not name.isalpha():
    print("Invalid input. Please enter letters only.")
else:
    queue = deque()

    for letter in name:
        queue.append(letter)

    print("\nOriginal Queue:")
    print("Front", list(queue), "Rear")

    while len(queue) > 0:
        input("\nPress ENTER to dequeue the front letter...")
        removed = queue.popleft()
        print("Dequeued Letter:", removed)
        print("Remaining Queue:")
        print("Front", list(queue), "Rear")

    print("\nThe queue is now empty!")
    print("Program finished.")
