# To DO List Django Project 

**A simple application for managing tasks(add, update, delete, filter) with user registration and authentication.**

## Features

- User registration and login
- Create, update, delete, and filter tasks
- Pagination for task lists
- REST API with JWT authentication

## Project Structure:

to_do_list/
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── to_do_app/
└── to_do_list/

## Technologies:
- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Simple JWT

## How to Start:

**Clone the repository:**
```
git clone <https://github.com/SimaG1989/to_do_list.git>
cd <to_do_list>
```

**Activate Environment:**
```
python -m venv to_do_list
to_do_list\Scripts\activate.bat

```
**Install Dependencies**
```
pip install -r reqirements.txt

```
**Run Migrations**
```
python manage.py migrate

```

**Start The Development Server on Local Machine**
```
python manage.py runserver
```
## Web Interface
http://localhost:8000/ Register Form
http://localhost:8000/tasks View Task List

## Project Structure
to_do_app/
├── forms.py
├── models.py
├── views.py
├── serializers.py
├── templates/
│   └── to_do_app/
│       ├── login.html
│       ├── register.html
│       ├── task_list.html
│       ├── task_update.html
│       └── task_detail.html



   

