// Tests for api.js
const expect = require('chai').expect;
const request = require('request');

describe('appTests', () => {
	it('Ensures app.js behavior', (done) => {
		request('http://localhost:7865/', (error, response, body) => {
			expect(response.statusCode).to.equal(200);
			expect(body).to.equal('Welcome to the payment system');
			done();
		})
	})
	it('Ensures /cart/:id behavior', (done) => {
		request('http://localhost:7865/cart/5', (error, response, body) => {
			expect(response.statusCode).to.equal(200);
			expect(body).to.equal('Payment methods for cart 5');
		});
		request('http://localhost:7865/cart/nope', (error, response, body) => {
			expect(response.statusCode).to.equal(404);
			done();
		});
	})
	it('Ensures /available_payments behavior', (done) => {
		request('http://localhost:7865/available_payments', (error, response, body) => {
			expect(response.statusCode).to.equal(200);
			expect(body).to.equal(
				'{"payment_methods":{"credit_cards":true,"paypal":false}}'
			);
			done();
		})
	})
	it('Ensures /login behavior', (done) => {
		request({
			method: 'POST',
			url: 'http://localhost:7865/login',
			json: {userName: 'Bean'}
		}, (error, response, body) => {
			expect(response.statusCode).to.equal(200);
			expect(body).to.equal('Welcome Bean');
			done();
		})
	})
})