# Starterproject Django 4.2 with tailwind and alpine.js

This project is a starter template designed to streamline the development of Django applications with integrated Tailwind CSS and Alpine.js. It includes a basic setup with one pre-configured Django app named `client`, which serves as an example to demonstrate how to define models and integrate frontend technologies.

## Project Description

The starter template provides a robust foundation for building modern web applications using Django, Tailwind CSS, and Alpine.js. The template aims to simplify the initial setup and configuration, allowing developers to focus on building their application's unique features.

## Demo Project

A live demo of the project is available at <a href="https://startproject-django-demo.onrender.com/" target="_blank">https://startproject-django-demo.onrender.com/</a>.

### Demo Credentials
- **Username:** testuser
- **Password:** demo1234

### Note
The project is hosted on a free instance web service on Render. As a result, it may be idle sometimes, causing the initial load to be slow. However, once the application is loaded, it should work normally.

### Features

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Tailwind CSS**: A utility-first CSS framework for rapid UI development.
- **Alpine.js**: A minimal JavaScript framework for composing behavior directly in your HTML.
- **Client App**: An example Django app named `client`, showcasing a basic model and how to integrate the frontend technologies.
- **Client CRUD App**: The Client App includes a fully featured CRUD interface for managing clients. You can create, read, update, and delete client records. The application templates are built using Alpine.js and styled with Tailwind CSS for a modern and responsive user experience.

### Example Model in Client App

The `client` app includes a simple model to demonstrate how to define and use models in Django. Here's an example of the `Client` model:

```python
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
```


## Prerequisites

Ensure you have the following installed on your machine:
- Python (3.x recommended)
- Node.js and npm
- pyenv (optional but recommended for managing Python versions)

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone git@github.com:igortosic-easymind/easymind-startproject-django-tailwindcss-alpinejs.git
cd easymind-startproject-django-tailwindcss-alpinejs
```

2. Set Up Python Virtual Environment
Using pyenv to set up a virtual environment ensures that the project dependencies are isolated from your global Python environment.

```bash
pyenv exec python3 -m venv .venv
```

3. Activate the Virtual Environment
Activate the virtual environment to start using it. This step is crucial before installing dependencies and running the project.

For macOS and Linux:
```bash
source .venv/bin/activate
```
For Windows:
```bash
.venv\Scripts\activate
```

4. Install Python Dependencies
Install all required Python packages listed in requirements.txt.

```bash
pip3 install -r requirements.txt
```

5. After cloning the repository, you need to create a superuser for your database. This is necessary to access the Django admin interface and manage your application.

To create a superuser, run the following command:

```bash
python3 manage.py createsuperuser
```

6. Install JavaScript Dependencies
Install the required Node.js packages.

```bash
npm install
```

7. Build JavaScript Assets
Build the project’s JavaScript assets using npm.

```bash
npm run build
```

8. Collect Static Files
Collect all static files into the directory specified in your Django settings. This is necessary for serving static assets.

```bash
python3 manage.py collectstatic
```

9. Run the Development Server
Start the Django development server. This will allow you to view the project in your web browser at http://127.0.0.1:8000/.

```bash
python3 manage.py runserver
```

Additional Commands
Deactivate the Virtual Environment: When you are done working on the project, you can deactivate the virtual environment by simply running:

```bash
deactivate
```

## Database Configuration

In the `settings.py` file, the default database settings for SQLite3 are commented out. There are settings for PostgreSQL which also require a `.env` file for local development. You can choose which one you want to use based on your preference.

### Using SQLite3
To use SQLite3, uncomment the relevant lines in the `settings.py` file.

### Using PostgreSQL
To use PostgreSQL, ensure you have a `.env` file with the necessary database configuration. The `DATABASE_URL_EXT` variable should be set in the `.env` file to configure the PostgreSQL connection.


## Contributing

If you wish to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes.
4. Commit your changes:
    ```bash
    git commit -am 'Add new feature'
    ```
5. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
6. Create a new Pull Request.

License
This project is licensed under the free License. See the LICENSE file for more details.
