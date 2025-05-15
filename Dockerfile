# Используем официальный Python образ
FROM python:3.9-slim

# Устанавливаем необходимые пакеты для PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для приложения (например, 5000 для Flask)
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]
