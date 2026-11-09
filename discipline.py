class Discipline:
    def __init__(self, name="Python", department=None, allowed_specialties=None):
        self.name = name
        self.department = department
        if allowed_specialties is None:
            self.allowed_specialties = []
        else:
            self.allowed_specialties = allowed_specialties

    @property
    def department_name(self):
        if self.department is None:
            return "none"
        return self.department.name

    @property
    def formatted_specialties(self):
        if not self.allowed_specialties:
            return "none"
        return ", ".join(self.allowed_specialties)

    def __repr__(self):
        return f"Discipline({self.name!r}, dept={self.department_name}, specialties=[{self.formatted_specialties}])"