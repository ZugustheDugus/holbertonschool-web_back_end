// Controller for "/students" route
const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2]).then((data) => {
      response.write('This is the list of our students\n');
      const textLines = data.split('\n').slice(1);
      const textBlock = textLines.join('\n');
      response.end(textBlock);
    })
      .catch((error) => response.status(500).end(error.message));
  }

  static getAllStudentsByMajor(request, response) {
    readDatabase(process.argv[2]).then((data) => {
      const { major } = request.params;
      if (!['CS', 'SWE'].includes(major)) {
        response.status(500).end('Major parameter must be CS or SWE');
      }
      const infoDict = {};
      let lines = data.split('\n');
      lines = lines.slice(1);
      const keys = [];
      const values = [];
      lines.forEach((line) => {
        const items = line.split('.');
        values.push(items[1].slice(1));
        keys.push(items[0].split(' ')[4].slice(0, -1));
      });
      keys.forEach((key, x) => {
        infoDict[key] = values[x];
      });
      for (const [field, studList] of Object.entries(infoDict)) {
        if (major === field) {
          response.end(studList);
        }
      }
    })
      .catch((error) => response.status(500).end(error.message));
  }
}

module.exports = StudentsController;
