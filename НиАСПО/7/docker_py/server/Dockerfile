# Dockerfile всегда должен начинаться с импорта базового образа.
# Для этого используется ключевое слово 'FROM'.
# Импортируем образ python (с DockerHub).
# В результате в качестве имени образа указываем 'python', а в качестве версии- 'latest'.
FROM python:latest
# Для того чтобы запустить в контейнере код, написанный на Python, нужноимпортировать файлы 'server.py' и 'index.html'.
# Для того, чтобы это сделать используется ключевое слово 'ADD'.
# Первый параметр, 'server.py', представляет собой имя файла, хранящегося накомпьютере.
# Второй параметр, '/server/', это путь, по которому нужно разместить указанный файл в образе.
# Помещаем файл в папку образа '/server/'.
ADD server.py /server/
ADD index.html /server/
# Воспользуемся командой 'WORKDIR'.
# Она позволяет изменить рабочую директорию образа.
# В качестве такой директории, в которой будут выполняться все команды, мы устанавливаем '/server/'.
WORKDIR /server/