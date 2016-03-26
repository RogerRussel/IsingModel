#!/usr/bin/python3.5

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
output = 'video'
iterate = 10

m = Model()
m.run(dimension, size, populate = populate, iterate = iterate, output = output)

print("finished")
