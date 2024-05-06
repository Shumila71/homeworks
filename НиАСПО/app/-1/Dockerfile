# Используем базовый образ Python
FROM python:3.8-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app


# Копируем приложение внутрь контейнера
COPY . .

EXPOSE 5000

RUN pip install flask requests

# Команда для запуска приложения
CMD [ "python", "app1.py" ]