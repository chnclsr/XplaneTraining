# import gym_xplane.parameters as params
from gym_xplane.parameters2 import *
from .keywords import *
from .vehicle import Aircraft, Global


class XPlaneObserver():
    "get state params from SIM"
    def __init__(self, client):
        self.client = client

        self.aircraft = Aircraft()
        self.glob = Global()

        self.position_drefs = get_position_drefs()
        self.tcas_drefs = get_tcas_drefs()
        self.global_drefs = get_global_drefs()

        self.prepare_drefs()

        self.attrs = {POSITION:{},TCAS:{},GLOBAL:{}}
        # self.attrs = {POSITION: {}, GLOBAL: {}}
        self.num = 0

        self.pilot_state = []

    def get_size(self):
        return self.aircraft.get_size(self.num)



    def prepare_drefs(self):
        self.drefs = []
        self.dnames = []

        for drefs in (self.position_drefs, self.tcas_drefs, self.global_drefs):
            self.drefs.extend(list(drefs.values()))
            self.dnames.extend(list(drefs.keys()))

    def handle_drefs(self):
        identified = {}
        while True:
            try:
                dataset = self.client.getDREFs(self.drefs)  # self lat
                break
            except Exception as E:
                print(E)

        for i, data in enumerate(dataset):
            identified.update({self.dnames[i]: data})

        for dname, data in identified.items():
            if dname.find(POSITION) != -1:
                # if dname[dname.find('/')+1:] == "v_phi":
                #     print("phi: ", data)
                self.attrs[POSITION].update({dname[dname.find('/')+1:]: data})  # lat lon relative
            elif dname.find(TCAS) != -1:
                self.attrs[TCAS].update({dname[dname.find('/')+1:]: data})
            elif dname.find(GLOBAL) != -1:
                self.attrs[GLOBAL].update({dname[dname.find('/')+1:]: data})

    def observe(self):
        # print("handle")
        self.handle_drefs()
        # print("glob update")
        self.glob.update(self.attrs)
        # print("aircraft fill")
        self.aircraft.fill(self.attrs)
        # print("vectorize")
        state = self.aircraft.vectorize(self.num)
        return state, self.attrs[POSITION] # state + phi angle


