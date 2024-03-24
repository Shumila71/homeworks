const http = require('http');

// Создаем HTTP-запрос к серверу
const options = {
  hostname: 'localhost',
  port: 1234,
  path: '/',
  method: 'GET'
};

const req = http.request(options, (res) => {
  let data = '';

  // Получаем данные с сервера
  res.on('data', (chunk) => {
    data += chunk;
  });

  // Выводим полученные данные
  res.on('end', () => {
    console.log(data);
  });
});

// Обрабатываем возможные ошибки
req.on('error', (error) => {
  console.error(`Error: ${error.message}`);
});

// Завершаем запрос
req.end();
