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
        model.matrix = [ random.randint(0,1) for i in range(self.size) ]

    def makeBiDimension(self, model):
        model.matrix = [
            [ random.randint(0,1) for i in range(self.size) ]
                for in range(self.size)
        ]

    def makeTriDimension(self, model):
        model.matrix = [                    [
            [ random.randint(0,1) for x in range(self.size) ]
                for y in range(self.size)
            ] for z in range(self.size)
        ]
