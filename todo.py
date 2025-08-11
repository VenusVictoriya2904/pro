def main():
    tasks = []
    while True:
        print("1->Add a Task")
        print("2->Show the Task")
        print("3->Marked Task as Done")
        print("4->Exit")
        try:
            choice = int(input("Enter your choice: "))
        except TypeError:
            print("please enter a number as a input")
        if choice == 1:
            print()
            n_choice = int(input("How many task you want to add:"))
            for i in range(n_choice):
                task = input("Enter the task:")
                tasks.append({"task":task,"status":False})
                print("Task added successfully")
        elif choice == 2:
            print("\nTask:")
            for index,task in enumerate(tasks):
                status = "Done" if task["status"] else "not done"
                print(f"{index+1}. {task['task']}-{status}")
        elif choice == 3:
            task_index = int(input("Enter the task number to mark as done:"))-1
            if task_index<=4 and task_index>0:
                tasks[task_index]["status"]= True
                print("Task Marked as Done!")
            else:
                print("Invalid Task number")
        elif choice == 4:
            print("Exiting the TO-DO list")
            break
        else:
            print("enter the valid choice. Please Try Again")
if __name__ == "__main__":
    main()