from model import Model

class Interface():

    def askDimension():

        dimensionRange = Model.getAceitableDimension()

        while True:
            dimension = input('How much dimension the model will be?\n number: ')
            try:
               dimension = int(dimension)
            except ValueError:
               print ('Valid dimension, please')
               continue
            if dimensionRange[0] <= dimension <= dimensionRange[1]:
               break
            else:
               print ('Range please: ', dimensionRange[0], dimensionRange[1])

        return dimension

    def askSize():

        sizeRange = Model.getAceitableSizeRange()

        while True:
            size = input('How much size the model will be?\n number: ')
            try:
               size = int(size)
            except ValueError:
               print ('Valid size number, please')
               continue
            if sizeRange[0] <= dimension <= sizeRange[1]:
               break
            else:
               print ('Range please:', sizeRange[0], '-', sizeRange[1])

        return sizeRange
