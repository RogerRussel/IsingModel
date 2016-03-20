import random

class Random():
    """
    Create the matrix populate with random distribuitation
    """

    def run(self, model):
        if model.dimension == 1:
            self.makeUniDimension(model)
        elif model.dimension == 2:
            self.makeBiDimension(model)
        elif model.dimension == 3:
            self.makeTriDimension(model)

    def makeUniDimension(self, model):
        model.matrix = [ random.randint(0,1) for i in range(model.size) ]

    def makeBiDimension(self, model):
        model.matrix = [
            [ random.randint(0,1) for i in range(model.size) ]
                for j in range(model.size)
        ]

    def makeTriDimension(self, model):
        model.matrix = [                    [
            [ random.randint(0,1) for x in range(model.size) ]
                for y in range(model.size)
            ] for z in range(model.size)
        ]
