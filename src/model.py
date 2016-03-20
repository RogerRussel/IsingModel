class Model():
    """
    Model Ising runner
    Execute with run
    """

    dimension = None
    dynamicType = None
    populateType = None
    matrix = None
    size = None

    aceitableSize = 1000, 1000000000000
    aceitableDimension = 1, 3

    @staticmethod
    def getAceitableSizeRange():
        return aceitableSize

    @staticmethod
    def getAceitableDimension():
        return aceitableDimension

    def run(self, dimension = 1, size = 1000, dynamic = 'vote', populate = 'random'):
        self.dimension = dimension
        self.size = size
        self.dynamicType = dynamic
        self.populateType = populate
        self.prepearMatrix()
        self.runDynamics()

    def prepearMatrix(self):
        if self.populateType == 'random':
            from populate.random import Random
            populate = Random()

        self.matrix = populate.run(self)

    def runDynamics(self):
        if self.dynamicType == 'vote' :
            from dynamics.vote.vote import Vote
            dynamic = Vote()

        dynamic.run(self)
