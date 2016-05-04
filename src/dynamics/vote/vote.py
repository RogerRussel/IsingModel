from ..dynamic import Dynamic
from random import randint

class Vote(Dynamic):
    """
    Dynamic Method Vote as your service
    It's the most simple method, but thats ok
    """

    def run(self, model):
        Dynamic.run(self, model)

    def process(self, values):
        return values[randint(0,len(values)-1)]
