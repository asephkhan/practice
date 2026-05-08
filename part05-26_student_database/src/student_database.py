def add_student(students: dict, name: str ):    
    if name not in students:
        students[name] = []
    
def add_course(students: dict, name: str, course_details):
    if course_details[1] == 0:
        return
    for course in students[name]:
        if course_details[0] in course and course_details[1] <= course[1]:
            return
        elif course_details[0] in course and course_details[1] > course[1]:
            students[name].remove(course)
            return students[name].append(course_details)
    else:            
        students[name].append(course_details)


def print_student(students: dict, name:str):
    if name in students:
        print(f"{name}:")
        if len(students[name]) > 0:
            print(f" {len(students[name])} completed courses:") 
            total_grade = 0       
            for course in students[name]:
                print(f"  {course[0]} {course[1]} ")
                total_grade = total_grade + course[1]
            average_grade = total_grade/len(students[name])
            print(f" average grade {average_grade}")
        else:
            print(f" no completed courses")


    if name not in students:
        print(f"{name}: no such person in the database")

def summary(students: dict):
    print(f"students {len(students)}")
    max_courses = 0
    max_courses_student_name = ''
#    best average = 0
    for name, student_courses in students.items():
        if student_courses > max_courses:
            max_courses = students_courses
            name = max_courses_student_name 
            print(f"{name} {max_courses}")
#print(len(students[name]))
    




if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Advanced Course in Programming", 3))
    print_student(students, "Peter")
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
    
    