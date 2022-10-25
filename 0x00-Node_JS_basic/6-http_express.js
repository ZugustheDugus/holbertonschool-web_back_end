// Creates a small HTTP server using the Express module
const express = require('express');

const app = express();

app.get('/', (request, response) => response.send(
  'Hello Holberton School!',
))
  .listen(1245);

module.exports = app;
