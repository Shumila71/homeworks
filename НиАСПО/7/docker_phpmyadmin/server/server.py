#!/usr/bin/env python3
# Импорт системных библиотек python.
# Эти библиотеки будут использоваться для создания веб-сервера.
# Эти библиотеки устанавливаются вместе с Python.
import http.server
import socketserver
# Эта переменная нужна для обработки запросов клиента к серверу.
handler = http.server.SimpleHTTPRequestHandler
# Сервер будет работать на порте 1234.
# Номер порта пригодится в дальнейшем при работе с docker-compose.
with socketserver.TCPServer(("", 1234), handler) as httpd:
 # Эта команда заставляет сервер работать постоянно, ожидая запросов отклиента.
 httpd.serve_forever()