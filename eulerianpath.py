import collections as col

class eulerpath:

    def __init__(self, infile):
        self.nodeDict = {}
        self.realpath = []
        self.compdict = {}
        pathlist = []
        with open(infile) as file:
            for line in file:
                [pathlist.append(i.rstrip()) for i in line.split(' -> ')[1].split(',')]
                self.nodeDict[line.split(' -> ')[0]] = pathlist
                self.compdict[line.split(' -> ')[0]] = pathlist
                pathlist = []


        self.inDict = {k: 0 for k in self.nodeDict}
        self.outDict = {k: 0 for k in self.nodeDict}

    def findStart(self):

        for key in self.nodeDict:
            try:
                for branch in self.nodeDict[key]:
                    self.outDict[key] +=1
                    self.inDict[branch] +=1
            except KeyError:
                continue

        for key in self.inDict:
            if self.outDict[key] > self.inDict[key]:
                return key

    def recur(self, start):
        stack = col.deque()
        pointer = start
        # starting at the start node, traverse
        # this will continue until all edges are "removed" from outDict
        stack.append(pointer)
        while sum(self.outDict.values()) > 0:
            # should check if paths even exist from the current node
            try:
                if self.outDict[pointer] == 0:
                    self.realpath.insert(0, pointer)
                    stack.pop()
                    pointer = stack[len(stack) - 1]

                    continue
            except KeyError: # this is for the end node
                self.realpath.insert(0, stack.pop())
                pointer = stack[len(stack) - 1]

                continue
            try:
                # this loop gets the next pointer
                for branch in self.nodeDict[pointer]:
                    if branch not in self.compdict[pointer]:
                        continue
                    else:
                        newpointer = branch
                        break
            except KeyError: # this will get thrown once we reach the end
                newpointer = stack.pop()
            # as we move to the next node, must account for the change
            # remove the path from compdict
            self.compdict[pointer].remove(newpointer)
            # subtract value from outDict
            self.outDict[pointer] -= 1
            # add to stack
            stack.append(newpointer)
            # update pointer
            pointer = newpointer

        # if here, pop everything off the stack in the order it's in since I assume it should be at the final pass

        while len(stack) > 0:
            self.realpath.insert(0, stack.pop())

    def writeout(self):
        with open('eulerout.txt', 'w') as out:
            out.write('->'.join(self.realpath))


