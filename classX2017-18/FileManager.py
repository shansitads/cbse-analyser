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
            id = student[:8].strip()
            name = student[11:46].strip()
            gender = student[46:47].strip()
            didPass = student[148:].strip()

            # current student's scores
            thisSubjects = []
            thisSubjects.append(self.makeSubject(student[49:60].strip()))
            thisSubjects.append(self.makeSubject(student[60:74].strip()))
            thisSubjects.append(self.makeSubject(student[74:88].strip()))
            thisSubjects.append(self.makeSubject(student[88:101].strip()))
            thisSubjects.append(self.makeSubject(student[101:114].strip()))
            # thisSubjects.append(self.makeSubject(student[114:131].strip()))
            thisSubjects.append(self.makeSubject(student[131:142].strip()))

            studentArr.append(Student(id, name, gender, didPass, thisSubjects))
            for s in thisSubjects:
                if s.name not in self.subjectList and s.name != "":
                    self.subjectList.append(s.name)

        file1.close()

    def makeSubject(self, info):
        subj_id = info[:3].strip()
        subj_score = info[4:7].strip()
        subj_grade = info[-2:].strip()
        subj_didChoose = (False, True)[info == '']
        # info parameter is in the form of a string (central section of original data file containing scores)
        return Subject(subj_id, subj_score, subj_grade, subj_didChoose)

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
