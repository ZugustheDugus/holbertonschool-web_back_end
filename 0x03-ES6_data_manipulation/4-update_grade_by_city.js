export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      const stuGrade = newGrades.filter((grade) => grade.studentId === student.id);
      const grade = stuGrade.length ? stuGrade[0].grade : 'N/A';
      return { ...student, grade };
    });
}
