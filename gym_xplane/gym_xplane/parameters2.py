




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

		"plane{}_lat".format(ac): "sim/multiplayer/position/plane{}_lat".format(ac),
		"plane{}_lon".format(ac): "sim/multiplayer/position/plane{}_lon".format(ac),
		"plane{}_el".format(ac): "sim/multiplayer/position/plane{}_el".format(ac),

		"plane{}_x".format(ac): "sim/multiplayer/position/plane{}_x".format(ac),
		"plane{}_y".format(ac): "sim/multiplayer/position/plane{}_y".format(ac),
		"plane{}_z".format(ac): "sim/multiplayer/position/plane{}_z".format(ac),

		"plane{}_the".format(ac): "sim/multiplayer/position/plane{}_the".format(ac),
		"plane{}_phi".format(ac): "sim/multiplayer/position/plane{}_phi".format(ac),
		"plane{}_psi".format(ac): "sim/multiplayer/position/plane{}_psi".format(ac),

		"plane{}_v_x".format(ac): "sim/multiplayer/position/plane{}_v_x".format(ac),
		"plane{}_v_y".format(ac): "sim/multiplayer/position/plane{}_v_y".format(ac),
		"plane{}_v_z".format(ac): "sim/multiplayer/position/plane{}_v_z".format(ac),

		"plane{}_throttle".format(ac): "sim/multiplayer/position/plane{}_throttle".format(ac,ac),

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


		"stateVariable" : ["sim/flightmodel/position/local_vx","sim/flightmodel/position/local_vy",
		"sim/flightmodel/position/local_vz"],

		# "sim/cockpit2/autopilot/gpss_status"
		"rewardVariable": "sim/cockpit2/radios/indicators/gps_dme_distance_nm", #,"sim/cockpit2/radios/indicators/gps_dme_time_min",

		"headingReward":"sim/cockpit2/radios/indicators/gps_bearing_deg_mag",

		# State variables values are stored in list sateVariableValue
		"stateVariableValue": [],

		# this is the timing data parameters from x plane DataRef. "sim/time/total_running_time_sec",
		"timer": "sim/time/total_flight_time_sec",
		"timer2": "sim/time/total_running_time_sec",  # sim/time/timer_elapsed_time_sec  sim/time/timer_is_running_sec
		# this is for timing data storage. It will be recovered from simulation
		"timerValue" : [None] ,
		"timerValue2": [None],
		"on_ground":"sim/flightmodel2/gear/on_ground",
		"crash": "sim/flightmodel/engine/ENGN_running",
		"resetHold": [10.],
		"NumOfStatesAndPositions": 14,
		# Aircraft Position state Variables
		"stateAircraftPosition" : [],
		"episodeReward": 0.,
		"totalReward":0.,
		"flag": False,
		"state":[0.,0.,0.,0.,0.,0.,0.],
		"state14":{"roll_rate":0,"pitch_rate":0, "altitude": 0,"Pitch":0,"Roll":0, "velocity_x": 0,  "velocity_y":0,"velocity_z":0,"delta_altitude":0, "delta_heading":0,"yaw_rate":0},
		"episodeStep":0,
		"reset":False

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


		"stateVariable" : ["sim/flightmodel/position/local_vx","sim/flightmodel/position/local_vy",
		"sim/flightmodel/position/local_vz"],

		# "sim/cockpit2/autopilot/gpss_status"
		"rewardVariable": "sim/cockpit2/radios/indicators/gps_dme_distance_nm", #,"sim/cockpit2/radios/indicators/gps_dme_time_min",

		"headingReward":"sim/cockpit2/radios/indicators/gps_bearing_deg_mag",

		# State variables values are stored in list sateVariableValue
		"stateVariableValue": [],

		# this is the timing data parameters from x plane DataRef. "sim/time/total_running_time_sec",
		"timer": "sim/time/total_flight_time_sec",
		"timer2": "sim/time/total_running_time_sec",  # sim/time/timer_elapsed_time_sec  sim/time/timer_is_running_sec
		# this is for timing data storage. It will be recovered from simulation
		"timerValue" : [None] ,
		"timerValue2": [None],
		"on_ground":["sim/flightmodel2/gear/on_ground"],
		"crash": "sim/flightmodel/engine/ENGN_running",
		"resetHold": [10.],
		"NumOfStatesAndPositions": 14,
		# Aircraft Position state Variables
		"stateAircraftPosition" : [],
		"episodeReward": 0.,
		"totalReward":0.,
		"flag": False,
		"state":[0.,0.,0.,0.,0.,0.,0.],
		"state14":{"roll_rate":0,"pitch_rate":0, "altitude": 0,"Pitch":0,"Roll":0, "velocity_x": 0,  "velocity_y":0,"velocity_z":0,"delta_altitude":0, "delta_heading":0,"yaw_rate":0},
		"episodeStep":0,
		"reset":False

		}

	# globalDictionary = dotdict(globalDictionary) # make the dot notation for dictionary possible
	return globalDictionary

