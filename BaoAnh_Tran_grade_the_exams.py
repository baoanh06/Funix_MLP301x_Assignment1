import numpy as np
import re

# Kiểm tra dữ liệu
def verify_data(class_exam):
    print("**** ANALYZING ****")
    num_valid_exam = 0
    num_invalid_exam = 0

    for student_exam in class_exam[:]:
        exam = student_exam.split(',')
        student_id = exam[0]
        student_answer = exam[1:len(exam)]

        if len(student_answer) != 25 or re.search("^N[0-9]{8}", student_id) is None:
            if len(student_answer) != 25:
                print("Invalid line of data: does not contain exactly 26 values:\n")
                print(student_exam)

            if re.search("^N[0-9]{8}", student_id) is None:
                print("Invalid line of data: N# is invalid:\n")
                print(student_exam)

            num_invalid_exam += 1
            class_exam.remove(student_exam)
        else:
            num_valid_exam += 1

    if num_invalid_exam == 0:
        print("No errors found!")

    return num_valid_exam, num_invalid_exam, class_exam

# Chấm bài
def marking_grade(valid_exams):
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_list = answer_key.split(',')

    class_results = []
    grade_list = []

    for student_exam in valid_exams:
        exam = student_exam.split(',')
        student_id = exam[0]
        student_answer = exam[1:len(exam)]

        score = 0

        for i in range(0, len(student_answer)):
            if student_answer[i] == answer_list[i]:
                score += 4
            elif student_answer[i] == '':
                continue
            else:
                score -= 1

        student_result = ','.join([student_id, str(score)]) + '\n'

        class_results.append(student_result)
        grade_list.append(score)

    print(grade_list)
    return class_results, grade_list

# Báo cáo kết quả
def report(num_valid_exam, num_invalid_exam, score_list):
    print("**** REPORT ****")
    print("Total valid lines of data: ", num_valid_exam)
    print("Total invalid lines of data: ", num_invalid_exam)
    print("Mean (average) score: ", np.mean(score_list))
    print("Highest score: ", np.max(score_list))
    print("Lowest score: ", np.min(score_list))
    print("Range of scores: ", np.max(score_list) - np.min(score_list))
    print("Median score: ", np.median(score_list))

# Lưu kết quả vào file
def output_file (filename, class_results):
    with open("Expected Output/" + filename + "_grades.txt", 'w') as file:
        file.writelines(class_results)

if __name__ == '__main__':
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")

    while filename != '-1':
        try:
            with open(filename + ".txt", 'r') as file:
                print("Successfully opened {}.txt".format(filename))
                class_data = file.readlines()

                num_valid_exam, num_invalid_exam, verified_class_exam = verify_data(class_data)
                class_results, class_grade_list = marking_grade(verified_class_exam)
                report(num_valid_exam, num_invalid_exam, class_grade_list)
                output_file(filename, class_results)
        except FileNotFoundError:
            print("File cannot be found.")
        finally:
            filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")