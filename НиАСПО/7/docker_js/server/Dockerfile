FROM node:latest

# Копируем файлы 'server.js' и 'index.html' внутрь контейнера
COPY server.js /server/
COPY index.html /server/

# Устанавливаем рабочую директорию '/server/'
WORKDIR /server/

# # Запускаем сервер при запуске контейнера
# CMD ["node", "server.js"]