# Используем официальный образ Python
FROM python:3.9

# Установка рабочей директории
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Установка зависимостей

RUN pip install --no-cache-dir -r requirements.txt --index-url https://pypi.org/simple


# Команда для запуска бота
CMD ["python", "main.py"]
