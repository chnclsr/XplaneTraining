import numpy as np
from scipy.spatial.distance import pdist, squareform



class XPlaneRewarder():
    def __init__(self, client, observer, applier):
        self.client = client
        self.observer = observer
        self.applier = applier
        self.done = None

    def gaussian_calculus(self, target_state, xplane_state, sigma=0.45):
        '''
        input : target state (a list containing the target heading, altitude and runtime)
                xplane_state(a list containing the aircraft heading , altitude at present timestep, and the running time)
                Note: if the aircraft crashes then the run time is small, thus the running time captures crashes
        output: Gaussian kernel similarîty between the two inputs. A value between 0 and 1

        '''

        data = np.array([target_state, xplane_state])
        pairwise_dists = pdist(data, 'cosine')
        #print('pairwise distance',pairwise_dists)
        similarity = np.exp(-pairwise_dists ** 2 / sigma ** 2)
        return pairwise_dists

    # distance rel enemyhit  f g h     y([d r ene]) = y
    def distance_reward(self, distance):
        reward = 0
        try:
            reward = 1 - (distance / 50000)
        except:
            print("check your distance")
        return reward

    def linear(self, x, c): # x: variable, c: max constant
        y = (1 - (x/c))
        return y

    def step_reward(self): # step reward
        #TODO: step reward: P Q R yüksekse ceza -0.001
        #TODO: PQR ye gerek olmayabilir
        reward = 0
        self_info = self.info_store[0]
        target_info = self.info_store[1] # 1:F-4 Phantom 2:Baron

        if abs(self_info['P']) > 45: # -300 +300
            reward -= 0.001
        if abs(self_info['Q']) > 45: # -100 +100
            reward -= 0.001
        if abs(self_info['R']) > 45: # -200 -200
            reward -= 0.001

        #if abs(self_info['phi']) > 30:
        reward += self.linear(abs(self_info['phi']), 90)/10
        reward += self.linear(abs(self_info['theta']), 90)/10
        reward -= self.linear(abs(self_info['psi']-180), 180)/10

        # target_info = self.info_store[1]  # 1:F-4 Phantom 2:Baron
        r_bearing = self.linear(abs(target_info['rel_bearing']), 90) / 10
        reward += r_bearing

        # opinion = 0 #self.instructor() # ask to instructor in every step
        # reward += opinion
        return reward

    """
    def episode_reward(self): # end of episode
        #TODO: episode bitiminde düşmana ne kadar yaklaşabildin ödülünü büyüterek(x10) ver.
        #TODO: episode sonu reward - relative bearing ve (relative)elevation için distance'taki yaklaşım kullanılacak

        # 1:F-4 Phantom 2:Baron
        pos_attrs = self.observer.attrs['position']
        tcas_attrs = self.observer.attrs['tcas']
        glob_attrs = self.observer.attrs['global']
        distance = self.linear(tcas_attrs['v_relative_distance_mtrs'][1], 50000)
        # r_bearing = self.linear(abs(target_info['rel_bearing']), 180)
        # r_elevation = self.linear(abs(pos_attrs['v_elevation'][0]), abs(pos_attrs['v_r_plane1_el'][0] - pos_attrs['v_elevation'][0]))

        # [onground_any, has_crashed] = self.client.getDREFs([self.gen_drefs['onground_any'], self.gen_drefs["has_crashed"]])
        onground_any = glob_attrs['onground_any'][0]
        has_crashed = glob_attrs['has_crashed'][0]
        # crash = self.client.getDREFs([self.gen_drefs.crash])[0][0]
        crash_rew = 0
        if has_crashed == 1:
            #TODO: -3 fena degil
            reward = -3
            print("EPISODE REWARD--- crash:{}".format(reward))
        else:
            # reward = 2 * distance + r_elevation
            pass
            # print("EPISODE REWARD--- distance:{}    r_elevation:{}  reward:{}".format(distance, r_elevation, reward))

        # reward = distance + r_elevation + crash_rew
        reward = distance + crash_rew
        return reward
    """

    """
    def instructor(self):
        ai_action = self.applier.action_         # [aileron, elevator, rudder, throttle, weapon, message]
        pilot_action = self.applier.pilot_action # [aileron, elevator, rudder, throttle, weapon, message]
        # TODO: evaluate by similarity? (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)  -  (0,1,2,3,4,5,6,7,8,9,10)
        # max distance: 20, min distance:0, if distance==0; give max reward. if distance==20; give min reward.
        aileron_dist = abs(ai_action[0] - pilot_action[0])
        if aileron_dist == 0:
            aileron_sim = 1 / (aileron_dist + 0.25) # 4
        else:
            aileron_sim = 1 / aileron_dist

        elevator_dist = abs(ai_action[1] - pilot_action[1])
        if elevator_dist == 0:
            elevator_sim = 1 / (elevator_dist + 0.25) # 4
        else:
            elevator_sim = 1 / elevator_dist

        rudder_dist = abs(ai_action[2] - pilot_action[2])
        if rudder_dist == 0:
            rudder_sim = 1 / (rudder_dist + 0.25) # 4
        else:
            rudder_sim = 1 / rudder_dist

        throttle_dist = abs(ai_action[3] - pilot_action[3])
        if throttle_dist == 0:
            throttle_sim = 1 / (throttle_dist + 0.25) # 4
        else:
            throttle_sim = 1 / throttle_dist
        # scale similarities wrt priority (rudder have high importance wrt throttle) ? reward = (a * aileron_sim) + (e * elevator_sim) + (r * rudder_sim) + (t * throttle_sim)
        a,e,r,t = 0.1,0.1,0.1,0.1
        opinion = (a * aileron_sim) + (e * elevator_sim) + (r * rudder_sim) + (t * throttle_sim)
        # print("aileron_sim:{}  elevator_sim:{}  rudder_sim:{}  throttle_sim:{}    opinion:{}".format(aileron_sim,elevator_sim,rudder_sim,throttle_sim,opinion))
        return opinion
    """

    """
    def reward(self):
        self_info = self.info_store[0]
        target_info = self.info_store[1] # 1:F-4 Phantom 2:Baron
        #
        print("el:{} t_el:{} P:{} Q:{} R:{} the:{}  phi:{} psi:{} distance:{} rel_bearing:{}".format(
            self_info['elevation'],
            target_info['el'], self_info['P'], self_info['Q'], self_info['R'],
            self_info['theta'], self_info['phi'], self_info['psi'],
            target_info['distance'], target_info['rel_bearing']))

        # if self.done:
        #     reward = self.episode_reward()
        # else:
        #     reward = self.step_reward()
        reward = self.step_reward()
        return [reward]
    """

    def reward(self, info_store):

        self.info_store = info_store # update incoming stream
        int_info = self.info_store[0]

        # allowed_perturbation = [3.5, 15] # perturbation allowed on altitude and heading
        #TODO: relative elevation'a dikkat
        objective_state = [info_store[2]["psi"], info_store[2]["el"]]  # target situation -heading, altitude, and distance
        # gps_dme_distance_nm : distance to the target . This is distance along the heading and altitude.
        # this is set to motivate the agent to move forward in time . Accumulate distance
        heading = int_info['psi']
        altitude = int_info['elevation']

        # gps_dme_distance_nm = self.client.getDREF(self.gen_drefs["gps_dme_distance_nm"])[0][0]
        current_state = [heading, altitude]  # present situation -heading, altitude, and distance

        # if the heading and altitude are within small pertubation, set good reward, othewise penalize it.
        reward = self.gaussian_calculus(objective_state, current_state)[0]

        distance = self.info_store[2]["distance"]
        reward += self.distance_reward(distance)

        print("heading:{}  altitude:{}  distance:{}".format(heading, altitude, distance))
        # if (abs(current_state[0] - objective_state[0])) < allowed_perturbation[0] and (abs(current_state[1] - objective_state[1])) < allowed_perturbation[1]:
        #     reward = self.gaussian_calculus(objective_state, current_state, sigma=0.85)[0]
        #     print("small perturbation")
        # else:
        #     reward = -self.gaussian_calculus(objective_state, current_state)[0]
        #     print("large perturbation")

        # detect crash and penalize the agent
        # if crash add -3, otherwise reward remain same
        [onground_any, crash] = self.client.getDREFs([self.gen_drefs["onground_any"], self.gen_drefs["crash"]])
        # crash = self.client.getDREFs([self.gen_drefs.crash])[0][0]
        if onground_any[0] >= 1 or crash[0] <= 0:
            #TODO: -3 fena degil
            reward -= 3

        return reward

    # TODO: fazla yüksekte ani hareketler yapıyorsa ceza olabilir. (P Q R değerlerine göre)
