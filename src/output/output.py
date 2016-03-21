from time import process_time

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

    def normalizeName(self, sufix):
        name = 'output/'
        name += self.module.dynamicType
        name += '.d-' + self.module.dimension
        name += '.s-' + self.module.size
        name += '.t-' + str(process_time())
        name += sufix

        return name
