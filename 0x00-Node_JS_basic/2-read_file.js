// Logs # of students in each field of database file

const fs = require('fs');

const countStudents = (path) => {
  let students;
  try {
    students = fs.readFileSync(path, 'utf-8');
  } catch (error) {
    throw Error('Cannot load the database');
  }
  const lines = students.split('\n').slice(1).filter((line) => line !== '');
  console.log(`Number of students: ${lines.length}`);
  const fields = [...new Set(lines.map((line) => line.split(',')[3]))];
  fields.forEach((field) => {
    const studentsInField = lines.filter((line) => line.endsWith(field))
      .map((line) => line.split(',')[0]);
    console.log(
      `Number of students in ${field}: ${
        studentsInField.length
      }. List: ${studentsInField.join(', ')}`,
    );
  });
};

module.exports = countStudents;
