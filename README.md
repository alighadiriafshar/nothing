Task Manager
A simple command-line task management application written in Python. This application allows users to manage tasks by adding, viewing, editing, marking as done, and deleting tasks. Tasks are stored in a JSON file (tasks.json) for persistence.
Features

Add Task: Create a new task with a title, description, and deadline.
Show Tasks: View all tasks with their ID, title, status, deadline, and description.
Mark Task as Done: Update the status of a task to "Done."
Edit Task: Modify the title, description, or deadline of an existing task.
Delete Task: Remove a task from the list and reassign IDs to maintain sequential order.
Cross-Platform Clear Screen: Clears the terminal screen on Windows, Linux, or macOS.
Colorful Interface: Uses colorama for colored terminal output to enhance user experience.

Requirements

Python 3.x
colorama library (pip install colorama)

Installation

Clone or download the repository.
Install the required package:pip install colorama


Run the script:python task_manager.py



Usage

Run the script to start the application.
Choose an option from the menu by entering the corresponding number:
1: Add a new task.
2: Display all tasks.
3: Mark a task as done by entering its ID.
4: Edit a task by entering its ID and updating its fields.
5: Delete a task by entering its ID.
0: Exit the application.


Follow the prompts to interact with the application.
Tasks are saved in tasks.json in the same directory as the script.

File Structure

task_manager.py: The main Python script containing the application logic.
tasks.json: The JSON file where tasks are stored (created automatically when tasks are added).

Example Task in tasks.json
[
    {
        "id": 1,
        "title": "Complete Project",
        "description": "Finish the project documentation",
        "status": "Pending",
        "deadline": "2025-09-10"
    }
]

Notes

The application uses the colorama library to provide a colorful and user-friendly interface.
Task IDs are automatically assigned and re-indexed when a task is deleted.
Invalid inputs (e.g., non-numeric input for task ID) are handled with appropriate error messages.
The screen is cleared after each operation for a clean interface.
The application is compatible with Windows, Linux, and macOS.

License
This project is licensed under the MIT License.
