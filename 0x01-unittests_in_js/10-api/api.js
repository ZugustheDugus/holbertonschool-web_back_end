// Express app
const express = require('express');
const app = express();

app.get('/', (request, response) => {
	response.send('Welcome to the payment system');
}).get('/cart/:id([0-9]*)', (request, response) => {
	response.send(`Payment methods for cart ${request.params.id}`);
}).get('/available_payments', (request, response) => {
	response.json({
		payment_methods: {
			credit_cards: true,
			paypal: false
		}
	});
}).use(express.json()).post('/login', (request, response) => {
	response.send(`Welcome ${request.body.userName}`);
}).listen(7865, () => {
	console.log('API available on localhost port 7865')
});

module.exports = app;