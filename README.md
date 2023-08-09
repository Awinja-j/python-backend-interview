# Amitruck Trip Logging Application

The Amitruck Trip Logging Application is a Django-based API service that allows logging trip details with user, vehicle, and trip entities. It provides endpoints for capturing trip information, managing users and vehicles, and establishing relationships between them.

## Prerequisites

- Python 3.x
- Django 3.x
- Django Rest Framework

## Setup Instructions

1. **Clone the Repository:**
   
   Clone this repository to your local machine using the following command:
   
   ```bash
   git clone https://github.com/your-username/python-backend-interview.git
   cd python-backend-interview
## Create Virtual Environment:
It's recommended to create a virtual environment for the project to isolate dependencies. Run the following commands:
```
python -m venv venv
source venv/bin/activate  
```

### Install Dependencies:
Install the required dependencies using pip:
```
pip install -r requirements.txt
```

### Apply Migrations:
Apply the database migrations to set up the database schema:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Create SQLite Database:

By default, the application uses an SQLite database. To create the SQLite database, run the following command:
```
python3 manage.py migrate

```
### create superuser

```
python3 manage.py createsuperuser  

```
### Run the Development Server:

Start the development server to run the application locally:

```
python3 manage.py runserver
```
### Run tests:

```
python3 manage.py test
```
### Access the API:

You can now access the API at `http://127.0.0.1:8000/. `

The available endpoints include:

Generate a token using this endpoint:

```
http://127.0.0.1:8000/api-token-auth/
```
 with the following payload:

 ```
 {
    "username": "root",
    "password": 7890
}
 
 ```
Log Trip: 

```
http://127.0.0.1:8000/admin (POST)

```
### When Making a request:

please include the following in your payload:

```

```










