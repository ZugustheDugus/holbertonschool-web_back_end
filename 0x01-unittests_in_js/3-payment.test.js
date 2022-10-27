// Tests for 3-payment.js
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./3-payment.js');
const sinon = require('sinon');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () => {
	it('Ensure that sendPayment... is using calculateNumber', () => {
		const spyUtils = sinon.spy(Utils, 'calculateNumber');
		sendPaymentRequestToApi(2, 2);
		expect(spyUtils.calledWith('SUM', 2, 2)).to.be.true;
		spyUtils.restore();
	});
});