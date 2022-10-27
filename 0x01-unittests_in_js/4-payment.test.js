// Tests for 4-payment.js
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./4-payment.js');
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () => {
	it('Ensure that sendPayment... is using calculateNumber', () => {
		const spyConsole = sinon.spy(console, 'log');
		const stubUtils = sinon.stub(Utils, 'calculateNumber').returns(10);
		sendPaymentRequestToApi(100, 20);
		expect(stubUtils.calledWith('SUM', 100, 20)).to.be.true;
		expect(spyConsole.calledWith('The total is: 10')).to.be.true;
		spyConsole.restore();
		stubUtils.restore();
	});
});