#############################################################################################################################################################################################
#############################################################################################################################################################################################
#############################################################################################################################################################################################
#############################################################################################################################################################################################
#############################################################################################################################################################################################
#############################################################################################################################################################################################

def get_position_drefs():
	globalDictionary = {

		"position/latitude": "sim/flightmodel/position/latitude",
		"position/longitude": "sim/flightmodel/position/longitude",
		"position/local_x": "sim/flightmodel/position/local_x",
		"position/local_y": "sim/flightmodel/position/local_y",
		"position/local_z": "sim/flightmodel/position/local_z",
		"position/v_elevation": "sim/flightmodel/position/elevation",
		"position/v_theta": "sim/flightmodel/position/theta", # pitch
		"position/v_phi": "sim/flightmodel/position/phi",     # roll
		"position/v_psi": "sim/flightmodel/position/psi",     # yaw (heading)
		"position/v_local_vx": "sim/flightmodel/position/local_vx",
		"position/v_local_vy": "sim/flightmodel/position/local_vy",
		"position/v_local_vz": "sim/flightmodel/position/local_vz",
		"position/v_P": "sim/flightmodel/position/P",
		"position/v_Q": "sim/flightmodel/position/Q",
		"position/v_R": "sim/flightmodel/position/R",

		# "position/v_r_plane1_lat": "sim/multiplayer/position/plane1_lat",
		# "position/v_r_plane1_lon": "sim/multiplayer/position/plane1_lon",
		# "position/v_r_plane1_el": "sim/multiplayer/position/plane1_el",
		# "position/v_r_plane1_x": "sim/multiplayer/position/plane1_x",
		# "position/v_r_plane1_y": "sim/multiplayer/position/plane1_y",
		# "position/v_r_plane1_z": "sim/multiplayer/position/plane1_z",
		# "position/v_plane1_the": "sim/multiplayer/position/plane1_the",
		# "position/v_plane1_phi": "sim/multiplayer/position/plane1_phi",
		# "position/v_plane1_psi": "sim/multiplayer/position/plane1_psi",
		# "position/v_plane1_v_x": "sim/multiplayer/position/plane1_v_x",
		# "position/v_plane1_v_y": "sim/multiplayer/position/plane1_v_y",
		# "position/v_plane1_v_z": "sim/multiplayer/position/plane1_v_z",
		# "position/v_plane1_throttle": "sim/multiplayer/position/plane1_throttle",
		#
		# "position/v_r_plane2_lat": "sim/multiplayer/position/plane2_lat",
		# "position/v_r_plane2_lon": "sim/multiplayer/position/plane2_lon",
		# "position/v_r_plane2_el": "sim/multiplayer/position/plane2_el",
		# "position/v_r_plane2_x": "sim/multiplayer/position/plane2_x",
		# "position/v_r_plane2_y": "sim/multiplayer/position/plane2_y",
		# "position/v_r_plane2_z": "sim/multiplayer/position/plane2_z",
		# "position/v_plane2_the": "sim/multiplayer/position/plane2_the",
		# "position/v_plane2_phi": "sim/multiplayer/position/plane2_phi",
		# "position/v_plane2_psi": "sim/multiplayer/position/plane2_psi",
		# "position/v_plane2_v_x": "sim/multiplayer/position/plane2_v_x",
		# "position/v_plane2_v_y": "sim/multiplayer/position/plane2_v_y",
		# "position/v_plane2_v_z": "sim/multiplayer/position/plane2_v_z",
		# "position/v_plane2_throttle": "sim/multiplayer/position/plane2_throttle",
		#
		# "position/v_r_plane3_lat": "sim/multiplayer/position/plane3_lat",
		# "position/v_r_plane3_lon": "sim/multiplayer/position/plane3_lon",
		# "position/v_r_plane3_el": "sim/multiplayer/position/plane3_el",
		# "position/v_r_plane3_x": "sim/multiplayer/position/plane3_x",
		# "position/v_r_plane3_y": "sim/multiplayer/position/plane3_y",
		# "position/v_r_plane3_z": "sim/multiplayer/position/plane3_z",
		# "position/v_plane3_the": "sim/multiplayer/position/plane3_the",
		# "position/v_plane3_phi": "sim/multiplayer/position/plane3_phi",
		# "position/v_plane3_psi": "sim/multiplayer/position/plane3_psi",
		# "position/v_plane3_v_x": "sim/multiplayer/position/plane3_v_x",
		# "position/v_plane3_v_y": "sim/multiplayer/position/plane3_v_y",
		# "position/v_plane3_v_z": "sim/multiplayer/position/plane3_v_z",
		# "position/v_plane3_throttle": "sim/multiplayer/position/plane3_throttle",
		#
		# "position/v_r_plane4_lat": "sim/multiplayer/position/plane4_lat",
		# "position/v_r_plane4_lon": "sim/multiplayer/position/plane4_lon",
		# "position/v_r_plane4_el": "sim/multiplayer/position/plane4_el",
		# "position/v_r_plane4_x": "sim/multiplayer/position/plane4_x",
		# "position/v_r_plane4_y": "sim/multiplayer/position/plane4_y",
		# "position/v_r_plane4_z": "sim/multiplayer/position/plane4_z",
		# "position/v_plane4_the": "sim/multiplayer/position/plane4_the",
		# "position/v_plane4_phi": "sim/multiplayer/position/plane4_phi",
		# "position/v_plane4_psi": "sim/multiplayer/position/plane4_psi",
		# "position/v_plane4_v_x": "sim/multiplayer/position/plane4_v_x",
		# "position/v_plane4_v_y": "sim/multiplayer/position/plane4_v_y",
		# "position/v_plane4_v_z": "sim/multiplayer/position/plane4_v_z",
		# "position/v_plane4_throttle": "sim/multiplayer/position/plane4_throttle",
		#
		# "position/v_r_plane5_lat": "sim/multiplayer/position/plane5_lat",
		# "position/v_r_plane5_lon": "sim/multiplayer/position/plane5_lon",
		# "position/v_r_plane5_el": "sim/multiplayer/position/plane5_el",
		# "position/v_r_plane5_x": "sim/multiplayer/position/plane5_x",
		# "position/v_r_plane5_y": "sim/multiplayer/position/plane5_y",
		# "position/v_r_plane5_z": "sim/multiplayer/position/plane5_z",
		# "position/v_plane5_the": "sim/multiplayer/position/plane5_the",
		# "position/v_plane5_phi": "sim/multiplayer/position/plane5_phi",
		# "position/v_plane5_psi": "sim/multiplayer/position/plane5_psi",
		# "position/v_plane5_v_x": "sim/multiplayer/position/plane5_v_x",
		# "position/v_plane5_v_y": "sim/multiplayer/position/plane5_v_y",
		# "position/v_plane5_v_z": "sim/multiplayer/position/plane5_v_z",
		# "position/v_plane5_throttle": "sim/multiplayer/position/plane5_throttle"

	}

	return globalDictionary

