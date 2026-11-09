from decanat import Decanat
from faculty import Faculty
from department import Department
from discipline import Discipline


def setup_demo(dc):
    faculty = Faculty("RFICT")
    dc.faculties.append(faculty)

    dept_pi = Department("Applied Informatics")
    dept_cs = Department("Cybersecurity")
    dept_math = Department("Mathematics")
    dc.departments.append(dept_pi)
    dc.departments.append(dept_cs)
    dc.departments.append(dept_math)
    faculty.departments.append(dept_pi)
    faculty.departments.append(dept_cs)
    faculty.departments.append(dept_math)

    faculty.specialties.append("Applied Informatics")
    faculty.specialties.append("Cybersecurity")

    disciplines = [
        Discipline("Programming", dept_pi, ["Applied Informatics", "Cybersecurity"]),
        Discipline("Databases", dept_pi, ["Applied Informatics"]),
        Discipline("Cryptography", dept_cs, ["Cybersecurity"]),
        Discipline("Linear Algebra", dept_math, ["Applied Informatics", "Cybersecurity"]),
        Discipline("Networks", dept_cs, ["Applied Informatics", "Cybersecurity"]),
    ]
    for d in disciplines:
        dc.disciplines.append(d)
        d.department.add_discipline(d)



operations = {
    1: "Enroll in discipline",
    2: "Remove from discipline",
    3: "Set grade",
    4: "Transfer to next semester",
    5: "Save student report to file",
    6: "Expel student",
    7: "Restore student",
    0: "Back",
}


def main():
    dc = Decanat()
    setup_demo(dc)

    while True:
        print("\nMAIN MENU")
        print(" 1. Enroll new student")
        print(" 2. Work with student by ID")
        print(" 3. Discipline report to file")
        print(" 4. Show all students")
        print(" 5. Show all disciplines")
        print(" 0. Exit")
        choice = input("Choice: ").strip()

        if choice == "0":
            print("Bye!")
            break

        if choice == "1":
            try:
                sid = int(input("Student ID: "))
            except ValueError:
                print("Bad ID")
                continue
            name = input("Name: ")
            spec = input("Specialty: ")
            try:
                dc.add_student(sid, name, spec)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                sid = int(input("Student ID: "))
            except ValueError:
                print("Bad ID")
                continue
            if dc._find_student(sid) is None:
                print("Student not found")
                continue
            while True:
                s = dc._find_student(sid)
                if s is None:
                    break
                print(f"\nStudent: {s.name} (ID: {s.id}, Specialty: {s.specialty}, Semester: {s.semester}, {s.status})")
                for key, text in operations.items():
                    print(key, text)
                try:
                    op = int(input("Choice: "))
                except ValueError:
                    print("Bad command")
                    continue
                try:
                    if op == 1:
                        dc.add_discipline_to_student(sid, input("Discipline: "))
                    elif op == 2:
                        dc.del_discipline_from_student(sid, input("Discipline: "))
                    elif op == 3:
                        name_d = input("Discipline: ")
                        try:
                            g = int(input("Grade (1-10): "))
                        except ValueError:
                            print("Bad grade")
                            continue
                        dc.set_grade(sid, name_d, g)
                    elif op == 4:
                        dc.transfer_to_next(sid)
                    elif op == 5:
                        dc.generate_student_report(sid)
                    elif op == 6:
                        dc.del_student(sid)
                    elif op == 7:
                        dc.restore_student(sid)
                    elif op == 0:
                        break
                    else:
                        print("Bad command")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "3":
            try:
                dc.generate_discipline_report(input("Discipline: "))
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            if not dc.students:
                print("no students")
            for s in dc.students:
                print(f"  {s}")

        elif choice == "5":
            if not dc.disciplines:
                print("no disciplines")
            for d in dc.disciplines:
                print(f"  {d}")

        else:
            print("Bad command")


if __name__ == "__main__":
    main()