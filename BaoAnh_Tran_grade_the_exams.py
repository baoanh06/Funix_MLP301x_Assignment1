def analyzeData(studentExam):
    return

if __name__ == '__main__':
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")

    try:
        with open(filename+".txt", 'r') as classfile:
            print("Successfully opened {}.txt", filename)
            student = classfile.readline()
            analyzeData(student)
    except FileNotFoundError:
        print("File cannot be found.")