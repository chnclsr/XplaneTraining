from .kheys import *
import numpy as np



class XPlaneApplier():
    def __init__(self, client, observer):
        self.client = client
        self.observer = observer
        self.action_size = (21,21,21,11) # aileron(speed), elevator(heading), rudder(altitude), throttle(sensor)
        self.initialize_semantics()
        self.action_ = None  # merged form (cont+disc)
        self.pilot_action = None
        self.munition_count = 0
        self.fired_action_count = 0

    def get_size(self):
        return self.action_size

    def initialize_semantics(self): # action pre-definition
        self.initialize_control_semantics()

    def initialize_control_semantics(self):
        ap = list(np.linspace(-1,1,self.action_size[0])) # aileron points
        ep = list(np.linspace(-1,1,self.action_size[1])) # elevator points
        rp = list(np.linspace(-1,1,self.action_size[2])) # rudder points
        tp = list(np.linspace(0,1,self.action_size[3]))  # throttle points

        self.aileron_smntcs = {0:ap[0], 1:ap[1], 2:ap[2], 3:ap[3], 4:ap[4], 5:ap[5], 6:ap[6], 7:ap[7], 8:ap[8], 9:ap[9],
                                10:ap[10], 11:ap[11], 12:ap[12], 13:ap[13], 14:ap[14], 15:ap[15], 16:ap[16], 17:ap[17], 18:ap[18], 19:ap[19], 20:ap[20]}

        self.elevator_smntcs = {0:ep[0], 1:ep[1], 2:ep[2], 3:ep[3], 4:ep[4], 5:ep[5], 6:ep[6], 7:ep[7], 8:ep[8], 9:ep[9],
                                  10:ep[10], 11:ep[11], 12:ep[12], 13:ep[13], 14:ep[14], 15:ep[15], 16:ep[16], 17:ep[17], 18:ep[18], 19:ep[19], 20:ep[20]}

        self.rudder_smntcs = {0:rp[0], 1:rp[1], 2:rp[2], 3:rp[3], 4:rp[4], 5:rp[5], 6:rp[6], 7:rp[7], 8:rp[8], 9:rp[9],
                                  10:rp[10], 11:rp[11], 12:rp[12], 13:rp[13], 14:rp[14], 15:rp[15], 16:rp[16], 17:rp[17], 18:rp[18], 19:rp[19], 20:rp[20]}

        self.throttle_smntcs = {0:tp[0], 1:tp[1], 2:tp[2], 3:tp[3], 4:tp[4], 5:tp[5], 6:tp[6], 7:tp[7], 8:tp[8], 9:tp[9], 10:tp[10]}

    def interpret(self, semantics, action):  # convert neural network output to predefined semantics without any intermediate process
        point = semantics.get(action)
        return point

    def apply_control(self):
        heading = self.interpret(self.aileron_smntcs, self.aileron_action) # kanat üstü üniteler
        rudder = 0.3 #self.interpret(self.elevator_smntcs, self.elevator_action) #arka kuyrukdaki rudderlar
        verticalStabilizer_point = 0.0 #self.interpret(self.rudder_smntcs, self.rudder_action) # TB2' ve AKINCI'da dikey stabilleştirici olmadığından 0
        speed = np.random.choice([0, 1], p=[0.4, 0.6])  #self.interpret(self.throttle_smntcs, self.throttle_action) #hız
        control = [rudder, heading, verticalStabilizer_point, speed, 0, 0] # elevator, aileron, rudder, throttle, gear, flaps
        self.client.sendCTRL(control)

    def apply_tactic(self):
        self.fired_action_count += 1
        if self.fired_action and self.fired_action_count < self.munition_count:
            self.client.sendDREF("sim/joystick/fire_key_is_down", 0)
            self.client.sendDREF("sim/cockpit/weapons/plane_target_index", 1)
            self.client.sendDREF("sim/cockpit2/weapons/weapon_select_console_index", self.fired_action_count)
            self.client.sendDREF("sim/joystick/fire_key_is_down", 1)



    def update(self, action):
        self.action_ = action #action.cont + action.disc # [speed heading altitude sensor] weapon message -> [aileron elevator rudder throttle]
        self.aileron_action = self.action_ # heading
        # self.aileron_action = self.action_[0]
        # self.elevator_action = self.action_[1]
        # self.rudder_action = self.action_[2]
        # self.throttle_action = self.action_[3] # speed
        self.fired_action = 0

    def apply(self, action):
        self.update(action)
        self.apply_control()
        self.apply_tactic()



# -1.(0), -0.9(1), -0.8(2), -0.7(3), -0.6(4), -0.5(5), -0.4(6), -0.3(7), -0.2(8), -0.1(9), 0.(10), 0.1(11), 0.2(12), 0.3(13), 0.4(14), 0.5(15), 0.6(16), 0.7(17), 0.8(18), 0.9(19), 1.(20)

# 0.(0), 0.1(1), 0.2(2), 0.3(3), 0.4(4), 0.5(5), 0.6(6), 0.7(7), 0.8(8), 0.9(9), 1.(10)


















