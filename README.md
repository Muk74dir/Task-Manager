# Task Manager

Task Manager is a web application built with Django, designed to help users manage and organize their tasks efficiently.

## Features

- **User Registration and Authentication:** Users can register for an account and log in securely.
- **Task Management:** Add, edit, and delete tasks with details such as title, description, due date, and priority.
- **Photo Attachment:** Users can attach photos to their tasks for better organization.
- **Profile Page:** Users have a profile page displaying their information.
- **Password Change:** Users can change their passwords.
- **Task Filtering:** Filter tasks by title, creation date, due date, priority, and completion status.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/task-manager.git
    cd task-manager
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Visit `http://127.0.0.1:8000` in your web browser to access the application.

## Contributing

Contributions are welcome! Feel free to open issues and pull requests.

