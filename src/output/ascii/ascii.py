from ..output import Output

class Ascii(Output):
    """
    Ascii Art Output
    """

    sufix = 'ascii'

    def runUniDimension(self):

        f = open(self.normalizeName(self.sufix))

        for i in self.model.matrix:
            char = "@" if i == 1 else " "
            f.write(char)

        f.close()

    def runBiDimension(self):

        f = open(self.normalizeName(self.sufix))

        for i in self.model.matrix:
            for j in i:
                char = "@" if j == 1 else " "
                f.write(char)
            f.write('\n')

        f.close()

    def runTriDimension(self):

        for i in self.model.matrix:

            f = open(self.normalizeName(str(i+1) + "to3." + self.sufix))

            for j in i:
                for z in j:
                    char = "@" if z == 1 else " "
                    f.write(char)
                f.write('\n')

            f.close()
