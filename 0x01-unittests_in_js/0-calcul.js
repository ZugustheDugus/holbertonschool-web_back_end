// Simple function to calculate a sum

const calculateNumber = (a,b) => {
  if (isNaN(a) || isNaN(b)) throw new TypeError("a & b must be numbers");
  return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;