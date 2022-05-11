export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      const stGrade = newGrades.filter((grade) => grade.studentId === student.id);
      const grade = stGrade.length ? stGrade[0].grade : 'N/A';
      return { ...student, grade };
    });
}
