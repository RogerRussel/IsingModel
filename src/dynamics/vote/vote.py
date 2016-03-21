from random import randint

class Vote():
    """
    Dynamic Method Vote as your service
    It's the most simple method, but thats ok
    """

    model = None

    def run(self, model):
        self.model = model

        self.model.output.start()

        if self.model.dimension == 1:
            self.runUniDimension()
        elif self.model.dimension == 2:
            self.runBiDimension()
        elif self.model.dimension == 3:
            self.runTriDimension()

        self.model.output.end()

    def runUniDimension(self):
        index = 0

        for i in self.model.matrix:
            r = [self.model.matrix[i-1], self.model.matrix[i+1]]
            self.model.matrix[i] = r[randint(0,1)] # random between left and right
            index += 1

        self.model.output.drawMatrix()


    def runBiDimension(self):
        print('Vote bidimension not implemented yet')
        pass

    def runTriDimension(self):
        print('Vote tridimension not implemented yet')
        pass
