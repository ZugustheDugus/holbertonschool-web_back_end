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
})