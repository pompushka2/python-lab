class Department:
    def __init__(self, name="Unknown"):
        self.name = name
        self.disciplines = []

    def add_discipline(self, discipline):
        if discipline not in self.disciplines:
            self.disciplines.append(discipline)
        discipline.department = self

    def __repr__(self):
        return f"Department({self.name!r}, {len(self.disciplines)} disciplines)"