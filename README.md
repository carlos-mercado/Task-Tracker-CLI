# Task Tracker CLI

A simple command-line task tracker written in Python. Tasks are stored in a local `tasks.json` file. You can add, update, delete, and list tasks with different statuses.

## Features

- Add new tasks with a name and status
- Update the status of existing tasks
- Remove tasks by name
- List tasks filtered by status (`done`, `not done`, `in progress`)
- Data is persisted in `tasks.json`

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Follow the on-screen prompts to manage your tasks:

   - Add (1): Add a new task
   - Update (2): Update the status of an existing task
   - Delete (3): Remove a task by name
   - Print (4): List tasks filtered by status
   - Quit (Q): Exit the program

## Requirements

- Python 3.x

## Data Storage

All tasks are stored in `tasks.json` in the project directory.

https://github.com/carlos-mercado/Task-Tracker-CLI
