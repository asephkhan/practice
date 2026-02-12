# Write your solution here
#def main():
#    while True:
#        user_entry = input("Exam points and excercises completed: ")
#        if user_entry == "":
#            print("Stats")            
#            break            
#main()
excercises = [87,60]
exam_points = [18, 14]

def completed_excercises_conversion(courses: list):
    excercises_points = []
    for excercises in courses:
        excercises_points.append(excercises//10)
    print("excercise points: ", excercises_points)
    return excercises_points

excercises_points = completed_excercises_conversion(excercises)

# function to calculate all points
def calculate_total_points(excercises_points: list, exam_points:list):
    total_points = []
    for points in range(len(excercises_points)):
        total_points.append(excercises_points[points] + exam_points[points])
    print("total points: ", total_points)    
    return total_points

total_points = calculate_total_points(excercises_points,exam_points)