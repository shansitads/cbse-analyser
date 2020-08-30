from FileManager import FileManager
from Editing import Editing
import os

# student list contains student data type elements
studentList = []
dataManager = FileManager()
editBot = Editing()

filepath = input("Enter the path of your file: ").strip()
assert os.path.exists(filepath), "Did not find the file at, "+str(filepath)
print("Your file was found!")

filename = os.path.splitext(os.path.basename(filepath))[0]

editBot.edits(filename)

dataManager.addToStudentList(studentList, "editedResults.txt")
dataManager.createFormattedFiles(studentList, "%s-output.csv" % filename, "%s-subjects.csv" % filename)


