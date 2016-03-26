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
    iterate = 1
    currentIterate = 0

    time = []

    aceitableSize = 1000, 1000000000000
    aceitableDimension = 1, 3

    @staticmethod
    def getAceitableSizeRange():
        return aceitableSize

    @staticmethod
    def getAceitableDimension():
        return aceitableDimension

    def run(self, dimension = 1, size = 1000, dynamic = 'vote', populate = 'random', output = 'ascii' , iterate = 1):


        self.dimension = dimension
        self.size = size
        self.dynamicType = dynamic
        self.populateType = populate
        self.outputType = output
        self.iterate = iterate
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
            from output.video.video import Video
            self.output = Video(self)

    def prepearMatrix(self):
        if self.populateType == 'random':
            from populate.random import Random
            populate = Random()
        elif self.populateType == 'circle':
            from populate.circle import Circle
            populate = Circle()

        populate.run(self)

    def runDynamics(self):
        if self.dynamicType == 'vote' :
            from dynamics.vote.vote import Vote
            dynamic = Vote()
        elif self.dynamicType == 'none':
            from dynamics.none.none import none
            dynamic = none()

        for i in range(self.iterate):
            self.currentIterate += 1
            dynamic.run(self)
