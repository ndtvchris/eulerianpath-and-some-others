class overlapper():

    def __init__(self, infile):
        self.list = self.readSequences(infile)

    def readSequences(self, infile):
        aList = []
        with open(infile) as file:
            for line in file:
                aList.append(line.rstrip())

        return aList

    def checkOverlap(self):
        results = []
        for x in self.list:
            string1 = x[0:len(x) - 1]
            for y in self.list:
                string2 = y[1:len(y)]
                if string1 == string2:
                    string3 = x + ' -> ' + y
                    results.append(string3)
                else:
                    continue
        with open('p10out.txt', 'w') as out:
            for i in results:
                out.write(i + '\n')


def main(infile):
    oL = overlapper(infile)
    oL.checkOverlap()


if __name__ == "__main__":
    main('problem10data.txt')