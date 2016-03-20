print("initializing Ising Model")

from model import Model

while True:
    dimension = input('How much dimension the model will be?\n number: ')
    try:
       dimension = int(dimension)
    except ValueError:
       print ('Valid dimension, please')
       continue
    if 0 < dimension < 4:
       break
    else:
       print ('Range please: 1-3')

m = Model()
