// A function that reads a database.csv file asynchronosly
const countStudents = require('../3-read_file_async');

function readDatabase(path) {
  return countStudents(path);
}

module.exports = readDatabase;
