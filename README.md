# Automation Task: To-Do List Sorter

This project is a simple Python script created for a university assignment. It automates the process of sorting a to-do list alphabetically.

## Description

The script, `automation_script.py`, takes a list of tasks as input and provides a neatly sorted, alphabetized list as output. This helps in organizing daily tasks more efficiently.

## How It Works

The script offers two methods for providing input:

1.  **Manual Console Input**: The user can type their tasks directly into the console one by one.
2.  **File Input**: The script can read tasks from a text file named `task.txt` located in the same directory. Each task should be on a new line.

After receiving the list of tasks, the script performs an alphabetical sort (case insensitive) and prints the ordered list to the console.

## How to Run the Script

1.  **Prerequisites**: Make sure you have Python 3 installed on your system.
2.  **Clone the Repository**:
    ```bash
    git clone [\[https://github.com/your-username/automation-task.git\]]
    (https://github.com/Faezeh05KZ/Automation-tasks.git)
    cd automation-task
    ```
3.  **Run the Script**:
    ```bash
    python automation_script.py
    ```
4.  **Follow the Prompts**: The script will ask you to choose an input method (1 for console, 2 for file). Follow the on-screen instructions to enter your tasks.

## Sample Usage

### Input from `tasks.txt`

If you create a `tasks.txt` file with the following content:

```
Ducumenting content
Finish assignment
Doing Tasks
Go to the gym
Read a chapter
```

### Running the Script and Output

When you run the script and choose option `2`, the output will be:

```
$ python automation_script.py
Daily Task Sorter
How would you like to input your tasks?
1: Enter tasks manually in the console
2: Read tasks from a 'tasks.txt' file
Enter your choice (1 or 2): 2
Successfully loaded tasks from tasks.txt.

Your Sorted To-Do List :
1. Ducumenting content
2. Doing Tasks
3. Finish assignment
4. Go to the gym
5. Read a chapter

```
