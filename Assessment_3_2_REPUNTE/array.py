# Assessment 3.2 - Array
# Last Name: REPUNTE

print("================================")
print("       ARRAY DATA STRUCTURE")
print("================================")

name = input("Enter your last name (press ENTER for REPUNTE): ").strip().upper()

if name == "":
    name = "REPUNTE"

if not name.isalpha():
    print("Invalid input. Please enter letters only.")
else:
    array = list(name)
    print("\nOriginal Array:", array)

    while len(array) > 0:
        input("\nPress ENTER to remove the first letter...")
        removed = array.pop(0)
        print("Removed Letter:", removed)
        print("Remaining Array:", array)

    print("\nThe array is now empty!")
    print("Program finished.")
