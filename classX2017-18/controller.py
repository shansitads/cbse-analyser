from FileManager import FileManager
import os

# student list contains student data type elements
studentList = []
dataManager = FileManager()

filepath = input("Enter the path of your file: ").strip()
assert os.path.exists(filepath), "Did not find the file at, "+str(filepath)
print("Your file was found!")

filename = os.path.splitext(os.path.basename(filepath))[0]

dataManager.addToStudentList(studentList, filepath)
dataManager.createFormattedFiles(studentList, "%s-output.csv" % filename, "%s-subjects.csv" % filename)