from math import pi
from math import sqrt

class Circle():
    """
    Create the matrix populate with an circle distribuitation
    """

    def run(self, model):
        if model.dimension == 1:
            self.makeUniDimension(model)
        elif model.dimension == 2:
            self.makeBiDimension(model)
        elif model.dimension == 3:
            self.makeTriDimension(model)

    def makeUniDimension(self, model):
        pass

    def makeBiDimension(self, model):

        model.matrix = [
            [ 0 for i in range(model.size) ]
                for j in range(model.size)
        ]

        squadArea = model.size ** 2

        radPower2 =  (squadArea/2)/pi
        circleCenter = model.size/2

        iIndex = 0
        while iIndex < model.size:
            jIndex = 0
            while jIndex < model.size:
                px = ((jIndex+1) - circleCenter ) ** 2
                py = ((iIndex+1) - circleCenter ) ** 2
                if ( px + py ) <= radPower2 :
                    model.matrix[iIndex][jIndex] = 1
                jIndex += 1
            iIndex += 1

    def makeTriDimension(self, model):
        pass
