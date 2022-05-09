/* eslint no-underscore-dangle: ["error", { "allowAfterThis": true }] */

export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) === 'string') {
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }

    if (typeof (length) === 'number') {
      this._length = length;
    } else {
      throw TypeError('Length must be a number');
    }

    if (students.some((element) => (typeof (element) === 'string'))) {
      this.students = students;
    } else {
      throw TypeError('length must be a array of strings');
    }
  }

  set name(name) {
    if (typeof (name) === 'string') {
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  set length(length) {
    if (typeof (length) === 'number') {
      this._length = length;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  set studetns(students) {
    if (typeof (students) === 'string') {
      this._students = students;
    } else {
      throw TypeError('Students must be a string');
    }
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }
}
