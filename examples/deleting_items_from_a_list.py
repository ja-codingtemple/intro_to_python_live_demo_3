tasks = []

# Function to initialize the list with its three default values.
def initializeList():
    global tasks
    tasks = ["Do homework", "Go to the gym", "Get groceries", "Edit homework", "Finish homework"]
    print("INTIIAL LIST: " + str(tasks))
    
# METHOD 1: remove()
print("\nMETHOD 1:")
initializeList() # Assigns default values to our list variable.
tasks.remove("Do homework") # Removes the element "Do homework" from the list.
print("CURRENT LIST: " + str(tasks))

# METHOD 2: pop()
print("\nMETHOD 2:")
initializeList() # Assigns default values to our list variable.
tasks.pop(0) # Remove the element at index 0 in the list.
print("CURRENT LIST: " + str(tasks))

# METHIOD 3: del
print("\nMETHOD 3:")
initializeList() # Assigns default values to our list variable.
del tasks[0] # Remove the element at index 0 in the list.
print("CURRENT LIST: " + str(tasks))

# BONUS METHOD (not recommended for the project)
'''
Loop through the list, check if any element contains a particular substring.
Use remove() to remove the element if it does.
'''
print("\nMETHOD 4:")
initializeList() # Assigns default values to our list variable.
for task in tasks[:]:
    # Check if the word "homework" is in the selected task.
    if "homework" in task:
        tasks.remove(task) # If it is, remove the task.
print("CURRENT LIST: " + str(tasks))