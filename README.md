# Building a Django CRUD (Create, Retrieve, Update and Delete) Project Using Class-Based Views

This project is A demonstrition of dajngo api skiles.
Django is a powerful Python web framework that simplifies web development by providing a clean and pragmatic design. One of the most common tasks in web development is creating CRUD (Create, Read, Update, Delete) functionality for your application. In this article, we'll explore how to create a Django CRUD project using function-based views.

### Prerequisites

Before we dive into building our CRUD project, make sure you have the following prerequisites in place:

1. Python and Django: Ensure you have Python installed on your system. You can install Django using pip:
```python
pip install django
```

2. Database: Decide on the database you want to use. By default, Django uses SQLite, but you can configure it to use other databases like PostgreSQL, MySQL, or Oracle.

3. Text Editor or IDE: Choose a code editor or integrated development environment (IDE) of your preference. Popular choices include Visual Studio Code, PyCharm, or Sublime Text.

### Setting Up Your Django Project

Let's start by creating a new Django project and a new app within that project. Open your terminal and run the following commands:

```python
django-admin startproject CrudDimo
cd crudproject
python manage.py startapp CrudDimoApi
```

We've created a new project named "CrudDimo" and an app named "CrudDimoApi."

### Testing Your CRUD Project

With everything set up, you can start your Django development server:

```python
python manage.py runserver
```

Visit http://localhost:8000/ in your browser, and you should be able to create, read, update, and delete orders in your Django CRUD project using function-based views.

In this tutorial, you've learned how to create a Django CRUD project using function-based views. You can further enhance your project by adding features like authentication, pagination, or search functionality. Django's flexibility and extensive ecosystem make it a great choice


