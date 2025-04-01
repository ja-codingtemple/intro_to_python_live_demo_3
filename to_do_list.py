tasks = []

# Function to display options.
def display_menu():
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")

# Function to add a task to the list.
def add_task():
    new_task = input("Enter a task: ") # Prompt user to enter a new task.
    tasks.append(new_task) # Add new_task to the list.
    print(f"Task {new_task} added successfully.")
    print(tasks)
    
# Function to view all tasks in the tasks list.
def view_task():
    print("This needs to be implemented still.") # Complete this please.
    
# Function to delete a task from the tasks list.
def delete_task():
    print("This needs to be implemented still.") # Complete this please.
    
# Main function (start of the program)
def main():
    # Infinite loop
    while True:
        display_menu()
        choice = input("What would you like to do?: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("invalid choice. Please try again.")
            
main()