from Student import Student
from Subject import Subject

class FileManager:

    subjectList = []

    def addToStudentList(self, studentArr, fileToReadFrom):
        # open files
        file1 = open("%s" % fileToReadFrom, "r")

        # read data from file1 into student list line by line
        for student in file1.readlines():
            # current student's details and overview
            id = student[:10].strip()
            gender = student[11:12].strip()
            name = student[13:64].strip()
            didPass = student[114:118].strip()

            # current student's scores
            thisSubjects = []
            # subject 1
            thisSubjects.append(Subject(student[64:70], student[121:124], student[125:127], self.checkChoose(student[64:70].strip())))
            # subject 2
            thisSubjects.append(Subject(student[70:77], student[128:131], student[132:134], self.checkChoose(student[70:77].strip())))
            # subject 3
            thisSubjects.append(Subject(student[77:84], student[135:138], student[139:141], self.checkChoose(student[77:84].strip())))
            # subject 4
            thisSubjects.append(Subject(student[84:90], student[142:145], student[146:148], self.checkChoose(student[84:90].strip())))
            # subject 5
            thisSubjects.append(Subject(student[90:96], student[149:152], student[153:155], self.checkChoose(student[90:96].strip())))
            # subject 6
            #if self.checkChoose(student[165:173].strip()):
            thisSubjects.append(Subject(student[104:112], student[163:166], student[167:169], self.checkChoose(student[165:173].strip())))
            #else:
            #    thisSubjects.append(Subject("-", "-", "-",self.checkChoose(student[169:173].strip())))


            studentArr.append(Student(id, name, gender, didPass, thisSubjects))
            for s in thisSubjects:
                if s.id + "," + s.name not in self.subjectList and s.name != "":
                    self.subjectList.append(s.id + "," + s.name)

        file1.close()

    def checkChoose(self, info):
        subj_didChoose = (False, True)[info == '']
        return subj_didChoose


    def createFormattedFiles(self, studentArr, fileCsv, fileSub):
        # read data from student list into new files in formatted form

        fileMaster = open("%s" % fileCsv, "w")  # csv file with complete data
        fileSubj = open("%s" % fileSub, "w")  # csv file with subject list

        # write headings
        fileMaster.write("ROLL NO,CANDIDATE NAME,GENDER,SUBJECT 1,MRK,GRD,SUBJECT 2,MRK,GRD,SUBJECT 3,MRK,GRD,SUBJECT 4,MRK,GRD,SUBJECT 5,MRK,GRD,SUBJECT 6,MRK,GRD,RESULT\n")
        fileSubj.write("List of subjects taken by current batch: \n")

        for s in studentArr:
            # read data from student list into files

            if s.id != "":  # don't include empty lines
                fileMaster.write(
                    s.id + "," + s.name + "," + s.gender + ","
                    + s.subject1.name + "," + s.subject1.score + "," + s.subject1.grade + ","
                    + s.subject2.name + "," + s.subject2.score + "," + s.subject2.grade + ","
                    + s.subject3.name + "," + s.subject3.score + "," + s.subject3.grade + ","
                    + s.subject4.name + "," + s.subject4.score + "," + s.subject4.grade + ","
                    + s.subject5.name + "," + s.subject5.score + "," + s.subject5.grade + ","
                    + s.subject6.name + "," + s.subject6.score + "," + s.subject6.grade + ","
                    + s.didPass + "," + "\n")

        for sub in self.subjectList:
            # read data from subject list into subject file
            fileSubj.write(sub + "\n")

        # close file
        fileMaster.close()
        fileSubj.close()

    def editTxt (self, resultInput, resultEdited):

        fileA = open("%s" % resultInput, "r")
        fileB = open("%s" % resultEdited, "w")

        b = True
        prevLine = ""
        for line in fileA.readlines():
            if line.strip() != "":
                if b:
                    fileB.write(line[:126].strip() + "   ")
                    prevLine = line[126:].strip()
                else:
                    fileB.write(line.strip() + "                " + prevLine + "\n")
                b = not b

        fileA.close()
        fileB.close()