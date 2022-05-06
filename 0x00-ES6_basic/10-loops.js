export default function appendToEachArrayValue(array, appendString) {
  const newarray = [];
  for (const idx of array) {
    newarray.push(appendString + idx);
  }

  return newarray;
}
