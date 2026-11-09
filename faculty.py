class Faculty:
    def __init__(self, name="RFICT", specialties=None, departments=None, students=None):
        self.name = name
        if specialties is None:
            self.specialties = []
        else:
            self.specialties = specialties
        if departments is None:
            self.departments = []
        else:
            self.departments = departments
        if students is None:
            self.students = []
        else:
            self.students = students

    def __repr__(self):
        return f"Faculty({self.name!r}, specialties={self.specialties})"