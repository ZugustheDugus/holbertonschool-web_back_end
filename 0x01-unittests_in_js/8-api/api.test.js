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
})