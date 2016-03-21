from ..output import Output

class Ascii(Output):
    """
    Ascii Art Output
    """

    f = None
    sufix = 'ascii'

    def drawMatrix(self):

        self.f = open(self.normalizeName(self.sufix),'w')

        if self.module.dimension == 1:
            self.runUniDimension()
        elif self.module.dimension == 2:
            self.runBiDimension()
        elif self.module.dimension == 3:
            self.runTriDimension()

        self.f.close()

    def runUniDimension(self):
        for i in self.module.matrix:
            char = "@" if i == 1 else " "
            self.f.write(char)

    def runBiDimension(self):
        for i in self.module.matrix:
            for j in i:
                char = "@" if j == 1 else " "
                self.f.write(char)
            self.f.write('\n')

    def runTriDimension(self):
        for i in self.module.matrix:

            f = open(self.normalizeName(str(i+1) + "to3." + self.sufix))

            for j in i:
                for z in j:
                    char = "@" if z == 1 else " "
                    f.write(char)
                f.write('\n')

            f.close()
