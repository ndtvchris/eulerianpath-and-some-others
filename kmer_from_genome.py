class finder():

    def __init__(self, infile):

        with open(infile) as file:
            self.k = int(file.readline())
            self.data = file.read()

    def motifFinder(self):
        aList = []
        for x in range(0, len(self.data) - self.k):  # remember, it cuts off the end since it's base 0.
            kmer = self.data[x: x + self.k]
            aList.append(kmer)
        with open('p8out.txt', 'w') as out:
            for x in aList:
                out.write(x + '\n')


def main(infile):
    find = finder(infile)
    find.motifFinder()


if __name__ == "__main__":
    main('problem8data.txt')