class Model():
    """
    Model Ising runner
    Execute with run
    """

    dimension = None
    dynamicType = None
    populateType = None
    outputType = None
    output = None
    matrix = None
    size = None

    time = []

    aceitableSize = 1000, 1000000000000
    aceitableDimension = 1, 3

    @staticmethod
    def getAceitableSizeRange():
        return aceitableSize

    @staticmethod
    def getAceitableDimension():
        return aceitableDimension

    def run(self, dimension = 1, size = 1000, dynamic = 'vote', populate = 'random', output = 'ascii'):


        self.dimension = dimension
        self.size = size
        self.dynamicType = dynamic
        self.populateType = populate
        self.outputType = output
        self.initOutput()
        self.output.start()
        self.prepearMatrix()
        self.output.drawMatrix()
        self.runDynamics()
        self.output.end()

    def initOutput(self):

        if self.outputType == 'ascii':
            from output.ascii.ascii import Ascii
            self.output = Ascii(self)
        elif self.outputType == 'image':
            from output.image.image import Image
            self.output = Image(self)
        elif self.outputType == 'video':
            from output.video.video import video
            self.output = Video(self)

    def prepearMatrix(self):
        if self.populateType == 'random':
            from populate.random import Random
            populate = Random()

        populate.run(self)

    def runDynamics(self):
        if self.dynamicType == 'vote' :
            from dynamics.vote.vote import Vote
            dynamic = Vote()

        dynamic.run(self)
