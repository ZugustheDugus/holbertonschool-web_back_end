// Module for Utils
const Utils = {
	calculateNumber(type, a, b) {
		if (isNaN(a) || isNaN(b)) throw new TypeError("a and b must be numbers");
		type = type.toUpperCase();
		if (type === 'SUM') {
			return Math.round(a) + Math.round(b);
		} else if (type === 'SUBTRACT') {
			return Math.round(a) - Math.round(b);
		} else if (type === 'DIVIDE') {
			if (Math.round(b) === 0) {
				return 'Error';
			} else {
				return Math.round(a) / Math.round(b);
			}
		} else {
			throw new TypeError("type must be; SUM, SUBTRACT, or DIVIDE");
		};
	}
};

module.exports = Utils;