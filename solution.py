import search


class RTBProblem(search.Problem):
    def __init__(self):
        self.initial = None

    def load(self, fh):
        # Open and read file lines
        fh = open('ex1.dat', 'r')
        #lines = fh.readlines()

        # line_id = 0

        # while (lines[line_id][0] == '#'):
        #     line_id += 1
        # N = lines[line_id][0]
        # line_id += 1

        # self.initial =
        pass

    def isSolution(self):
        # return 1 or 0 depending if it is a solution
        pass
