# Full-Stack Authentication Starter Kit

A clean and robust boilerplate for building modern applications, featuring a **Python (FastAPI)** backend and a **Flutter** frontend.  
This starter kit is designed to help junior developers kickstart their projects by providing a ready-to-use, secure user authentication system.

---

## ✨ Features

- **User Registration**: Securely create new user accounts.  
- **User Login**: Authenticate users with email and password.  
- **JWT Authentication**: Secure API endpoints using JSON Web Tokens.  
- **Password Hashing**: Passwords are never stored in plain text, using bcrypt.  
- **Separated Frontend & Backend**: A decoupled architecture for better maintainability and scalability.  
- **Ready for Mobile**: The Flutter frontend is set up for both Android and iOS.

---

## 🛠️ Technology Stack

| Area      | Technology                                                                                  |
|-----------|---------------------------------------------------------------------------------------------|
| Backend   | Python, FastAPI, SQLAlchemy (ORM), PostgreSQL, Alembic, Pytest, Uvicorn                      |
| Frontend  | Flutter, Dart                                                                              |

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.9+  
- PostgreSQL  
- Flutter SDK  
- An IDE/Editor like VS Code or IntelliJ IDEA

---

### 1. Backend Setup (FastAPI)

```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create and activate a virtual environment
# On Windows:
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your environment variables
# Create a .env file and fill in your database credentials and a secret key.
# You can copy the structure from .env.example if provided.

# 5. Run database migrations
alembic upgrade head

# 6. Start the server
python -m uvicorn app.main:app --reload
```
The backend API will be running at http://127.0.0.1:8000.

You can access the auto-generated documentation at http://127.0.0.1:8000/docs.

2. Frontend Setup (Flutter)
```bash
# 1. Navigate to the frontend directory
cd login_frontend 

# 2. Get all the dependencies
flutter pub get

# 3. Make sure an emulator is running or a device is connected.
# You can check with:
flutter devices

# 4. Run the app
flutter run
```

🤝 Contributing & Contact

This project is designed as a learning and starting point. If you have questions, suggestions, or would like to contribute, please feel free to reach out.

For more information or to participate in the project, please email: conect@albertocardenas.com
