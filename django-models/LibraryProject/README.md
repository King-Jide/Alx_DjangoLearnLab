# 📚 LibraryProject

A beginner-friendly guide to setting up and running a basic Django project called **LibraryProject**.

---

## 📝 Task Description

Set up a Django project named **LibraryProject**.  
This initial setup serves as the foundation for developing Django applications.  
You’ll also explore the project’s default structure to understand the roles of various components.

---

## 📑 Table of Contents

- [Task Description](#-task-description)
- [Virtual Environment Setup](#-virtual-environment-setup)
- [Steps](#-steps)
- [Explore the Project Structure](#-explore-the-project-structure)
- [Repository Info](#-repository-info)
- [Next Steps](#-next-steps)
- [Contributing](#-contributing)

---

## ⚙️ Virtual Environment Setup

Using a virtual environment keeps project dependencies isolated from your system Python.

1. **Create a virtual environment:**
   ```bash
   python3 -m venv django_env
   ```

2. **Activate the virtual environment:**
   - On **Linux/Mac**:
     ```bash
     source django_env/bin/activate
     ```
   - On **Windows (PowerShell)**:
     ```powershell
     .\django_env\Scripts\activate
     ```

3. **Deactivate when finished (all platforms):**
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

Verify installation:
```bash
django-admin --version
```

### 2. Create Your Django Project

Run the following command:
```bash
django-admin startproject LibraryProject
```

### 3. Run the Development Server

- Navigate into your project directory:
  ```bash
  cd LibraryProject
  ```
- Start the development server:
  ```bash
  python manage.py runserver
  ```
- Open a web browser and go to:  
  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
  to view the default Django welcome page 🎉

---

## 🧭 Explore the Project Structure

When you create a new Django project, the folder structure looks like this:

```
LibraryProject/
├── manage.py
└── LibraryProject/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### Key Files

| File                  | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `manage.py`           | Command-line utility to interact with this Django project               |
| `settings.py`         | Configuration for the Django project                                    |
| `urls.py`             | URL declarations; the “table of contents” of your site                  |
| `__init__.py`         | Marks the directory as a Python package                                 |
| `asgi.py` / `wsgi.py` | Entry points for ASGI/WSGI-compatible web servers                       |

---

## 📂 Repository Info

- **GitHub Repository:** [`Alx_DjangoLearnLab`](https://github.com/King-Jide/Alx_DjangoLearnLab)
- **Directory:** `Introduction_to_Django/LibraryProject`

---

## ✅ Next Steps

- Create Django apps inside **LibraryProject**
- Explore **models**, **views**, and **templates**
- Add routing and dynamic content
- Connect to a database and build CRUD functionality

For more in-depth guidance, see the [Django documentation](https://docs.djangoproject.com/en/stable/).

---

## 🤝 Contributing

Contributions are welcome!  
If you’d like to improve this guide, feel free to fork the repository, make changes, and submit a pull request.

---
