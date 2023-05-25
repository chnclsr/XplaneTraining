import os
import math
from datetime import datetime
import numpy as np



class Attribute():

    def set(self, attrs):
        tuple(map(lambda item: setattr(self, *item), attrs.items()))

    def get_size(self, num):
        return len(list(filter(lambda attr: attr.startswith('v_'), self.__dict__.keys())))

    def encode(self, attr, val):
        min_lim = self.cfg[attr]['min_lim']
        max_lim = self.cfg[attr]['max_lim']
        vector_dim = self.cfg[attr]['vector_dim']
        method = self.cfg[attr]['method']
        binary_suitable = self.cfg[attr]['binary_suitable']
        epsilon = 0.00001

        if(math.isnan(val)):
            warn = "{} value is NaN, so set to minimum value".format(attr)
            print(warn)
            self.logger(warn, "digit_logs")
            val = min_lim
        elif val > max_lim :
            warn = "{} value {} is more than max value {}".format(attr, val, max_lim)
            print(warn)
            val = max_lim - 0.0000001
            self.logger(warn, "digit_logs")
        elif val < min_lim:
            warn = "{} value {} is less than min value {}".format(attr, val, min_lim)
            print(warn)
            # self.logger(warn, "digit_logs")
            val = min_lim

        if method == "onehot" or binary_suitable == False:
            digit = [epsilon] * vector_dim
            port = math.floor((vector_dim * (val-min_lim)) / (max_lim-min_lim))
            if port > vector_dim:
                warn = "{} Position calculation error: position is {}, but vector size {}".format(attr, port, vector_dim)
                print(warn)
                self.logger(warn, "digit_logs")
                port = vector_dim - 1
            elif port < 0:
                warn = "{} Position calculation error: position is {}, but vector size {}".format(attr, port, vector_dim)
                print(warn)
                self.logger(warn, "digit_logs")
                port = 0
            elif port == vector_dim:
                # print("{} Value is on max limit: position is {}, but vector size {}".format(attr, port, vector_dim))
                port = vector_dim - 1
            digit[port] = 1
        elif method == "binary" and binary_suitable == True:
            digit = np.array(list(np.binary_repr(math.floor(2 ** vector_dim * (val - min_lim) / (max_lim - min_lim)) - 1, vector_dim))).astype(np.int8).tolist()
            #digit = np.array(list(np.binary_repr(math.floor(val), vector_dim).zfill(vector_dim))).astype(np.int8).tolist()
            if len(digit) > vector_dim:
                warn = "{} value {} is extremely large/small that it was not enough to express with {} bits. Vector extended to {} bits !".format(attr, val, vector_dim, len(digit))
                print(warn)
                self.logger(warn, "digit_logs")
                how_many_bit_is_overage = len(digit) - vector_dim
                digit = digit[:-how_many_bit_is_overage]  # ignore least significant bits
        else:
            warn = "undefined methodology: ", method
            print(warn)
            self.logger(warn, "digit_logs")
            digit = [0] * vector_dim

        return digit

    def logger(self, text, filename):
        text = str(text)

        log_date = str(datetime.now())
        # log_date = log_date.split(":")
        # log_date = log_date[0]

        content = "warning:" + text + " log time:" + log_date

        # current_path = os.getcwd()
        # parent_path = os.path.dirname(current_path)
        # log_path = os.path.join(parent_path, "logs")
        # if not os.path.isdir(log_path):
        #     os.mkdir(log_path)
        # log_path = os.path.join(parent_path, "logs", filename)
        #
        # with open(log_path, "a") as outfile:
        #     outfile.write(content)
        #     outfile.write("\n")
        #     outfile.close

        # log_file_size_in_bytes = os.path.getsize(log_path)
        # if log_file_size_in_bytes > 536870912*10: # 0.5 GB * 10
        #     os.remove(log_path)
        #     print("file removed")


