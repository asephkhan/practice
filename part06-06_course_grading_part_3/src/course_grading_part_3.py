# tee ratkaisu tänne
# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points1 = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points1 = "exam_points1.csv"

students = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = sum(int(value) for value in parts[1:])


exam_points = {}
with open(exam_points1) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exam_points[parts[0]] = sum(int(value) for value in parts[1:])
print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")
for student_id, exercise in exercises.items():
    if student_id in exam_points and student_id in students:
        exercise_points = exercises[student_id] // 4
        total_points = int(exercise_points) + exam_points[student_id]
        if total_points >= 28:
            grade = 5
        elif total_points >= 24:
            grade = 4
        elif total_points >= 21:
            grade = 3
        elif total_points >= 18:
            grade = 2
        elif total_points >= 15:
            grade = 1
        else:
            grade = 0
        print(f"{students[student_id]:30}{exercises[student_id]:<10}{exercise_points:<10}{exam_points[student_id]:<10}{total_points:<10}{grade:<10}")