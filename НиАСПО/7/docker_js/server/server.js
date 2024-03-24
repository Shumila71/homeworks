const http = require('http');
const fs = require('fs');

// Создаем HTTP-сервер
const server = http.createServer((req, res) => {
  // Загружаем файл 'index.html' с сервера
  fs.readFile('index.html', (err, data) => {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found");
    }  
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
});

// Сервер будет работать на порте 1234
const PORT = 1234;
server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});
