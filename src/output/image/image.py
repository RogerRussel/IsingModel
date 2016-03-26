from ..output import Output
from PIL import Image as pImage

class Image(Output):
    """
    Image Output
    """

    sufix = 'png'
    mode = '1' # L is for grayscale

    imgSize = None
    defaultColor = 'White'

    def __init__(self, model):
        Output.__init__(self, model)
        self.imgSize = (model.size, model.size)

    def runUniDimension(self):

        img = pImage.new(self.mode, ( self.model.size, 0 ), self.defaultColor)

        index = 0
        for i in self.model.matrix:
            img.putpixel(( index , 0), i)
            index += 1

        img.save(self.normalizeName(self.sufix))

    def runBiDimension(self):

        maxSize = len(self.model.matrix)

        img = pImage.new(self.mode, self.imgSize, self.defaultColor)

        iIndex = 0

        while iIndex < maxSize:

            jIndex = 0

            while jIndex < maxSize:

                img.putpixel((iIndex,jIndex),self.model.matrix[iIndex][jIndex]);

                jIndex += 1

            iIndex += 1


        img.save(self.normalizeName(self.sufix))

    def runTriDimension(self):

        maxSize = len(self.model.matrix)
        index = 0

        while index < maxSize:
            img = pImage.new(self.mode, self.imgSize, self.defaultColor)
            img.putdata(self.model.matrix)
            img.save(self.normalizeName(self.sufix))
