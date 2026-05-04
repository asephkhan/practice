def add_student(students: dict, name: str ):    
    if name not in students:
        students[name] = []
    
def add_course(students: dict, name: str, course_details):
    if name in students:
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
    print_student(students, "Peter")
    
    