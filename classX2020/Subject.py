import csv
class Subject:

    def __init__(self, id, score, grade, didChoose):
        self.id = id.strip()
        self.score = score.strip()
        self.grade = grade.strip()
        self.didChoose = didChoose
        try:
            self.name = self.subjectCodes[self.id]
        except:
            self.name = ' '

    file = "subjectCodeList.csv"
    reader = csv.reader(open("%s" % file))

    subjectCodes = {}
    for row in reader:
        key = row[0]
        if key in subjectCodes:
            # implement your duplicate row handling here
            pass
        subjectCodes[key] = row[1]