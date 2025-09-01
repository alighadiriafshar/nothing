Task Manager
A simple command-line task management application built with Python. This tool allows users to create, view, edit, mark as done, and delete tasks. Tasks are stored persistently in a tasks.json file.
Features

Add Task: Create a task with a title, description, and deadline.
View Tasks: Display all tasks with their ID, title, status, deadline, and description.
Mark as Done: Update a task's status to "Done" by entering its ID.
Edit Task: Modify a task's title, description, or deadline.
Delete Task: Remove a task and automatically re-index task IDs.
Cross-Platform: Works on Windows, Linux, and macOS with screen-clearing functionality.
Colored Interface: Uses the colorama library for a vibrant, user-friendly terminal experience.

Prerequisites

Python 3.x
colorama library (pip install colorama)

Installation

Clone or download the repository:git clone <repository-url>


Install the required dependency:pip install colorama


Run the application:python task_manager.py



Usage

Launch the script to open the main menu.
Select an option by entering the corresponding number:
1: Add a new task.
2: View all tasks.
3: Mark a task as done by entering its ID.
4: Edit a task by entering its ID and updating fields.
5: Delete a task by entering its ID.
0: Exit the application.


Follow the on-screen prompts to manage tasks.
Tasks are saved automatically to tasks.json in the project directory.

Example tasks.json
[
    {
        "id": 1,
        "title": "Finish Project",
        "description": "Complete the project documentation",
        "status": "Pending",
        "deadline": "2025-09-10"
    }
]

File Structure

task_manager.py: Main script containing the application logic.
tasks.json: Auto-generated file for storing tasks.
LICENSE: MIT License file (recommended to include).

Notes

Task IDs are auto-assigned and re-indexed upon deletion.
Invalid inputs (e.g., non-numeric IDs) are handled with clear error messages.
The terminal screen clears after each operation for a clean interface.
The colorama library enhances the interface with colored text.
Compatible with Windows, Linux, and macOS.

Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.
License
This project is licensed under the MIT License.
