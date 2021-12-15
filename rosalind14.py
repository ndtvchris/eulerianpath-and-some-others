class stringSticker():

    def __init__(self, infile):
        import copy
        self.realDict = {}

        holdList = []
        prefix = ''
        suffix = ''
        with open(infile) as file:
            file.readline()
            for line in file:
                holdList.append(line.rstrip())
            for kmer in holdList:
                prefix = kmer[0:-1]
                suffix = kmer[1:len(kmer)]
                self.realDict[prefix] = suffix

    def findPath(self):

        tempList = []
        hold = ''
        temp = ''
        start = ''
        copyDict = copy.deepcopy(self.realDict)  # make dictionary for verification

        for key in self.realDict:  # starting at each prefix in the dictionary, looks for a path
            hold = key  # holds the key being used currently
            while True:
                tempList.append(hold)  # puts the prefix into the list
                temp = self.realDict[hold]  # goes into the value at that key, uses that value as the new key
                if temp not in self.realDict:  # if the value doesn't exist as key, it doesn't lead to anything
                    tempList.append(temp)  # puts in the list
                    break  # so, break out of the loop
                else:  # if the key does exist, keep going
                    hold = temp  # sets the hold to keep loop going
            # out here, test if the path even worked

            for x in tempList:
                if x == temp:
                    continue
                copyDict.pop(x)  # destroys each key if it was 'visited' in the list

            if len(copyDict) == 0:  # if every key was destroyed, it worked
                break
            else:
                copyDict = copy.deepcopy(self.realDict)  # remakes dict for another try
                tempList.clear()  # also clears list for another try

        # if here, the path was found correctly. so, put it all together now.
        start = tempList[0]
        with open('p14out.txt', 'w') as out:

            for i in range(1, len(tempList)):
                start += tempList[i][-1]
            # now, should have the full sequence.
            out.write(start)


def main(infile):
    ss = stringSticker(infile)
    ss.findPath()


if __name__ == "__main__":
    main('problem14data.txt')


