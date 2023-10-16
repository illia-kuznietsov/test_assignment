# Django Restaurant Franchise Management System

## Description

A comprehensive Django-based backend system designed to manage multiple facets of restaurant franchises, such as menus, dishes, voting on dishes, employees, and more. The project utilizes Django Rest Framework (DRF) for API creation and JWT for user authentication and authorization.

## Features

- **Restaurants**: Add, update, delete, and retrieve details of different restaurants.
- **Dishes**: Manage dishes, allowing CRUD operations.
- **Menus**: Create menus consisting of various dishes, allowing for a daily selection.
- **Employees**: Manage employee information.
- **Voting**: Employees can vote on their preferred dishes for the day.

## Installation and Setup

1. **Clone the repository**

2. **Navigate to the project directory**

cd restaurant_franchise

3. **Setup a virtual environment**

python -m venv myenv

4. **Activate the virtual environment**

- **Windows**
  ```
  .\myenv\Scripts\activate
  ```
- **Linux or MacOS**
  ```
  source myenv/bin/activate
  ```

5. **Install dependencies**

pip install -r requirements.txt
## Running the Application

6. **Apply migrations**
python manage.py migrate

7. **Run the server**
python manage.py runserver

9. Access the application at `http://127.0.0.1:8000/`

