class Faculty:
    def __init__(self, name="RFICT", specialties=None, departments=None, students=None):
        self.name = name
        self.specialties = specialties if specialties is not None else []
        self.departments = departments if departments is not None else []
        self.students = students if students is not None else []

    def __repr__(self):
        return f"Faculty({self.name!r}, specialties={self.specialties})"