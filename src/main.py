#!/usr/bin/python3.4

print("initializing Ising Model")

from model import Model
from interface import Interface

#i = Interface()
#dimension = i.askDimension()
#size = i.askSize()

size = 100
dimension = 2

m = Model()
m.run(dimension, size)

print("finished")
