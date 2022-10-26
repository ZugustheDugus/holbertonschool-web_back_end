// Tests for 1-calcul.js
const calculateNumber = require('./1-calcul.js');
const expect = require('chai').expect;

describe('calculateNumber', () => {
	it('Testing positive numbers and non-capital letters', () => {
		expect(calculateNumber('SUM', 2, 2)).to.equal(4);
		expect(calculateNumber('divide', 2, 2)).to.equal(1);
		expect(calculateNumber('SubTract', 2, 2)).to.equal(0);
		expect(calculateNumber('SUM', 1.5, 1.5)).to.equal(4);
		expect(calculateNumber('SUM', 1.5, 2)).to.equal(4);
		expect(calculateNumber('SUM', 2, 1.5)).to.equal(4);
	});
	it('Testing negative numbers and non-capital letters', () => {
		expect(calculateNumber('SUM', -2, -2)).to.equal(-4);
		expect(calculateNumber('suBtrAct', -2, -6)).to.equal(4);
		expect(calculateNumber('divide', -16, -4)).to.equal(4);
		expect(calculateNumber('SUM', -2.5, -2.5)).to.equal(-4);
		expect(calculateNumber('SUM', -2.5, -2)).to.equal(-4);
		expect(calculateNumber('SUM', -2, -2.5)).to.equal(-4);
	});
	it('Testing errors', () => {
		expect(() => calculateNumber('NOPE', 2, 2)).to.throw(TypeError);
		expect(calculateNumber('DIVIDE', 2, 0)).to.equal('Error');
		expect(() => calculateNumber(2, 'b')).to.throw(TypeError);
		expect(() => calculateNumber(NaN, 2)).to.throw(TypeError);
	});
});
