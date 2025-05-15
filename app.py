from flask import Flask, render_template, request, flash, redirect, url_for
import psycopg2
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Секретный ключ для сессий и безопасности

# Настройки для подключения к базе данных
DB_NAME = "Aiproject"
DB_USER = "postgres"
DB_PASSWORD = "solution"
DB_HOST = "localhost"
DB_PORT = "5432"

# Инициализация Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Подключение к базе данных PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None, None

# Модель пользователя
class User(UserMixin):
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

# Загружаем пользователя по его ID
@login_manager.user_loader
def load_user(user_id):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        return User(user[0], user[1], user[2])  # Возвращаем объект пользователя
    return None

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()  # Убираем пробелы
        password = request.form['password'].strip()  # Убираем пробелы

        conn, cursor = connect_db()
        cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash("Пользователь с таким именем уже существует.", "danger")
            return redirect(url_for('register'))
        
        cursor.execute("INSERT INTO users (name, password, role) VALUES (%s, %s, 'user')", (name, password))
        conn.commit()
        flash("Вы успешно зарегистрировались!", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name'].strip()  # Убираем пробелы
        password = request.form['password'].strip()  # Убираем пробелы

        conn, cursor = connect_db()
        if conn:
            cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
            user = cursor.fetchone()

            if user and user[3] == password:  # Проверяем пароль
                user_obj = User(user[0], user[1], user[2])  # Создаем объект пользователя
                login_user(user_obj)  # Выполняем вход
                flash("Успешный вход!", "success")
                return redirect(url_for('home'))  # Перенаправление на главную страницу
            else:
                flash("Неверные имя пользователя или пароль", "danger")
        else:
            flash("Ошибка при подключении к базе данных.", "danger")

    return render_template('login.html')


# Главная страница
@app.route('/home')
@login_required
def home():
    conn, cursor = connect_db()
    if conn:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()  # Получаем всех пользователей
        return render_template('home.html', users=users)  # Передаем пользователей в шаблон
    else:
        flash("Ошибка при подключении к базе данных.", "danger")
        return redirect(url_for('login'))

# Удаление пользователя
@app.route('/delete_user/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    if current_user.role != 'admin':
        flash("У вас нет прав для удаления пользователей", "danger")
        return redirect(url_for('home'))

    conn, cursor = connect_db()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    flash("Пользователь удален", "success")
    return redirect(url_for('home'))

# Выход
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы успешно вышли", "success")
    return redirect(url_for('login'))


# Запуск приложения
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
