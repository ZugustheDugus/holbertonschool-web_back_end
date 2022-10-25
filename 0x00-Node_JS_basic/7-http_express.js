// Creates a small HTTP server using the Express module
const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (request, response) => response.send(
  'Hello Holberton School!',
));

app.get('/students', (request, response) => {
  response.write('This is the list of our students\n');
  countStudents(process.argv[2]).then((data) => {
    response.end(data);
  })
    .catch((error) => response.end(error.message));
});

app.listen(1245);

module.exports = app;
