export default function getStudentIdsSum(studentList) {
  return studentList.reduce((total, num) => total + num.id, 0);
}
