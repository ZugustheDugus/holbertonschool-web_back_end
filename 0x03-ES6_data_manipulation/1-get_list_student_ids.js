export default function getListStudentIds(stulist) {
  try {
    return stulist.map((mapped) => mapped.id);
  } catch (error) {
    return [];
  }
}
