import numpy as np
import re

# Kiểm tra dữ liệu
def verifyData(classExam):
    print("**** ANALYZING ****")
    numValidExam = 0
    numInvalidExam = 0

    for studentExam in classExam[:]:
        exam = studentExam.split(',')
        studentId = exam[0]
        studentAnswer = exam[1:len(exam)]

        if len(studentAnswer) != 25 or re.search("^N[0-9]{8}", studentId) is None:
            if len(studentAnswer) != 25:
                print("Invalid line of data: does not contain exactly 26 values:\n")
                print(studentExam)

            if re.search("^N[0-9]{8}", studentId) is None:
                print("Invalid line of data: N# is invalid:\n")
                print(studentExam)

            numInvalidExam += 1
            classExam.remove(studentExam)
        else:
            numValidExam += 1

    if numInvalidExam == 0:
        print("No errors found!")

    return numValidExam, numInvalidExam, classExam

# Chấm bài
def markingScore(validExams):
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_list = answer_key.split(',')

    scoreList = []

    for studentExam in validExams:
        exam = studentExam.split(',')
        studentAnswer = exam[1:len(exam)]

        score = 0

        for i in range(0, len(studentAnswer)):
            if studentAnswer[i] == answer_list[i]:
                score += 4
            elif studentAnswer[i] == '':
                continue
            else:
                score -= 1

        scoreList.append(score)

    return scoreList

# Báo cáo kết quả
def report(numValidExam, numInvalidExam, scoreList):
    print("**** REPORT ****")
    print("Total valid lines of data: ", numValidExam)
    print("Total invalid lines of data: ", numInvalidExam)
    print("Mean (average) score: ", np.mean(scoreList))
    print("Highest score: ", np.max(scoreList))
    print("Lowest score: ", np.min(scoreList))
    print("Range of scores: ", np.max(scoreList) - np.min(scoreList))
    print("Median score: ", np.median(scoreList))

if __name__ == '__main__':
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")

    while filename != '-1':
        try:
            with open(filename + ".txt", 'r') as file:
                print("Successfully opened {}.txt".format(filename))
                classData = file.readlines()

                numValidExam, numInvalidExam, verifiedClassExam = verifyData(classData)
                classGrade = markingScore(verifiedClassExam)
                report(numValidExam,numInvalidExam,classGrade)
        except FileNotFoundError:
            print("File cannot be found.")
        finally:
            filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")