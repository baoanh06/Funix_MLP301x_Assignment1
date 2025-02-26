import re

def analyzeData(classExam):
    # Phân tích
    print("**** ANALYZING ****")
    validExam = 0
    invalidExam = 0

    for studentExam in classExam:
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

            invalidExam += 1
        else:
            validExam += 1

    if invalidExam == 0:
        print("No errors found!")

    print("**** REPORT ****")
    print("Total valid lines of data: ", validExam)
    print("Total invalid lines of data: ", invalidExam)

if __name__ == '__main__':
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")

    while filename != '-1':
        try:
            with open(filename+".txt", 'r') as file:
                print("Successfully opened {}.txt".format(filename))
                classData = file.readlines()
                analyzeData(classData)
        except FileNotFoundError:
            print("File cannot be found.")
        finally:
            filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")