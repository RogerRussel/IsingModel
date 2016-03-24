#!/usr/bin/python3.4

print("initializing Ising Model")

from model import Model
from interface import Interface

#i = Interface()
#dimension = i.askDimension()
#size = i.askSize()

size = 100
dimension = 2
populate = 'circle'
dynamic = 'none'

m = Model()
m.run(dimension, size, populate = populate, iterate = 1000)

print("finished")
