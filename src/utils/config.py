__config = None
class Config(object):
    def __init__(self):
        self.__debug = False

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value

def setConfig(config: Config):
    global __config
    __config = config

def getConfig() -> Config:
    return __config