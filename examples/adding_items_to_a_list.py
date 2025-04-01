# Create the original list.
tasks = ["Do homework", "Go the gym", "Get groceries"]
# Print out the list.
print(tasks)

# Prompt the user to add an item to the list, save their response in 'new_task'
new_task = input("What do you want to add to your to-do list? ")
# Append the value of 'new_task' to the list.
tasks.append(new_task)

# Print out the list.
print(tasks)