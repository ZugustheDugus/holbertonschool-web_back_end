// Tests for 6-payment_token.js
const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', () => {
	it('Ensures function returns new Promise', (done) => {
		getPaymentTokenFromAPI(true).then((response) => {
			expect(response.data).to.equal('Successful response from the API');
			done();
		});
	});
});