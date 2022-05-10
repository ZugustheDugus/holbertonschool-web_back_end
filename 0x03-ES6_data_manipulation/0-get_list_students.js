const students = [
  { id: 1, firstName: 'Guillaume', location: 'San Fransisco' },
  { id: 2, firstName: 'James', location: 'Columbia' },
  { id: 5, firstName: 'Serena', location: 'San Fransisco' },
];

export default function getListStudents(student) {
  return [student.id, student.firstName, student.location].join(' ');
}

students.map(getListStudents);
