print("initializing Ising Model")

from model import Model
from interface import Interface

#i = Interface()
#dimension = i.askDimension()
#size = i.askSize()

size = 1000
dimension = 1

m = Model()
m.run(dimension, size)

print("finished")
