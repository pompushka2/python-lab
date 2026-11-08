class Discipline:
    def __init__(self, name="Python", department=None, allowed_specialties=None):
        self.name = name
        self.department = department
        self.allowed_specialties = allowed_specialties if allowed_specialties is not None else []

    def get_name(self):
        return self.name

    def get_allowed_specialties(self):
        return self.allowed_specialties

    def get_department(self):
        return self.department

    def set_name(self, name):
        self.name = name

    def set_department(self, department):
        self.department = department

    def set_allowed_specialties(self, specialties):
        self.allowed_specialties = specialties

    def __repr__(self):
        dept = self.department.name if self.department else "None"
        specs = ", ".join(self.allowed_specialties) or "-"
        return f"Discipline({self.name!r}, dept={dept}, specialties=[{specs}])"