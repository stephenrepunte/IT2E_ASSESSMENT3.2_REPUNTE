# Assessment 3.2 - Stack (LIFO)
# Last Name: REPUNTE

print("================================")
print("        STACK STRUCTURE")
print("================================")

name = input("Enter your last name (press ENTER for REPUNTE): ").strip().upper()

if name == "":
    name = "REPUNTE"

if not name.isalpha():
    print("Invalid input. Please enter letters only.")
else:
    stack = []

    for letter in name:
        stack.append(letter)

    print("\nOriginal Stack (Top to Bottom):")
    print(list(reversed(stack)))

    while len(stack) > 0:
        input("\nPress ENTER to pop the top letter...")
        removed = stack.pop()
        print("Popped Letter:", removed)
        print("Remaining Stack (Top to Bottom):")
        print(list(reversed(stack)))

    print("\nThe stack is now empty!")
    print("Program finished.")
