class Student:
    def __init__(self, student_id, name, specialty, semester=1, is_active=True):
        if student_id <= 0:
            raise ValueError("ID must be positive")
        self.id = student_id
        self.name = name
        self.specialty = specialty
        self.semester = semester
        self.is_active = is_active
        self.disciplines = []
        self.grades = {}
        self.faculty = None

    @property
    def status(self):
        if self.is_active:
            return "active"
        return "expelled"

    @property
    def average_grade(self):
        total = 0
        count = 0
        for grade in self.grades.values():
            if grade is not None:
                total = total + grade
                count = count + 1
        if count == 0:
            return 0.0
        return total / count

    @property
    def can_transfer(self):
        if not self.is_active:
            return False
        for grade in self.grades.values():
            if grade is None:
                return False
            if grade < 4:
                return False
        return True

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name!r}, specialty={self.specialty!r}, sem={self.semester}, {self.status})"