def get_tcas_drefs():
	globalDictionary = {
		"tcas/v_relative_bearing_degs": "sim/cockpit2/tcas/indicators/relative_bearing_degs",
		"tcas/v_relative_distance_mtrs": "sim/cockpit2/tcas/indicators/relative_distance_mtrs"
	}

	return globalDictionary

def get_weapons_drefs():
	pass

def get_global_drefs():
	globalDictionary = {

		"global/onground_any": "sim/flightmodel/failures/onground_any",
		#"global/tcas_num_acf": "sim/cockpit2/tcas/indicators/tcas_num_acf",
		"global/has_crashed": "sim/flightmodel2/misc/has_crashed",
		"global/ENGN_running": "sim/flightmodel/engine/ENGN_running"

	}

	return globalDictionary





def get_position_encode_params():  # min_lim, max_lim, vector_dim, value, name, binary_suitable=False
	globalDictionary = {

		"elevation": {'min_lim': 0, 'max_lim': 15000, 'vector_dim': 100, 'name': 'elevation', 'binary_suitable': False},
		"theta": {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'name': 'theta', 'binary_suitable': False},
		"phi": {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'name': 'phi', 'binary_suitable': False},
		"psi": {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'name': 'psi', 'binary_suitable': False},
		"local_vx": {'min_lim': -200, 'max_lim': 200, 'vector_dim': 40, 'name': 'local_vx', 'binary_suitable': False},
		"local_vy": {'min_lim': -300, 'max_lim': 300, 'vector_dim': 60, 'name': 'local_vy', 'binary_suitable': False},
		"local_vz": {'min_lim': -600, 'max_lim': 600, 'vector_dim': 120, 'name': 'local_vz', 'binary_suitable': False},
		"P": {'min_lim': -300, 'max_lim': 300, 'vector_dim': 60, 'name': 'P', 'binary_suitable': False},
		"Q": {'min_lim': -100, 'max_lim': 100, 'vector_dim': 20, 'name': 'Q', 'binary_suitable': False},
		"R": {'min_lim': -200, 'max_lim': 200, 'vector_dim': 40, 'name': 'R', 'binary_suitable': False},

		"plane1_lat": {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'name': 'plane1_lat', 'binary_suitable': False},
		"plane1_lon": {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'name': 'plane1_lon', 'binary_suitable': False},
		"plane1_el": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'name': 'plane1_el', 'binary_suitable': False},
		"plane1_x": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane1_x', 'binary_suitable': False},
		"plane1_y": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'name': 'plane1_y', 'binary_suitable': False},
		"plane1_z": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane1_z', 'binary_suitable': False},
		"plane1_the": {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'name': 'plane1_the', 'binary_suitable': False},
		"plane1_phi": {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'name': 'plane1_phi', 'binary_suitable': False},
		"plane1_psi": {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'name': 'plane1_psi', 'binary_suitable': False},
		"plane1_v_x": {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'name': 'plane1_v_x', 'binary_suitable': False},
		"plane1_v_y": {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'name': 'plane1_v_y', 'binary_suitable': False},
		"plane1_v_z": {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'name': 'plane1_v_z', 'binary_suitable': False},
		"plane1_throttle": {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'name': 'plane1_throttle', 'binary_suitable': False},

		"plane2_lat": {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'name': 'plane2_lat', 'binary_suitable': False},
		"plane2_lon": {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'name': 'plane2_lon', 'binary_suitable': False},
		"plane2_el": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'name': 'plane2_el', 'binary_suitable': False},
		"plane2_x": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane2_x', 'binary_suitable': False},
		"plane2_y": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'name': 'plane2_y', 'binary_suitable': False},
		"plane2_z": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane2_z', 'binary_suitable': False},
		"plane2_the": {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'name': 'plane2_the', 'binary_suitable': False},
		"plane2_phi": {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'name': 'plane2_phi', 'binary_suitable': False},
		"plane2_psi": {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'name': 'plane2_psi', 'binary_suitable': False},
		"plane2_v_x": {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'name': 'plane2_v_x', 'binary_suitable': False},
		"plane2_v_y": {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'name': 'plane2_v_y', 'binary_suitable': False},
		"plane2_v_z": {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'name': 'plane2_v_z', 'binary_suitable': False},
		"plane2_throttle": {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'name': 'plane2_throttle', 'binary_suitable': False},

		"plane3_lat": {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'name': 'plane3_lat', 'binary_suitable': False},
		"plane3_lon": {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'name': 'plane3_lon', 'binary_suitable': False},
		"plane3_el": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'name': 'plane3_el', 'binary_suitable': False},
		"plane3_x": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane3_x', 'binary_suitable': False},
		"plane3_y": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'name': 'plane3_y', 'binary_suitable': False},
		"plane3_z": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane3_z', 'binary_suitable': False},
		"plane3_the": {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'name': 'plane3_the', 'binary_suitable': False},
		"plane3_phi": {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'name': 'plane3_phi', 'binary_suitable': False},
		"plane3_psi": {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'name': 'plane3_psi', 'binary_suitable': False},
		"plane3_v_x": {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'name': 'plane3_v_x', 'binary_suitable': False},
		"plane3_v_y": {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'name': 'plane3_v_y', 'binary_suitable': False},
		"plane3_v_z": {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'name': 'plane3_v_z', 'binary_suitable': False},
		"plane3_throttle": {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'name': 'plane3_throttle', 'binary_suitable': False},

		"plane4_lat": {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'name': 'plane4_lat', 'binary_suitable': False},
		"plane4_lon": {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'name': 'plane4_lon', 'binary_suitable': False},
		"plane4_el": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'name': 'plane4_el', 'binary_suitable': False},
		"plane4_x": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane4_x', 'binary_suitable': False},
		"plane4_y": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'name': 'plane4_y', 'binary_suitable': False},
		"plane4_z": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane4_z', 'binary_suitable': False},
		"plane4_the": {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'name': 'plane4_the', 'binary_suitable': False},
		"plane4_phi": {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'name': 'plane4_phi', 'binary_suitable': False},
		"plane4_psi": {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'name': 'plane4_psi', 'binary_suitable': False},
		"plane4_v_x": {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'name': 'plane4_v_x', 'binary_suitable': False},
		"plane4_v_y": {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'name': 'plane4_v_y', 'binary_suitable': False},
		"plane4_v_z": {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'name': 'plane4_v_z', 'binary_suitable': False},
		"plane4_throttle": {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'name': 'plane4_throttle', 'binary_suitable': False},

		"plane5_lat": {'min_lim': -2, 'max_lim': 2, 'vector_dim': 200, 'name': 'plane5_lat', 'binary_suitable': False},
		"plane5_lon": {'min_lim': -3, 'max_lim': 3, 'vector_dim': 200, 'name': 'plane5_lon', 'binary_suitable': False},
		"plane5_el": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 50, 'name': 'plane5_el', 'binary_suitable': False},
		"plane5_x": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane5_x', 'binary_suitable': False},
		"plane5_y": {'min_lim': -10000, 'max_lim': 10000, 'vector_dim': 100, 'name': 'plane5_y', 'binary_suitable': False},
		"plane5_z": {'min_lim': -100000, 'max_lim': 100000, 'vector_dim': 100, 'name': 'plane5_z', 'binary_suitable': False},
		"plane5_the": {'min_lim': -90, 'max_lim': 90, 'vector_dim': 30, 'name': 'plane5_the', 'binary_suitable': False},
		"plane5_phi": {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'name': 'plane5_phi', 'binary_suitable': False},
		"plane5_psi": {'min_lim': 0, 'max_lim': 360, 'vector_dim': 60, 'name': 'plane5_psi', 'binary_suitable': False},
		"plane5_v_x": {'min_lim': -400, 'max_lim': 400, 'vector_dim': 20, 'name': 'plane5_v_x', 'binary_suitable': False},
		"plane5_v_y": {'min_lim': -300, 'max_lim': 300, 'vector_dim': 30, 'name': 'plane5_v_y', 'binary_suitable': False},
		"plane5_v_z": {'min_lim': -600, 'max_lim': 600, 'vector_dim': 60, 'name': 'plane5_v_z', 'binary_suitable': False},
		"plane5_throttle": {'min_lim': 0, 'max_lim': 1, 'vector_dim': 10, 'name': 'plane5_throttle', 'binary_suitable': False}

	}

	return globalDictionary

def get_tcas_encode_params():
	globalDictionary = {

		"relative_bearing_degs": {'min_lim': -180, 'max_lim': 180, 'vector_dim': 60, 'name': 'relative_bearing_degs', 'binary_suitable': False},
		"relative_distance_mtrs": {'min_lim': 0, 'max_lim': 100000, 'vector_dim': 100, 'name': 'relative_distance_mtrs', 'binary_suitable': False}

	}

	return globalDictionary



# class dotdict(dict):
#    """dot.notation access to dictionary attributes"""
#    __getattr__ = dict.get
#    __setattr__ = dict.__setitem__
#    __delattr__ = dict.__delitem__
