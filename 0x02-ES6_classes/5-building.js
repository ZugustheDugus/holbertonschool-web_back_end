/* eslint no-underscore-dangle: ["error", { "allowAfterThis": true }] */
export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
    if (!this.evacuationWarningMessage && this.constructor !== Building) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
