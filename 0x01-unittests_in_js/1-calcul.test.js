// Tests for 1-calcul.js
const calculateNumber = require('./1-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
	it('Testing positive numbers and non-capital letters', () => {
		assert.equal(calculateNumber('SUM', 2, 2), 4);
		assert.equal(calculateNumber('divide', 2, 2), 1);
		assert.equal(calculateNumber('SubTract', 2, 2), 0);
		assert.equal(calculateNumber('SUM', 1.5, 1.5), 4);
		assert.equal(calculateNumber('SUM', 1.5, 2), 4);
		assert.equal(calculateNumber('SUM', 2, 1.5), 4);
	});
	it('Testing negative numbers and non-capital letters', () => {
		assert.equal(calculateNumber('SUM', -2, -2), -4);
		assert.equal(calculateNumber('suBtrAct', -2, -6), 4);
		assert.equal(calculateNumber('divide', -16, -4), 4);
		assert.equal(calculateNumber('SUM', -2.5, -2.5), -4);
		assert.equal(calculateNumber('SUM', -2.5, -2), -4);
		assert.equal(calculateNumber('SUM', -2, -2.5), -4);
	});
	it('Testing errors', () => {
		assert.throws(() => calculateNumber('NOPE', 2, 2), TypeError);
		assert.equal(calculateNumber('DIVIDE', 2, 0), 'Error');
		assert.throws(() => calculateNumber(2, 'b'), TypeError);
		assert.throws(() => calculateNumber(NaN, 2), TypeError);
	});
});
