
def get_internal_datarefs():
	'''
	This function is used to define training parameters.
	This is separated from the main loop pf the program for ease of reference.
	There are many  state variables
	so that having them in a separate file is a good idea.
	'''


	# Global dictionary for acrquiring the parameters for the training
	globalDictionary = {
		# State Variables. This together with other parameters (to be defined later) will give us the
		# state of the aircraft. Note that this variables will be parsed to our function and the function
		# returns a set of values. check xplane dataref file for definition of stateVariable

		"elevation": "sim/flightmodel/position/elevation",

		"theta": "sim/flightmodel/position/theta", # pitch
		"phi": "sim/flightmodel/position/phi",     # roll
		"psi": "sim/flightmodel/position/psi",     # yaw (heading)

		"local_vx": "sim/flightmodel/position/local_vx",
		"local_vy": "sim/flightmodel/position/local_vy",
		"local_vz": "sim/flightmodel/position/local_vz",

		"P": "sim/flightmodel/position/P",
		"Q": "sim/flightmodel/position/Q",
		"R": "sim/flightmodel/position/R",

	}

	# globalDictionary = dotdict(globalDictionary) # make the dot notation for dictionary possible
	return globalDictionary

def get_internal_ghost_datarefs():
	globalDictionary = {

		"local_x": "sim/flightmodel/position/local_x",
		"local_y": "sim/flightmodel/position/local_y",
		"local_z": "sim/flightmodel/position/local_z",
		"latitude": "sim/flightmodel/position/latitude",
		"longitude": "sim/flightmodel/position/longitude",
		"elevation": "sim/flightmodel/position/elevation",

	}

	# globalDictionary = dotdict(globalDictionary) # make the dot notation for dictionary possible
	return globalDictionary

def get_external_datarefs(ac):
	globalDictionary = {

		"lat": "sim/multiplayer/position/plane{}_lat".format(ac),
		"lon": "sim/multiplayer/position/plane{}_lon".format(ac),
		"el": "sim/multiplayer/position/plane{}_el".format(ac),

		"x": "sim/multiplayer/position/plane{}_x".format(ac),
		"y": "sim/multiplayer/position/plane{}_y".format(ac),
		"z": "sim/multiplayer/position/plane{}_z".format(ac),

		"the": "sim/multiplayer/position/plane{}_the".format(ac),
		"phi": "sim/multiplayer/position/plane{}_phi".format(ac),
		"psi": "sim/multiplayer/position/plane{}_psi".format(ac),

		"v_x": "sim/multiplayer/position/plane{}_v_x".format(ac),
		"v_y": "sim/multiplayer/position/plane{}_v_y".format(ac),
		"v_z": "sim/multiplayer/position/plane{}_v_z".format(ac),

		"throttle": "sim/multiplayer/position/plane{}_throttle".format(ac),

	}

	# globalDictionary = dotdict(globalDictionary)
	return globalDictionary

def get_auxiliary_drefs():
	globalDictionary = {

		"relative_bearing_degs": "sim/cockpit2/tcas/indicators/relative_bearing_degs",
		"relative_distance_mtrs": "sim/cockpit2/tcas/indicators/relative_distance_mtrs",

		"onground_any": "sim/flightmodel/failures/onground_any",
		"tcas_num_acf": "sim/cockpit2/tcas/indicators/tcas_num_acf",
		"has_crashed": "sim/flightmodel2/misc/has_crashed",
		"crash": "sim/flightmodel/engine/ENGN_running",

	}

	# globalDictionary = dotdict(globalDictionary) # make the dot notation for dictionary possible
	return globalDictionary



