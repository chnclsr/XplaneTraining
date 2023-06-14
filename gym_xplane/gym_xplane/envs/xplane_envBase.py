import gym
from .. import xpc
import gym_xplane.gym_xplane.parameters as parameters
import gym_xplane.gym_xplane.space_definition as envSpaces
import numpy as np
import time
from gym import spaces
from .observation import XPlaneObserver
from .reward import XPlaneRewarder
from. application import XPlaneApplier



class XplaneEnv(gym.Env):
    "Pekiştirmeli öğrenme GYM objesi. Sunucu-İstemci tarafında XplaneConnect plugins kullanılmıştır."
    def __init__(self, clientAddr, xpHost, xpPort, clientPort, timeout=3000, max_episode_steps=303, test=False):
        self.clientAddr = clientAddr
        self.xpHost = xpHost
        self.xpPort = xpPort
        self.timeout = timeout
        self.clientPort = clientPort
        self.max_episode_steps = max_episode_steps
        #client = client
        self.client = None
        #print(parameters)
        envSpace = envSpaces.xplane_space()
        self.action_space = envSpace._action_space()
        self.observation_space = envSpace._observation_space()
        #self.episode_steps = 0
        self.max_episode_steps = max_episode_steps
        self.statelength = 7
        self.actions = [0,0,0,0]
        self.test=test
        self.resetTimeStep = 0
        self.total_time_step = 0
        self.gen_drefs = parameters.get_general_datarefs()
        self.comms = parameters.get_commands()
        self.client = xpc.XPlaneConnect(port=self.clientPort)
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            self.client.getDREF("sim/test/test_float")
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return

        self.observer = XPlaneObserver(self.client)
        self.applier = XPlaneApplier(self.client, self.observer)
        self.rewarder = XPlaneRewarder(self.client, self.observer, self.applier)
        self.observer.client = self.client
        self.rewarder.client = self.client
        self.applier.client = self.client

        self.state_space = spaces.Box(np.ones(self.observer.get_size()), -np.ones(self.observer.get_size())) # 85, 6190, now 6490
        self.concatenated_action_num = 1
        self.speed_worker_action_space = spaces.Discrete(self.applier.get_size()[0])    # aileron worker: 21
        self.heading_worker_action_space = spaces.Discrete(self.applier.get_size()[1])  # elevator worker: 21
        self.altitude_worker_action_space = spaces.Discrete(self.applier.get_size()[2]) # rudder worker: 21
        self.sensor_worker_action_space = spaces.Discrete(self.applier.get_size()[3])   # throttle worker: 11

        self.episode = 0
        self.time_step_limit = 250

        self.rollAngleList = np.linspace(-90, 90, 13)

        self.preState = None
        self.pre_phi = None

        self.v_phi = None
        self.vhi_limit = 10


    def _get_info(self):
        """Returns a dictionary contains debug info"""
        return {'data reference names':self.gen_drefs, 'actions':self.action_space }

    def close(self):
        self.client.close()

    def step(self, action):
        self.time_step += 1
        self.total_time_step += 1
        state, reward, done, _ = self.ministep(action)
        return state, reward, done, _

    def apply_action(self, action):
        self.applier.apply(action)

    def ministep(self, action):
        # print("actionnnnnnnn")
        # send selected action
        self.apply_action(action) # {'ai_actions':[], 'pilot_action':[]}
        time.sleep(0.1)
        # get next state
        # print("action geçildiiiiiiiiiii")

        next_state, positionData = self.get_state()
        self.v_phi = positionData["v_phi"][0]
        done = self.check_termination()
        # get reward
        reward = self.get_reward(done)

        self.preState = next_state
        # get info
        _ = self._get_info()

        return next_state, reward, done, _

    def check_termination(self):
        done = False
        pos_attrs = self.observer.attrs['position']
        glob_attrs = self.observer.attrs['global']
        has_crashed = glob_attrs['has_crashed'][0]
        onground_any = glob_attrs['onground_any'][0]

        # has_crashed = self.client.getDREF(self.gen_drefs["has_crashed"])[0][0]
        # onground_any = self.client.getDREF(self.gen_drefs["onground_any"])[0][0]
        # print("on ground:", onground_any)
        # elevation = self.client.getDREF(self.gen_drefs["elevation"])[0][0]
        elevation = pos_attrs['v_elevation'][0]
        # print("elevation:",elevation)
        if (has_crashed == True) or (onground_any == True) or (elevation < 100) or (self.time_step >= self.time_step_limit):
            done = True
            print("has_crashed: {} --- timestep: {}".format(has_crashed, self.time_step))
        return done

    def get_reward(self, done):
        self.rewarder.done = done
        "calculate vhi angle changing WR2pre state and currrent state"
        abs_vhi = np.abs(self.v_phi)  # açı sıfırla tolerans aralığındaysa sıfıra yaklaştıkça ödül artar, Toleranstan büyük oldukça daha büyük ceza alır
        reward = -1 * ((abs_vhi - self.vhi_limit)/(180 - self.vhi_limit)) - 0.001
        reward = self.rewarder.reward() #TODO: info store
        return reward

    def get_state(self):
        self._start_time = time.time()
        state = self.observer.observe()
        return state

    def render(self, mode='human', close=False):
        pass

    def reset(self, state_c=True):
        self.client.pauseSim(False)
        self.client.sendCOMM("sim/operation/reset_flight")  # reset flight to most recent start
        # print("99")

        self.client.sendVIEW(xpc.ViewType.Chase)  # external view
        gear = 0  # 0:down, 1:up
        values = [47.18, -122.307753, 10000, 0, self.rollAngleList[np.random.randint(13)], 180, 0]  # Seattle Tacoma Airport coordinates, self.rollAngleList[np.random.randint(13)]
        # print("102")

        self.client.sendPOSI(values, 0)  # respawn at starting point
        time.sleep(.25)

        # values1 = [47.163639, -122.307753, 1200, 0, 0, 0, 0]  # Seattle Tacoma Airport coordinates
        # self.client.sendPOSI(values1, 1)  # respawn at starting point
        # time.sleep(.25)

        # values2 = [47.163639, -122.307753, 1400, 0, 0, 0, 0]  # Seattle Tacoma Airport coordinates
        # self.client.sendPOSI(values2, 2)  # respawn at starting point
        # time.sleep(.25)
        # print("110")

        # time.sleep(4)
        if state_c:
            accessed = False
            while not accessed:
                # print("posssssssss")
                posi = self.client.getPOSI()
                print(posi)
                if (posi[2] < values[2] + 100) and (posi[2] > values[2] - 100):
                    accessed = True
                    print("reset succeded")
                    # print("posi:", posi)
                else:
                    self.client.sendPOSI(values, 0)
                    # self.client.sendPOSI(values1, 1)
                    # self.client.sendPOSI(values2, 2)
                    self.client.sendVIEW(xpc.ViewType.Chase)
                    print("reset failed")

            # onground_any = self.client.getDREF(self.gen_drefs["onground_any"])[0][0]
            # accessed = False
            # while not accessed:
            #     if onground_any == True:
            #         print("reset failed")
            #         self.client.sendPOSI(values, 0)
            #     else:
            #         accessed = True
            #         print("reset succeded")

            self.client.sendDREF(self.gen_drefs["local_vz"], np.array([250], dtype="float32")[0])  # give initial speed
            print("hız gönderildi")
            self.time_step = 0
            self.episode += 1
            print("state alındı")

            state, self.pre_phi = self.get_state()  # get initial state
            self.preState = state
            return state
        else:
            self.client.sendDREF(self.gen_drefs["local_vz"], np.array([250], dtype="float32")[0])  # give initial speed
            print("hız gönderildi")
            return 0
