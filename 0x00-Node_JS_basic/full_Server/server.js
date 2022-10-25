// Express HTTP server
const express = require('express');
const routes = require('./routes/index');

const app = express();

app.use(routes).listen(1245);

export default app;
