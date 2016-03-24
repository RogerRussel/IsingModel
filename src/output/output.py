from time import process_time
from sys import stdout

class Output():
    """
    Output Class, normalize output commands
    """
    time = [0,0]

    model = None

    def __init__(self, model):
        self.model = model

    def start(self):
        self.time[0] = process_time()
        print('\n\tstarted at: ',self.time[0],'\n')

    def end(self):
        self.time[1] = process_time()
        print('\n\tfinished at: ',self.time[1],'\n')

    def running(self, maxSize, current ):
        percent = int((100 * current)/maxSize)
        stdout.write("\r\tRunning iterate " + str(self.model.currentIterate) + ": " + str(percent) + "%")
        stdout.flush()

    def runningEnd(self):
        stdout.write("\r\tRunning iterate " + str(self.model.currentIterate) + ": 100%\n")
        stdout.flush()

    def normalizeName(self, sufix):
        name = 'output/'
        name += self.model.dynamicType
        name += '.d-' + str(self.model.dimension)
        name += '.s-' + str(self.model.size)
        name += '.t-' + str(self.model.currentIterate)
        name += '.' + sufix

        return name
