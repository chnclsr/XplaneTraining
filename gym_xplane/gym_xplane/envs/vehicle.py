import itertools
from .keywords import *
from .attribute import Position, Tcas



class Aircraft():
    def __init__(self):
        self.position = Position()
        self.tcas = Tcas()

    def get_size(self, num): # alternate: self.position.get_size(num)
        return sum(list(map(lambda obj: obj.get_size(num), self.__dict__.values())))

    def fill(self, attrs):
        for attr, obj in self.__dict__.items():
            obj.set(attrs[attr])               # alternate: self.position.set(attrs[attr])

    def vectorize(self, num):
        pos_vec = self.position.vectorize(num)
        tcas_vec = self.tcas.vectorize(num)
        vecs = [pos_vec, tcas_vec]
        # vecs = [pos_vec]
        vec = list(itertools.chain(*vecs))
        return vec





class Global():
    def __init__(self):
        self.onground_any = None
        self.tcas_num_acf = None
        self.has_crashed = None
        self.ENGN_running = None

    def update(_self, attrs):
        tuple(map(lambda item: setattr(_self, *item), attrs[GLOBAL].items()))
