# Write your solution here
# function to calculate exercises points
def completed_exercises_conversion(users: list):
    exercises_points = []
    for exercises in users:
        exercises_points.append(exercises//10)
    return exercises_points
    
# function to calculate all points
def calculate_total_points(exercises_points: list, exam_points:list):
    total_points = 0

    for points in range(len(exercises_points)):
        total_points += (exercises_points[points] + exam_points[points])    
    return total_points
    
# function to calculate average
def calculate_average_points(total_points, number_of_users):
    average = float(total_points/number_of_users)
    return average
# function to calculate percentage of passing students
def calculate_percentage_of_passing_students(passed_students: int, total_students: int):
    percentage = (passed_students* 100 )/total_students
    return percentage

def calculate_grades(exercises_points: list, exam_points:list):
    grades = []

    for points in range(len(exercises_points)):
        total_points = (exercises_points[points] + exam_points[points]) 
        if exam_points[points] < 10:
            grades.append(0)
        elif total_points >= 28:
            grades.append(5)
        elif total_points >= 24:
            grades.append(4)
        elif total_points >= 21:
            grades.append(3)
        elif total_points >= 18:
            grades.append(2)
        elif total_points >= 15:
            grades.append(1)
        else:
            grades.append(0)
    
    return grades


# function to print stats
def print_stats(average, percentage, grades):
    print("Statistics:")
    print(f"Points average:{average: .1f}")
    print(f"Pass percentage:{percentage: .1f}")
    total_grades = [5, 4, 3, 2, 1, 0]
    print(f"Grade distribution:"  )
    
    for grade in total_grades:
        stars = grades.count(grade) * "*"
        print(f" {grade}: {stars}")
        
    return

def main():
    exercises = []
    exam_points = []
    passed_students = 0
    while True:
        user_entry = input("Exam points and exercises completed: ")
        if user_entry == "" :
            exercises_points = completed_exercises_conversion(exercises) 
            total_points = calculate_total_points(exercises_points,exam_points)
            average = calculate_average_points(total_points, len(exam_points))
            percentage = calculate_percentage_of_passing_students(passed_students,len(exam_points))
            grades = calculate_grades(exercises_points,exam_points)            
            print_stats(average, percentage, grades)            
            break
        parts = user_entry.split()
        exam_points.append(int(parts[0]))   
        exercises.append(int(parts[1])) 
        if int(parts[0]) >= 10 and int(parts[0]) + (int(parts[1])//10) >= 15 :
            passed_students += 1
main()
