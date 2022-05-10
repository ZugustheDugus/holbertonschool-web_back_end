/* eslint no-underscore-dangle: ["error", { "allowAfterThis": true }] */
export default class Airport {
  constructor(name, code) {
    if (typeof (name) === 'string') this._name = name;
    if (typeof (code) === 'number') this._code = code;
  }

  toString() {
    return `[${typeof this} ${this._code}]`;
  }
}
