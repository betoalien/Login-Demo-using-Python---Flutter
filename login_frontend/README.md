# 🚀 Full-Stack Authentication Starter Kit

A clean and beginner-friendly boilerplate for building modern applications with a **Python (FastAPI)** backend and a **Flutter** frontend.  
This starter kit is designed to help **junior developers** quickly build a secure, working authentication system for mobile or web apps.

---

## ✨ Features

- ✅ **User Registration** – Create accounts with hashed passwords.
- 🔐 **User Login** – Authenticate users using email and password.
- 🪙 **JWT Authentication** – Secure API endpoints using JSON Web Tokens.
- 🧂 **Password Hashing** – Uses bcrypt to avoid storing plain text passwords.
- 🧱 **Frontend & Backend Separation** – Decoupled architecture for easy scaling.
- 📱 **Mobile Ready** – Flutter setup works for both Android and iOS emulators/devices.
- ⚡ **Redis Cache** (Optional) – Integrated caching layer for user data (advanced use).

---

## 🛠️ Technology Stack

| Area      | Technology                                                                                  |
|-----------|---------------------------------------------------------------------------------------------|
| Backend   | Python, FastAPI, SQLAlchemy (ORM), PostgreSQL, Alembic, Pytest, Uvicorn, Redis               |
| Frontend  | Flutter, Dart                                                                              |

---

## 📂 Project Structure

```bash
backend/
├─ app/
│ ├─ routers/ # FastAPI routes (auth, users)
│ ├─ models.py # SQLAlchemy models
│ ├─ crud.py # Database & Redis operations
│ ├─ schemas.py # Pydantic schemas
│ ├─ security.py # JWT & password hashing
│ ├─ redis_client.py # Redis connection
│ └─ main.py # App entrypoint
└─ .env

frontend/
├─ lib/
│ ├─ screens/ # Login, Register, User dashboard
│ ├─ services/ # AuthService (HTTP requests)
│ └─ main.dart
└─ pubspec.yaml
```

---

## 🧰 Prerequisites

- 🐍 **Python** 3.9+
- 🐘 **PostgreSQL**
- 🐦 **Flutter SDK**
- 📝 IDE like VS Code, IntelliJ IDEA, or Android Studio

---

## ⚡ Backend Setup (FastAPI)

```bash
# 1. Navigate to the backend folder
cd backend

# 2. Create and activate virtual environment
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Create a .env file with your DB credentials and JWT secret key.
# (You can copy from .env.example if provided)

# 5. Run migrations
alembic upgrade head

# 6. Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 5000
```

The backend runs at http://localhost:5000

API docs available at http://localhost:5000/docs


```bash
# 1. Navigate to frontend folder
cd login_frontend

# 2. Get dependencies
flutter pub get

# 3. Ensure a device/emulator is connected
flutter devices

# 4. Run the app
flutter run
```

The Flutter app is configured to connect to the backend using your local IP (e.g. http://192.168.x.x:5000).

🔐 Authentication Flow

Register → Creates a new user in PostgreSQL.

Login → Authenticates and receives a JWT token.

User Screen → Displays the logged-in user's email and the current login time.

Redis Cache (optional) → Caches user data for faster lookups on subsequent logins.

🧠 Why this project?

Most tutorials for authentication are either too simple (no real structure) or too complex for beginners.
This starter kit gives juniors a realistic, production-like structure that they can use as a base for:

Mobile apps with secure backends

SaaS dashboards or portals

Real-world interview projects / coding challenges

🤝 Contributing & Contact

This project is meant as a learning tool and quick start template.
If you’d like to contribute improvements, translations, or bug fixes, PRs are welcome.

📬 Contact: conect@albertocardenas.com

🧭 Next Steps (Ideas)

Add persistent token storage on mobile (e.g. flutter_secure_storage)

Refresh tokens

Role-based access (admin / user)

More Redis caching layers

Docker Compose setup