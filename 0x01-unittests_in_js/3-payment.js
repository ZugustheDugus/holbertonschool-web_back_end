// Function that takes two arguments and uses calculateNumber
const Utils = require('./utils.js')

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
	const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
	console.log(`The total is: ${total}`);
}

module.exports = sendPaymentRequestToApi;