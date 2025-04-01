#            Index 0        Index 1          Index 2
tasks = ["Do homework", "Go to the gym", "Get groceries"]

# Print out each item in the list with a number beside it, starting from 1.
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
    
# Prompt the user for which task they want to delete. Cast the type to 'integer'. input() returns a string by default.
choice = int(input("Which task do you want to delete? "))
choice = choice - 1 # Reduce the value of their input by 1 to give us a proper index number.
tasks.pop(choice) # Remove the desired element from the list. 

# Print out the new contents of the list.
print(tasks)