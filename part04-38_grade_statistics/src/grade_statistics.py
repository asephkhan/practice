# Write your solution here
# function to calculate excercises points
def completed_excercises_conversion(users: list):
    excercises_points = []
    for excercises in users:
        excercises_points.append(excercises//10)
    return excercises_points
    
# function to calculate all points
def calculate_total_points(excercises_points: list, exam_points:list):
    total_points = 0

    for points in range(len(excercises_points)):
        total_points += (excercises_points[points] + exam_points[points])    
    return total_points
    
# function to calculate average
def calculate_average_points(total_points, number_of_users):
    average = float(total_points/number_of_users)
    return average
# function to calculate percentage of passing students
def calculate_percentage_of_passing_students(passed_students: int, total_students: int):
    percentage = (passed_students* 100 )/total_students
    return percentage

def calculate_grades(excercises_points: list, exam_points:list):
    grades = []

    for points in range(len(excercises_points)):
        total_points = (excercises_points[points] + exam_points[points]) 
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
        elif total_points >= 14:
            grades.append(1)
        else:
            grades.append(0)
    
    return grades


# function to print stats
def print_stats(average, percentage, grades):
    print("Average points:", average)
    print("Percentage:", percentage)
    print("Grade Statistcs:", grades)
    return

def main():
    excercises = []
    exam_points = []
    passed_students = 0
    while True:
        user_entry = input("Exam points and excercises completed: ")
        if user_entry == "":
            excercises_points = completed_excercises_conversion(excercises) 
            total_points = calculate_total_points(excercises_points,exam_points)
            average = calculate_average_points(total_points, len(exam_points))
            percentage = calculate_percentage_of_passing_students(passed_students,len(exam_points))
            grades = calculate_grades(excercises_points,exam_points)            
            print_stats(average, percentage, grades)            
            break
        parts = user_entry.split()
        exam_points.append(int(parts[0]))   
        excercises.append(int(parts[1])) 
        if int(parts[0]) >= 10 and int(parts[0]) + (int(parts[1])//10) >= 15 :
            passed_students += 1
main()
