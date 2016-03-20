from populate.random import Random
from dynamics.vote.vote import Vote

class Model():
    """
    Model Ising runner
    Execute with run
    """

    dimension = None
    dynamic = None
    dynamicType = None
    matrix = None

    aceitableSize = 1000, 1000000000000
    aceitableDimension = 1, 3

    @staticmethod
    def getAceitableSizeRange():
        return aceitableSize

    @staticmethod
    def getAceitableDimension():
        return aceitableDimension

    def run(self, dimension = 1, dynamic = 'vote'):
        self.dimension = 1
        self.dynamicType = dynamic
        self.prepearMatrix()
        self.runDynamics()

    def runDynamics(self):
        self.dynamic = Vote()
        self.dynamic.run(self)

    def prepearMatrix(self):
        if self.dimension == 1:
            pass
        elif self.dimension == 2:
            pass
        elif self.dimensin == 3:
            pass
