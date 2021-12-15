class deBrujinKmer:

    def __init__(self, infile):
        self.data = self.readFile(infile)
        self.graph = []
        self.prefixes = []

    def readFile(self, infile):

        with open(infile) as f:
            data = []
            for line in f:
                data.append(line.replace("\n", ""))

        return data

    # create composition graph where every kmer is paired with its prefix and suffix
    def makeGraph(self):

        k = len(self.data[0])

        self.prefixes = [i[0:k - 1] for i in self.data]
        suffixes = [i[1:k] for i in self.data]
        self.graph = list(zip(self.data, self.prefixes, suffixes))

    # create deBruijn graph, gluing suffix nodes to identical prefix node
    def deBruijnGraph(self):

        prefix = list(set(self.prefixes))
        prefix.sort()

        dbg = {}

        for x in prefix:
            dbg[x] = []

        for i in range(len(self.graph)):
            dbg[self.graph[i][1]].append(self.graph[i][2])

        return dbg


def main(infile):
    dbk = deBrujinKmer(infile)
    dbk.makeGraph()
    dbg = dbk.deBruijnGraph()

    with open('p12out.txt', 'w') as out:

        for key in dbg:

            dbg[key].sort()
            hold = ""
            for value in dbg[key]:
                hold = hold + value + ","

            hold = hold[0:len(hold) - 1]
            out.write(key + " -> " + hold + "\n")


if __name__ == '__main__':
    main('rosalind_ba3e.txt')
