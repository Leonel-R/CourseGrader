def user_in():
    student_file = input("Student information:")
    exercise_file = input("Exercises completed:")
    exam_file = input("Exam points:")
    return student_file,exercise_file, exam_file

def collect_data_from_files(student_file,exercise_file,exam_file):
    student_names = {}
    exercise_scores = {}
    exam_scores = {}
    with open(student_file) as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            student_names[parts[0]] = parts[1]+" "+parts[2]
        
    with open(exercise_file) as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            convert = [eval(num) for num in parts[1:]]
            exercise_scores[parts[0]] = convert
        
    with open(exam_file) as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id":
                continue
            convert = [eval(num) for num in parts[1:]]
            exam_scores[parts[0]] = convert
        return student_names, exercise_scores, exam_scores
    
def point_total_calc(student_names,exercise_scores,exam_scores):
    point_totals = {}
    for id, name in student_names.items():
        if id in exercise_scores and id in exam_scores:
            point_total = (sum(exercise_scores[id])//4) + sum(exam_scores[id])
        point_totals[id] = point_total
    return point_totals
        
            
def create_points_table(student_names, exercise_scores,exam_scores, point_totals):
    print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade'}")
    for id, name in student_names.items():
        if id in point_totals:
            if point_totals[id] <= 14:
                grade = 0
            elif point_totals[id] <= 17:
                grade = 1
            elif point_totals[id] <= 20:
                grade = 2
            elif point_totals[id] <= 23:
                grade = 3
            elif point_totals[id] <= 27:
                grade = 4
            elif point_totals[id] >= 28:
                grade = 5
            print(f"{name:30}{sum(exercise_scores[id]):<10}{sum(exercise_scores[id])//4:<10}{sum(exam_scores[id]):<10}{point_totals[id]:<10}{grade:<10}")

                      


def main():
    student_file,exercise_file,exam_file = user_in() 
    student_names,exercise_scores, exam_scores = collect_data_from_files(student_file,exercise_file,exam_file)
    point_totals = point_total_calc(student_names,exercise_scores,exam_scores)
    create_points_table(student_names, exercise_scores,exam_scores, point_totals)

main()
