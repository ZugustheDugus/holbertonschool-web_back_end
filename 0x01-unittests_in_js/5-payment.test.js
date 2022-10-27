// Tests for 3-payment.js
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./5-payment.js');
const sinon = require('sinon');

describe('sendPaymentRequestToApi', () => {
	let spyConsole;
	beforeEach(() => {
		spyConsole = sinon.spy(console, 'log');
	});
	afterEach(() => {
		spyConsole.restore();
	})
	it('Ensure console output & console only called once', () => {
		sendPaymentRequestToApi(100, 20);
		expect(spyConsole.calledWith('The total is: 120')).to.be.true;
		expect(spyConsole.calledOnce).to.be.true;
	});
	it('Ensure console output & console only called once', () => {
		sendPaymentRequestToApi(10, 10);
		expect(spyConsole.calledWith('The total is: 20')).to.be.true;
		expect(spyConsole.calledOnce).to.be.true;
	});
});