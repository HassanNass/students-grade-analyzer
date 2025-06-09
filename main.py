
def student_name_grade():
    students = []
    grades = []
    
    while True:
        name = input("Enter the name of the student(enter 'done' if finished): ")
        if name.lower() == "done":
            break
        else:
            grade = int(input("Enter the grade of the student (out of 100): "))
            if grade < 0 or grade > 100:
                print("Invalid input. The grade must be out of 100.")
            else:
                students.append(name)
                grades.append(grade)

    return students, grades


def display_student_summary(students, grades):
    for i in range(len(students)):
        print(f"{students[i]}: {grades[i]}")


def get_avg_grade(students, grades):
    nb_of_students = len(students)
    total = sum(grades)
    average = total / nb_of_students
    return average


def get_heighest_grade(students, grades):
    index = 0
    for i in range(1, len(grades)):
        if grades[i] > grades[index]:
            index = i

    return students[index], grades[index]


def count_passed(students, grades):
    passed = 0
    for grade in grades:
        if grade >= 60:
            passed += 1
    return passed