from random import randint

class Vote():
    """
    Dynamic Method Vote as your service
    It's the most simple method, but thats ok
    """

    model = None

    def run(self, model):
        self.model = model

        if self.model.dimension == 1:
            self.runUniDimension()
        elif self.model.dimension == 2:
            self.runBiDimension()
        elif self.model.dimension == 3:
            self.runTriDimension()

    def checkSize(self, max, size):
        max -= 1
        if max == size:
            s = 0
        else:
            s = size + 1
        return s

    def runUniDimension(self):
        index = 0
        maxSize = len(self.model.matrix)
        maxSizeMinos = maxSize - 1

        maxSize = 100
        x = index

        while index < maxSize:

            self.model.output.running(maxSize, index)

            iRight = self.checkSize(maxSize, index)

            r = [self.model.matrix[index-1], self.model.matrix[iRight]]
            self.model.matrix[index] = r[randint(0,1)] # random between left and right

            index += 1

        self.model.output.runningEnd()

        self.model.output.drawMatrix()

    def runBiDimension(self):

        maxSize = len(self.model.matrix)
        maxPercent = maxSize*2
        iIndex = 0

        while iIndex < maxSize:
            jIndex = 0
            iRight = self.checkSize(maxSize, iIndex)
            iLeft = iIndex - 1

            while jIndex < maxSize:

                self.model.output.running(maxPercent, iIndex+jIndex)

                jRight = self.checkSize(maxSize, jIndex)
                jLeft = jIndex - 1

                r = [
                    self.model.matrix[iLeft][jIndex],
                    self.model.matrix[iRight][jIndex],
                    self.model.matrix[iIndex][jLeft],
                    self.model.matrix[iIndex][jRight]
                ]

                self.model.matrix[iIndex][jIndex] = r[randint(0,3)]

                jIndex += 1
            iIndex += 1

        self.model.output.runningEnd()

        self.model.output.drawMatrix()

    def runTriDimension(self):
        print('Vote tridimension not implemented yet')
        pass
