````markdown
# 📚 LibraryProject

A beginner-friendly Django setup guide for creating and running a basic project called **LibraryProject**.

---

## 📝 Task Description

Install Django and create a new Django project named **LibraryProject**.  
This initial setup will serve as the foundation for developing Django applications.  
You’ll also explore the project’s default structure to understand the roles of various components.

---

## 📑 Table of Contents

- [Task Description](#-task-description)
- [Virtual Environment Setup](#-virtual-environment-setup)
- [Steps](#-steps)
- [Project Structure](#-explore-the-project-structure)
- [Repository Info](#-repository-info)
- [Next Steps](#-next-steps)
- [License](#-license)
- [Contributing](#-contributing)

---

## ⚙️ Virtual Environment Setup

It’s best practice to use a virtual environment so dependencies don’t interfere with your system Python.

1. Create a virtual environment:
   ```bash
   python3 -m venv django_env
   ```

2. Activate the virtual environment:

   * On **Linux/Mac**:
     ```bash
     source django_env/bin/activate
     ```
   * On **Windows (PowerShell)**:
     ```powershell
     django_env\Scripts\activate
     ```

3. When finished working, deactivate with:
   ```bash
   deactivate
   ```

---

## 🚀 Steps

### 1. Install Django

With the virtual environment active, install Django:

```bash
pip install django
```

### 2. Create Your Django Project

Run the following command:

```bash
django-admin startproject LibraryProject
```

### 3. Run the Development Server

* Navigate into your project directory:
  ```bash
  cd LibraryProject
  ```
* Start the development server:
  ```bash
  python manage.py runserver
  ```
* Open a web browser and go to:  
  👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
  to view the default Django welcome page.

---

## 🧭 Explore the Project Structure

Pay attention to the following files:

| File                  | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `manage.py`           | Command-line utility to interact with this Django project               |
| `settings.py`         | Configuration for the Django project                                    |
| `urls.py`             | URL declarations; the “table of contents” of your Django-powered site   |
| `__init__.py`         | Marks the directory as a Python package                                 |
| `asgi.py` / `wsgi.py` | Entry points for ASGI/WSGI-compatible web servers                       |

---

## 📂 Repository Info

* **GitHub Repository**: `Alx_DjangoLearnLab`  
* **Directory**: `Introduction_to_Django`

---

## ✅ Next Steps

- Create Django apps inside **LibraryProject**
- Dive deeper into **models**, **views**, and **templates**
- Add routing and dynamic content
- Connect to a database and build CRUD functionality

---



