class stringCombiner():

    def __init__(self, infile):
        self.list = self.readSequences(infile)

    def readSequences(self, infile):
        aList = []
        with open(infile) as file:
            for line in file:
                aList.append(line.rstrip())

        return aList

    def motifCombine(self):
        string1 = self.list[0]
        for x in range(1, len(self.list)):
            char = self.list[x][-1]

            string1 += char
        with open('p9out.txt', 'w') as out:
            out.write(string1)


def main(infile):
    sc = stringCombiner(infile)
    sc.motifCombine()


if __name__ == "__main__":
    main('problem9data.txt')