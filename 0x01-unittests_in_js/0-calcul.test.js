// Tests for 0-calcul.js
const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
	it('Tests positive ints and floats', () => {
		assert.equal(calculateNumber(2, 2), 4);
		assert.equal(calculateNumber(1.5, 1.5), 4);
		assert.equal(calculateNumber(1.5, 2), 4);
		assert.equal(calculateNumber(2, 1.5), 4);
	});
	it('Tests negative ints and floats', () => {
		assert.equal(calculateNumber(-2, -2), -4);
		assert.equal(calculateNumber(-2.5, -2.5), -4);
		assert.equal(calculateNumber(-2.5, -2), -4);
		assert.equal(calculateNumber(-2, -2.5), -4);
	});
	it('Tests TypeError', () => {
		assert.throws(() => calculateNumber(2, 'b'), TypeError);
		assert.throws(() => calculateNumber(NaN, 2), TypeError);
	});
});