class Position(Attribute):
    def __init__(self):
        super().__init__()
        self.latitude = None
        self.longitude = None
        self.local_x = None
        self.local_y = None
        self.local_z = None
        self.v_elevation = None
        self.v_theta = None
        self.v_phi = None
        self.v_psi = None
        self.v_local_vx = None
        self.v_local_vy = None
        self.v_local_vz = None
        self.v_P = None
        self.v_Q = None
        self.v_R = None

        # self.v_r_plane1_lat = None # plane_lat - latitude
        # self.v_r_plane1_lon = None # plane_lon - longitude
        # self.v_r_plane1_el = None  # plane_el - elevation
        # self.v_r_plane1_x = None   # plane_x - local_x
        # self.v_r_plane1_y = None   # plane_y - local_y
        # self.v_r_plane1_z = None   # plane_z - local_z
        # self.v_plane1_the = None
        # self.v_plane1_phi = None
        # self.v_plane1_psi = None
        # self.v_plane1_v_x = None
        # self.v_plane1_v_y = None
        # self.v_plane1_v_z = None
        # self.v_plane1_throttle = None
        #
        # self.v_r_plane2_lat = None
        # self.v_r_plane2_lon = None
        # self.v_r_plane2_el = None
        # self.v_r_plane2_x = None
        # self.v_r_plane2_y = None
        # self.v_r_plane2_z = None
        # self.v_plane2_the = None
        # self.v_plane2_phi = None
        # self.v_plane2_psi = None
        # self.v_plane2_v_x = None
        # self.v_plane2_v_y = None
        # self.v_plane2_v_z = None
        # self.v_plane2_throttle = None
        #
        # self.v_r_plane3_lat = None
        # self.v_r_plane3_lon = None
        # self.v_r_plane3_el = None
        # self.v_r_plane3_x = None
        # self.v_r_plane3_y = None
        # self.v_r_plane3_z = None
        # self.v_plane3_the = None
        # self.v_plane3_phi = None
        # self.v_plane3_psi = None
        # self.v_plane3_v_x = None
        # self.v_plane3_v_y = None
        # self.v_plane3_v_z = None
        # self.v_plane3_throttle = None
        #
        # self.v_r_plane4_lat = None
        # self.v_r_plane4_lon = None
        # self.v_r_plane4_el = None
        # self.v_r_plane4_x = None
        # self.v_r_plane4_y = None
        # self.v_r_plane4_z = None
        # self.v_plane4_the = None
        # self.v_plane4_phi = None
        # self.v_plane4_psi = None
        # self.v_plane4_v_x = None
        # self.v_plane4_v_y = None
        # self.v_plane4_v_z = None
        # self.v_plane4_throttle = None
        #
        # self.v_r_plane5_lat = None
        # self.v_r_plane5_lon = None
        # self.v_r_plane5_el = None
        # self.v_r_plane5_x = None
        # self.v_r_plane5_y = None
        # self.v_r_plane5_z = None
        # self.v_plane5_the = None
        # self.v_plane5_phi = None
        # self.v_plane5_psi = None
        # self.v_plane5_v_x = None
        # self.v_plane5_v_y = None
        # self.v_plane5_v_z = None
        # self.v_plane5_throttle = None

        self.cfg = {
            'v_elevation': {'min_lim': 0, 'max_lim': 15000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            'v_theta': {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            'v_phi': {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            'v_psi': {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            'v_local_vx': {'min_lim': -200, 'max_lim': 200, 'vector_dim': 40, 'method': 'onehot', 'binary_suitable': False},
            'v_local_vy': {'min_lim': -300, 'max_lim': 300, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            'v_local_vz': {'min_lim': -600, 'max_lim': 600, 'vector_dim': 120, 'method': 'onehot', 'binary_suitable': False},
            'v_P': {'min_lim': -300, 'max_lim': 300, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            'v_Q': {'min_lim': -100, 'max_lim': 100, 'vector_dim': 20, 'method': 'onehot', 'binary_suitable': False},
            'v_R': {'min_lim': -200, 'max_lim': 200, 'vector_dim': 40, 'method': 'onehot', 'binary_suitable': False},

            # 'v_r_plane1_lat': {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane1_lon': {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane1_el': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane1_x': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane1_y': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane1_z': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane1_the': {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane1_phi': {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane1_psi': {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane1_v_x': {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane1_v_y': {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane1_v_z': {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane1_throttle': {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'method': 'onehot', 'binary_suitable': False},
            #
            # 'v_r_plane2_lat': {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane2_lon': {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane2_el': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane2_x': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane2_y': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane2_z': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane2_the': {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane2_phi': {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane2_psi': {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane2_v_x': {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane2_v_y': {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane2_v_z': {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane2_throttle': {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'method': 'onehot', 'binary_suitable': False},
            #
            # 'v_r_plane3_lat': {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane3_lon': {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane3_el': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane3_x': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane3_y': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane3_z': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane3_the': {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane3_phi': {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane3_psi': {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane3_v_x': {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane3_v_y': {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane3_v_z': {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane3_throttle': {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'method': 'onehot', 'binary_suitable': False},
            #
            # 'v_r_plane4_lat': {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane4_lon': {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane4_el': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane4_x': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane4_y': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane4_z': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane4_the': {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane4_phi': {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane4_psi': {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane4_v_x': {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane4_v_y': {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane4_v_z': {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane4_throttle': {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'method': 'onehot', 'binary_suitable': False},
            #
            # 'v_r_plane5_lat': {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane5_lon': {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane5_el': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane5_x': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane5_y': {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_r_plane5_z': {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane5_the': {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane5_phi': {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane5_psi': {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane5_v_x': {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane5_v_y': {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane5_v_z': {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            # 'v_plane5_throttle': {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'method': 'onehot', 'binary_suitable': False},
        }

    def get_size(self, num):
        return sum(list(map(lambda cfg: cfg['vector_dim'], self.cfg.values())))

    def vectorize(self, num):
        vec = []
        for attr, val in self.__dict__.items():
            if attr.startswith('v_'):        # prefix for vectorize or not
                if attr.startswith('r_', 2): # prefix relative or not
                    pass #params for other aircrafts
                    #vec.extend(self.relative_handler(attr, val[0]))
                else:

                    vec.extend([val[0]])
                    # vec.extend(self.encode(attr, val[0]))
        return vec

    def relative_handler(self, attr, val):
        v_r_plane1_lat = self.latitude
        v_r_plane1_lon = self.longitude
        v_r_plane1_el = self.v_elevation
        v_r_plane1_x = self.local_x
        v_r_plane1_y = self.local_y
        v_r_plane1_z = self.local_z

        v_r_plane2_lat = self.latitude
        v_r_plane2_lon = self.longitude
        v_r_plane2_el = self.v_elevation
        v_r_plane2_x = self.local_x
        v_r_plane2_y = self.local_y
        v_r_plane2_z = self.local_z

        v_r_plane3_lat = self.latitude
        v_r_plane3_lon = self.longitude
        v_r_plane3_el = self.v_elevation
        v_r_plane3_x = self.local_x
        v_r_plane3_y = self.local_y
        v_r_plane3_z = self.local_z

        v_r_plane4_lat = self.latitude
        v_r_plane4_lon = self.longitude
        v_r_plane4_el = self.v_elevation
        v_r_plane4_x = self.local_x
        v_r_plane4_y = self.local_y
        v_r_plane4_z = self.local_z

        v_r_plane5_lat = self.latitude
        v_r_plane5_lon = self.longitude
        v_r_plane5_el = self.v_elevation
        v_r_plane5_x = self.local_x
        v_r_plane5_y = self.local_y
        v_r_plane5_z = self.local_z

        locs = locals()
        ref = locs[attr][0]
        diff = val - ref
        return self.encode(attr, diff)




class Tcas(Attribute):
    def __init__(self):
        super().__init__()
        self.v_relative_bearing_degs = None
        self.v_relative_distance_mtrs = None

        self.cfg = {
            'v_relative_bearing_degs': {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'method': 'onehot', 'binary_suitable': False},
            'v_relative_distance_mtrs': {'min_lim': 0, 'max_lim': 100000, 'vector_dim': 100, 'method': 'onehot', 'binary_suitable': False}
        }

    def get_size(self, num):
        return sum(list(map(lambda cfg: cfg['vector_dim'], self.cfg.values()))) * num

    def vectorize(self, num):
        vec = []
        for attr, val in self.__dict__.items():
            if attr.startswith('v_'): # prefix for vectorize or not
                for v in val[1:num+1]:
                    vec.extend(self.encode(attr, v))
        return vec



class Weapons(Attribute):
    def __init__(self):
        super().__init__()
        pass

    def vectorize(self, num):
        pass



