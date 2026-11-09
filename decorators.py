import functools


def require_student(func):
    @functools.wraps(func)
    def wrapper(self, student_id, *args, **kwargs):
        student = self._find_student(student_id)
        if student is None:
            raise ValueError(f"Student with ID {student_id} does not exist")
        return func(self, student, *args, **kwargs)
    return wrapper


def require_active(func):
    @functools.wraps(func)
    def wrapper(self, student, *args, **kwargs):
        if not student.is_active:
            raise ValueError(f"Student with ID {student.id} is expelled")
        return func(self, student, *args, **kwargs)
    return wrapper