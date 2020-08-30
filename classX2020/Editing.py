class Editing:

    def edits(self, filename):
        fileA = open("%s.txt" % filename, "r")
        fileB = open("editedResults.txt", "w")

        b = True
        prevLine = ""
        for line in fileA.readlines():
            if line.strip() != "":
                if b:
                    fileB.write(line[:118].strip() + "   ")
                    prevLine = line[118:].strip()
                else:
                    fileB.write(line.strip() + "                " + prevLine + "\n")
                b = not b

        fileA.close()
        fileB.close()
