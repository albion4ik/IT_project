
# 👤 User Management Web App

This is a full-stack Flask web application with PostgreSQL and Docker, allowing users to **register**, **log in**, and **view all users**. Admin users additionally have permission to **delete any user** from the system.

---

## 🎯 Project Purpose

- Simple and secure user management system.
- Admin features for user moderation.
- Deployed and runnable using Docker.

---

## 🛠️ Features

| Feature | Description |
|--------|-------------|
| ✅ User Registration | Users can sign up with a username and password. |
| ✅ User Login | Authenticated users can log in and view others. |
| ✅ Admin Role | Admins can delete any user account. |
| ✅ PostgreSQL DB | Stores user information securely. |
| ✅ Dockerized | Easily deployable via Docker & Docker Compose. |

---

## ⚙️ Technologies Used

- 🐍 **Python 3.9**
- 🌐 **Flask**
- 🗄️ **PostgreSQL**
- 🐳 **Docker**
- 🔐 **Flask-Login** for authentication
- 💻 **HTML/CSS** for frontend

---

## 🛠️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/albion4ik/IT_project.git
cd IT_project
```

### 2. Install dependencies

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Ensure you have **PostgreSQL** running. Modify database connection parameters in `app.py` if necessary.

### 4. Run the application

#### Using Docker (recommended)

To run the app with Docker, use the following command:

```bash
docker-compose up --build
```

Access the app at: [http://localhost:5000](http://localhost:5000)

#### Without Docker

Alternatively, you can run the app directly using Flask:

1. Make sure **PostgreSQL** is installed and running.
2. Modify the database connection settings in `app.py`.
3. Run the app with:

```bash
python app.py
```

---

## 📂 Project Structure

```
IT_project/
│
├── static/               # Static files (CSS, images)
├── templates/             # HTML templates
│   └── home.html          # Main page template
│   └── login.html         # Login page template
│   └── register.html      # Registration page template
├── app.py                 # Backend logic for user management
├── requirements.txt       # Python dependencies
└── Dockerfile             # Dockerfile for containerization
└── docker-compose.yml     # Docker Compose configuration
└── README.md              # Project documentation
```

---

## 🚀 How to Run the Project

1. Clone the repo:

```bash
git clone https://github.com/albion4ik/IT_project.git
cd IT_project
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open your browser at:

```
http://localhost:5000
```

---

## 📚 License

This project is open-source and available under the [MIT License](LICENSE).