def get_general_datarefs():
	globalDictionary = {

		"latitude": "sim/flightmodel/position/latitude",
		"longitude": "sim/flightmodel/position/longitude",
		"elevation": "sim/flightmodel/position/elevation",

		"local_x": "sim/flightmodel/position/local_x",
		"local_y": "sim/flightmodel/position/local_y",
		"local_z": "sim/flightmodel/position/local_z",

		"theta": "sim/flightmodel/position/theta", # pitch
		"phi": "sim/flightmodel/position/phi",     # roll
		"psi": "sim/flightmodel/position/psi",     # yaw (heading)

		"local_vx": "sim/flightmodel/position/local_vx",
		"local_vy": "sim/flightmodel/position/local_vy",
		"local_vz": "sim/flightmodel/position/local_vz",

		"P": "sim/flightmodel/position/P",
		"Q": "sim/flightmodel/position/Q",
		"R": "sim/flightmodel/position/R",

		"hstab1_elv2def": "sim/flightmodel/controls/hstab1_elv2def",
		"vstab2_rud1def": "sim/flightmodel/controls/vstab2_rud1def",

		"gps_dme_distance_nm": "sim/cockpit2/radios/indicators/gps_dme_distance_nm",
		"gps_bearing_deg_mag": "sim/cockpit2/radios/indicators/gps_bearing_deg_mag",

		"relative_bearing_degs": "sim/cockpit2/tcas/indicators/relative_bearing_degs",
		"relative_distance_mtrs": "sim/cockpit2/tcas/indicators/relative_distance_mtrs",

		"onground_any": "sim/flightmodel/failures/onground_any",
		"ai_flies_aircraft": "sim/operation/prefs/ai_flies_aircraft",
		"tcas_num_acf": "sim/cockpit2/tcas/indicators/tcas_num_acf",
		"has_crashed": "sim/flightmodel2/misc/has_crashed",


		"stateVariable" : ["sim/flightmodel/position/local_vx" ,"sim/flightmodel/position/local_vy",
						   "sim/flightmodel/position/local_vz"],

		# "sim/cockpit2/autopilot/gpss_status"
		"rewardVariable": "sim/cockpit2/radios/indicators/gps_dme_distance_nm",
		# ,"sim/cockpit2/radios/indicators/gps_dme_time_min",

		"headingReward" :"sim/cockpit2/radios/indicators/gps_bearing_deg_mag",

		# State variables values are stored in list sateVariableValue
		"stateVariableValue": [],

		# this is the timing data parameters from x plane DataRef. "sim/time/total_running_time_sec",
		"timer": "sim/time/total_flight_time_sec",
		"timer2": "sim/time/total_running_time_sec",  # sim/time/timer_elapsed_time_sec  sim/time/timer_is_running_sec
		# this is for timing data storage. It will be recovered from simulation
		"timerValue" : [None] ,
		"timerValue2": [None],
		"on_ground" :"sim/flightmodel2/gear/on_ground",
		"crash": "sim/flightmodel/engine/ENGN_running",
		"resetHold": [10.],
		"NumOfStatesAndPositions": 14,
		# Aircraft Position state Variables
		"stateAircraftPosition" : [],
		"episodeReward": 0.,
		"totalReward" :0.,
		"flag": False,
		"state" :[0. ,0. ,0. ,0. ,0. ,0. ,0.],
		"state14" :{"roll_rate" :0 ,"pitch_rate" :0, "altitude": 0 ,"Pitch" :0 ,"Roll" :0, "velocity_x": 0,  "velocity_y" :0 ,"velocity_z" :0 ,"delta_altitude" :0, "delta_heading" :0 ,"yaw_rate" :0},
		"episodeStep" :0,
		"reset" :False

	}

	# globalDictionary = dotdict(globalDictionary) # make the dot notation for dictionary possible
	return globalDictionary


def get_commands():
	globalDictionary = {

		"fire": "autodidactic/fire",
		"reset_flight": "sim/operation/reset_flight",

		"P": "sim/flightmodel/position/P",
		"Q": "sim/flightmodel/position/Q",
		"R": "sim/flightmodel/position/R",
		"local_vx": "sim/flightmodel/position/local_vx",
		"local_vy": "sim/flightmodel/position/local_vy",
		"local_vz": "sim/flightmodel/position/local_vz",
		"hstab1_elv2def": "sim/flightmodel/controls/hstab1_elv2def",
		"vstab2_rud1def": "sim/flightmodel/controls/vstab2_rud1def",

		"gps_dme_distance_nm": "sim/cockpit2/radios/indicators/gps_dme_distance_nm",
		"gps_bearing_deg_mag": "sim/cockpit2/radios/indicators/gps_bearing_deg_mag",

		"onground_any": "sim/flightmodel/failures/onground_any",
		"ai_flies_aircraft": "sim/operation/prefs/ai_flies_aircraft",


		"stateVariable" : ["sim/flightmodel/position/local_vx" ,"sim/flightmodel/position/local_vy",
						   "sim/flightmodel/position/local_vz"],

		# "sim/cockpit2/autopilot/gpss_status"
		"rewardVariable": "sim/cockpit2/radios/indicators/gps_dme_distance_nm",
		# ,"sim/cockpit2/radios/indicators/gps_dme_time_min",

		"headingReward" :"sim/cockpit2/radios/indicators/gps_bearing_deg_mag",

		# State variables values are stored in list sateVariableValue
		"stateVariableValue": [],

		# this is the timing data parameters from x plane DataRef. "sim/time/total_running_time_sec",
		"timer": "sim/time/total_flight_time_sec",
		"timer2": "sim/time/total_running_time_sec",  # sim/time/timer_elapsed_time_sec  sim/time/timer_is_running_sec
		# this is for timing data storage. It will be recovered from simulation
		"timerValue" : [None] ,
		"timerValue2": [None],
		"on_ground" :["sim/flightmodel2/gear/on_ground"],
		"crash": "sim/flightmodel/engine/ENGN_running",
		"resetHold": [10.],
		"NumOfStatesAndPositions": 14,
		# Aircraft Position state Variables
		"stateAircraftPosition" : [],
		"episodeReward": 0.,
		"totalReward" :0.,
		"flag": False,
		"state" :[0. ,0. ,0. ,0. ,0. ,0. ,0.],
		"state14" :{"roll_rate" :0 ,"pitch_rate" :0, "altitude": 0 ,"Pitch" :0 ,"Roll" :0, "velocity_x": 0,  "velocity_y" :0 ,"velocity_z" :0 ,"delta_altitude" :0, "delta_heading" :0 ,"yaw_rate" :0},
		"episodeStep" :0,
		"reset" :False

	}

	# globalDictionary = dotdict(globalDictionary) # make the dot notation for dictionary possible
	return globalDictionary


# class dotdict(dict):
#    """dot.notation access to dictionary attributes"""
#    __getattr__ = dict.get
#    __setattr__ = dict.__setitem__
#    __delattr__ = dict.__delitem__
