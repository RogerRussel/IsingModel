from time import process_time
from sys import stdout

class Output():
    """
    Output Class, normalize output commands
    """
    time = [0,0]

    module = None

    def __init__(self, module):
        self.module = module

    def start(self):
        self.time[0] = process_time()
        print('\n\tstarted at: ',self.time[0],'\n')

    def end(self):
        self.time[1] = process_time()
        print('\n\tfinished at: ',self.time[1],'\n')

    def running(self, maxSize, current ):
        percent = int((100 * current)/maxSize)
        stdout.write("\r\tRunning: " + str(percent) + "%")
        stdout.flush()        

    def runningEnd(self):
        stdout.write("\r\tRunning: 100%\n")
        stdout.flush()

    def normalizeName(self, sufix):
        name = 'output/'
        name += self.module.dynamicType
        name += '.d-' + str(self.module.dimension)
        name += '.s-' + str(self.module.size)
        name += '.t-' + str(process_time())
        name += sufix

        return name
