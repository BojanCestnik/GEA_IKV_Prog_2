# Model
class ToDoModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

# View
class ToDoView:
    def show_tasks(self, tasks):
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    def show_message(self, message):
        print(message)

# Controller
class ToDoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        self.model.add_task(task)
        self.view.show_message("Task added successfully!")

    def display_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)

def main():
    model = ToDoModel()
    view = ToDoView()
    controller = ToDoController(model, view)

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            controller.add_task(task)
        elif choice == "2":
            controller.display_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
