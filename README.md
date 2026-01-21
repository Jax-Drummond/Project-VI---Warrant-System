# 👮 Officer Warrant System

A hybrid **Django + Django REST Framework** application for managing police personnel and search warrants. This project allows for both web-based management (via Django Templates) and external integration (via REST API).

The entire development environment is containerized using **Docker**, ensuring consistency across all developer machines.

---

## 🚀 Features

* **Hybrid Architecture:**
* 🖥️ **Web Dashboard:** Server-side rendered views using Django Templates.
* 📡 **REST API:** JSON endpoints for mobile apps or external integrations.


* **Core Modules:**
* 👮 **Officers:** Keep track of police personnel.
* 📜 **Warrants:** Create, track, and execute search warrants.


* **Infrastructure:**
* 🐳 Fully Dockerized (No local Python installation required).
* 🗄️ SQLite Database (File-based, persistent via Docker volumes).



---

## 📦 Requirements

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* *Windows Users:* Ensure **WSL 2** backend is enabled in Docker settings.


* Git

---

## 📂 File Structure

```bash
warrant-system/
├── /config                # Project-wide settings & main URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── /warrants              # Main Application Logic
│   ├── /management        # Commands (e.g seed)
│   ├── /migrations        # DB Schema changes
│   ├── /templates         # HTML files (Frontend)
│   ├── models.py          # Database Tables
│   ├── views.py           # Logic handlers
│   └── urls.py            # App-specific routes
├── Dockerfile             # Image build instructions
├── docker-compose.yml     # Service orchestration
├── requirements.txt       # Python dependencies
├── manage.py              # Django CLI entry point
└── db.sqlite3             # Database file (Ignored by Git)

```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Jax-Drummond/Project-VI---Warrant-System
cd warrant-system
```


2. **Start the environment:**
This will build the Docker image and start the server.
```bash
docker compose up
```


* *Note: The first run might take a few minutes to download the Python image.*


3. **Run Migrations (Initialize Database):**
Open a **new** terminal window and run:
```bash
docker compose exec web python manage.py migrate
```


4. **Create an Admin User:**
To access the Django Admin panel:
```bash
docker compose exec web python manage.py createsuperuser
```


5. **Access the App:**
* **Web App:** [http://localhost:8000](https://www.google.com/search?q=http://localhost:8000)
* **Admin Panel:** [http://localhost:8000/admin](https://www.google.com/search?q=http://localhost:8000/admin)



---

## 🛠️ Development Workflow

Because we are using Docker, **do not** run `python manage.py` directly on your local machine. Use the wrapper commands below.

### 🔄 Database Migrations

Run this whenever you pull code that changes `models.py`:

```bash
docker compose exec web python manage.py migrate
```

If you have made changes to `models.py` and need to generate new migration files:

```bash
docker compose exec web python manage.py makemigrations
```

### 🌱 Database Seeding

Run this if you want to seed the database. (Currently only seeds citizens, and adds superuser(Check template.env))
```bash
docker compose exec web python manage.py seed
```

### 📦 Installing New Packages

If you add a package to `requirements.txt`, you must rebuild the container:

```bash
docker compose up --build
```

### 🧪 Running Tests

```bash
docker compose exec web python manage.py test
```

### 💻 Accessing the Shell

To interact with the database directly via Python:

```bash
docker compose exec web python manage.py shell
```

---

## ⚠️ Team Guidelines (Important)

**Database Management:**
We are using **SQLite**. The `db.sqlite3` file is ignored by Git to prevent conflicts.

* Each individual has their own local database.
* **Do not** delete the `.gitignore` entry for `db.sqlite3`.
* Always run `migrate` after pulling the latest code.
