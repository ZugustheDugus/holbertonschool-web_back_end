/* eslint no-underscore-dangle: ["error", { "allowAfterThis": true }] */
export default class Currency {
  constructor(code, name) {
    if (typeof (code) === 'string') {
      this._code = code;
    }
    if (typeof (name) === 'string') {
      this._name = name;
    }
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof (name) === 'string') {
      this._name = name;
    }
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof (code) === 'string') {
      this._code = code;
    }
  }

  displayFullCurrency() {
    return (`${this._name} (${this._code})`);
  }
}
