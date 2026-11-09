from student import Student
from decorators import require_student, require_active


class Decanat:
    def __init__(self):
        self.students = []
        self.departments = []
        self.faculties = []
        self.disciplines = []

    def _find_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def _find_discipline(self, name):
        for d in self.disciplines:
            if d.name == name:
                return d
        return None

    def _get_discipline(self, name):
        d = self._find_discipline(name)
        if d is None:
            raise ValueError(f"Discipline '{name}' does not exist")
        return d

    def add_student(self, student_id, name, specialty):
        if self._find_student(student_id) is not None:
            raise ValueError(f"Student with ID {student_id} already exists!")
        faculty = None
        for f in self.faculties:
            if specialty in f.specialties:
                faculty = f
                break
        if faculty is None:
            raise ValueError(f"No faculty offers specialty '{specialty}'")
        student = Student(student_id, name, specialty)
        student.faculty = faculty
        self.students.append(student)
        faculty.students.append(student)
        print(f"Student {name} (ID={student_id}) enrolled to {specialty}")

    @require_student
    def del_student(self, student):
        if not student.is_active:
            raise ValueError(f"Student with ID {student.id} is already expelled")
        student.is_active = False
        print(f"Student {student.id} expelled (record kept for reports)")

    @require_student
    def restore_student(self, student):
        if student.is_active:
            raise ValueError(f"Student with ID {student.id} is not expelled")
        student.is_active = True
        print(f"Student {student.id} restored")

    @require_student
    @require_active
    def add_discipline_to_student(self, student, discipline_name):
        d = self._get_discipline(discipline_name)
        if d in student.disciplines:
            raise ValueError(f"Student {student.id} is already enrolled in '{discipline_name}'")
        if student.specialty not in d.allowed_specialties:
            raise ValueError(f"Discipline '{discipline_name}' is not taught for specialty '{student.specialty}'")
        student.disciplines.append(d)
        student.grades[d.name] = None
        print(f"Student {student.id} enrolled in '{discipline_name}'")

    @require_student
    @require_active
    def del_discipline_from_student(self, student, discipline_name):
        d = self._get_discipline(discipline_name)
        if d not in student.disciplines:
            raise ValueError(f"Student {student.id} is not enrolled in '{discipline_name}'")
        student.disciplines.remove(d)
        student.grades.pop(d.name, None)
        print(f"Student {student.id} removed from '{discipline_name}'")

    @require_student
    @require_active
    def set_grade(self, student, discipline_name, grade):
        d = self._get_discipline(discipline_name)
        if d not in student.disciplines:
            raise ValueError(f"Student {student.id} is not enrolled in '{discipline_name}'")
        if grade < 2 or grade > 5:
            raise ValueError(f"Grade must be between 2 and 5, got {grade}")
        student.grades[d.name] = grade
        print(f"Grade {grade} set for student {student.id} in '{discipline_name}'")

    @require_student
    @require_active
    def transfer_to_next(self, student):
        for name, grade in student.grades.items():
            if grade is None:
                raise ValueError(f"Cannot transfer: '{name}' has no grade")
            if grade < 4:
                raise ValueError(f"Cannot transfer: '{name}' has grade {grade} (debt)")
        student.semester = student.semester + 1
        student.disciplines.clear()
        student.grades.clear()
        print(f"Student {student.id} transferred to semester {student.semester}")

    @require_student
    def generate_student_report(self, student, filename=None):
        if filename is None:
            filename = f"student_{student.id}_report.txt"
        lines = []
        lines.append("STUDENT GRADE REPORT")
        lines.append(f"ID:         {student.id}")
        lines.append(f"Name:       {student.name}")
        lines.append(f"Specialty:  {student.specialty}")
        lines.append(f"Semester:   {student.semester}")
        lines.append(f"Status:     {student.status}")
        lines.append("Disciplines:")
        if not student.disciplines:
            lines.append("  no disciplines")
        for d in student.disciplines:
            g = student.grades.get(d.name)
            lines.append(f"  {d.name}  [department: {d.department_name}]")
            if g is None:
                lines.append("      grade: not graded")
            else:
                lines.append(f"      grade: {g}")
        lines.append(f"Average grade: {student.average_grade:.2f}")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Report saved to '{filename}'")

    def generate_discipline_report(self, discipline_name, filename=None):
        d = self._get_discipline(discipline_name)
        if filename is None:
            safe = ""
            for c in discipline_name:
                if c.isalnum():
                    safe = safe + c
                else:
                    safe = safe + "_"
            filename = f"discipline_{safe}_report.txt"

        graded = []
        pending = []
        total = 0
        count = 0
        for s in self.students:
            if d in s.disciplines:
                g = s.grades.get(d.name)
                if g is None:
                    pending.append(s)
                else:
                    graded.append((s, g))
                    total = total + g
                    count = count + 1
        if count == 0:
            avg = 0.0
        else:
            avg = total / count

        lines = []
        lines.append("DISCIPLINE GRADE REPORT")
        lines.append(f"Discipline:          {d.name}")
        lines.append(f"Reading department:  {d.department_name}")
        lines.append(f"Allowed specialties: {d.formatted_specialties}")
        lines.append("Completed (graded):")
        if not graded:
            lines.append("  none")
        for s, g in graded:
            lines.append(f"  {s.name} (ID={s.id}): {g}")
        lines.append("Currently enrolled (not graded):")
        if not pending:
            lines.append("  none")
        for s in pending:
            lines.append(f"  {s.name} (ID={s.id})")
        lines.append(f"Average grade: {avg:.2f}")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Report saved to '{filename}'")