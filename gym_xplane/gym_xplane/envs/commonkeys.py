GENERAL = "GENERAL"
DAMAGE = "damage"
FORCE = "force"
ID = 'ID'
SELF = "self"
ENTITY = "entity"
RESET = "reset"
ISFIRED = "isfired"

MOTION = "MOTION"
MYSPEED = "mySpeed"
MYHEADING = "myHeading"
MSLALTITUDE = "msla_altitude"
AGLALTITUDE = "agla_altitude"
TERRAINALTITUDE = "terrain_altitude"
ECEF = "ecef"  # outputu liste olcak [x,y,z]
LLA = "lla"  # outputu [latitude, longtitude]
RELATIVEBEARING = "relative_bearing_dict"
BEARING = "bearing_dict"
DISTANCE = "distance"
ENTITYDICT = "EntityDict"
WHOAMI = "WhoAmI"
MESSAGE = "Message"
MESSAGESENDER = "message_sender"
MESSAGESUBJECT = "message_subject"
COMM = "communication"
ENGAGECOMMAND = "engageCommand"
TARGETENTITY = "targetEntity"
COMMANDERENTITY = "commanderEntity"
CLOSERADARCOMMAND = "closeradar_command"
TURNCOMMAND = "turn_command"
FUELCOMMAND = "fuel_command"
TARGETMISSILE = "target_missile"

IFF = "iff"
IFF_UNKNOWN = "iff_unknown"
IFF_FRIEND = "iff_friend"
IFF_HOSTILE = "iff_hostile"

FORCE = "force"
FORCE_FRIEND = "force_friend"
FORCE_ENEMY = "force_enemy"

MUNITION = "munition"
MISSILECOUNT = "missileCount"
ROCKETCOUNT = "rocketCount"
BULLETCOUNT = "bulletCount"
IRFLARECOUNT = "IRFlareCount"
LASERGUIDEDMISSILECOUNT = "laserGuidedMissileCount"
RADARGUIDEDMISSILECOUNT = "radarGuidedMissileCount"
IRGUIDEDMISSILECOUNT = "IRGuidedMissileCount"
EOGUIDEDMISSILECOUNT = "EOGuidedMissileCount"
WIREGUIDEDMISSILECOUNT = "wireGuidedMissileCount"
PROJECTILESHOTBULLETCOUNT = "projectileShotBulletCount"
FLATSHOTBULLETCOUNT = "flatShotBulletCount"
CHAFFCOUNT = "chaffCount"
ILLUMINATIONFLARECOUNT = "illuminationFlareCount"
BOMBCOUNT = "bombCount"
SMOKECOUNT = "smokeCount"
DECOYCOUNT = "decoyCount"
ACTIVERADARGUIDEDMISSILECOUNT = "activeRadarGuidedMissileCount"
SEMIACTIVERADARGUIDEDMISSILECOUNT = "semiActiveRadarGuidedMissileCount"
PASSIVERADARGUIDEDMISSILECOUNT = "passiveRadarGuidedMissileCount"

ASSETTYPE = "assetType"
ISPLATFORM = "isPlatform"
ISAIRPLATFORM = "isAirPlatform"
ISGROUNDPLATFORM = "isGroundPlatform"
ISFIXEDWING = "isFixedWing"
ISROTARYWING = "isRotaryWing"
ISSHIP = "isShip"
ISLIFEFORM = "isLifeForm"
ISUAV = "isUAV"

DISCODE = "DISCode"
ENTITYKIND = "entityKind"
COUNTRYCODE = "countryCode"
CATEGORY = "category"
SUBCATEGORY = "subCategory"
SPECIFIC = "specific"
EXTRA = "extra"
DOMAIN = "domain"

CHAFFRELEASEFLAG = "chaffReleaseFlag"
FLARERELEASEFLAG = "flareReleaseFlag"
RUNAWAYDIRECTION = "runAwayDirection"


SENSOR = "sensor"
ISRWR = "is_receiving_rwr_signal"
ISMWR = "is_receiving_mwr_signal"
ISLWR = "is_receiving_lwr_signal"
TIMERWR = "get_rwr_collision_time"
TIMEMWR = "get_mwr_collision_time"
ANGLERWR = "detected_angle_of_rwr"
ANGLEMWR = "detected_angle_of_mwr"
ANGLELWR = "detected_angle_of_lwr"
ISRADARIO = "is_radar_in_operation"
ISRADARSEARCH = "is_radar_in_search"
ISRADARTRACK = "is_radar_in_track"
ISLASERIO = "is_laser_in_operation"
ISLASERDESIGNATION = "is_laser_in_designation"
ISLASERRANGEFIND = "is_laser_in_rangefind"
ISIFFIO = "is_iff_in_operation"
ISEOIO = "is_eo_in_operation"
ISIRJAMMERIO = "is_irjammer_in_operation"
ISLASERJAMMERIO = "is_laserJammer_in_operation"
ISRADARJAMMERIO = "is_radarJammer_in_operation"
ISRADIOJAMMERIO = "is_radioJammer_in_operation"
ISGPSJAMMERIO = "is_gpsJammer_in_operation"
ISIRBEACONIO = "is_irBeacon_in_operation"
ISLASERPOINTERIO = "is_laserPointer_in_operation"
ACQUISITION = "acquisition"

HASRADARSUBSYSTEM = "hasRadarSubsystem"
HASLASERSUBSYSTEM = "hasLaserSubsystem"
HASIFFSUBSYSTEM = "hasIFFSubsystem"
HASEOSUBSYSTEM = "hasEOSubsystem"
HASRWRSUBSYSTEM = "hasRWRSubsystem"
HASMWRSUBSYSTEM = "hasMWRSubsystem"
HASLWRSUBSYSTEM = "hasLWRSubsystem"
HASRADARJAMMERSUBSYSTEM = "hasRadarJammerSubsystem"
HASLASERJAMMERSUBSYSTEM = "hasLaserJammerSubsystem"
HASIRJAMMERSUBSYSTEM = "hasIRJammerSubsystem"


ROUTE = "route"
HASROUTE = "hasRoute"
ISROUTEACTIVE = "isRouteActive"
ROUTEPOINTCOORDINATE = "routePointCoordinate"

HASPOENTITY = "hasPOEntity"
EFFECTIVERANGE = "effectiveRange"
SIZE = "size"

POENTITY = "POEntity"
HASSUBSYSTEM = "hasSubsystem"

NONEMISSILE = "noneMissile"
LASERGUIDEDMISSILE = "laserGuidedMissile"
ACTIVERADARGUIDEDMISSILE = "activeRadarGuidedMissile"
IRGUIDEDMISSILE = "IRGuidedMissile"
SEMIACTIVERADARGUIDEDMISSILE = "SemiActiveRadarGuidedMissile"
PASSIVERADARGUIDEDMISSILE = "PassiveRadarGuidedMissile"
EOGUIDEDMISSILE = "EOGuidedMissile"
WIREGUIDEDMISSILE = "WireGuidedMissile"

ENTITYINRANGE = "entityInRange"
DIVERANGE = "diveRange"
FIRINGRANGE = "firingRange"
ENTITYINEFFECTIVERANGE = "entityInEffectiveRange"
ENTITYINDIVERANGE = "entityInDiveRange"
ENTITYINFIRINGRANGE = "entityInFiringRange"
ENTITYINGUNRANGE = "gun_range"

MISSILEINGUNRANGE = "missileInGunRange"

FORMATION = "formation"
FORMATIONORDER = "formationOrder"

FUEL = "fuel"
FUELAMOUNT = "fuelAmount"

WEATHERCONDITIONS = "wheatherConditions"
PRECIPITATIONTYPE = "precipitationType"
PRECIPITATIONLEVEL = "precipitationLevel"
CLOUDCOVERAGELEVEL = "cloudCoverageLevel"
CLOUDTOPINMETERS = "cloudTopInMeters"
CLOUDBOTTOMINMETERS = "cloudBottomInMeters"
VISIBILITYINMETERS = "visibilityInMeters"
TEMPERATUREINCELCIUS = "temperatureInCelcius"
WINDDIRECTIONINDEGREES = "windDirectionInDegrees"
WINDSPEEDINKNOTS = "windSpeedInKnots"

TIME = "time"
ELAPSEDTIMEINSECONDS = "elapsedTimeInSeconds"

CURRENTSCENARIODATETIMEYEAR = "currentScenarioDateTimeYear"
CURRENTSCENARIODATETIMEMONTH = "currentScenarioDateTimeMonth"
CURRENTSCENARIODATETIMEDAY = "currentScenarioDateTimeDay"
CURRENTSCENARIODATETIMEHOUR = "currentScenarioDateTimeHour"
CURRENTSCENARIODATETIMEMINUTE = "currentScenarioDateTimeMinute"
CURRENTSCENARIODATETIMESECOND = "currentScenarioDateTimeSecond"

MISSILETHREAT = "missile_threat"
ARMTHREAT = "ARM_threat"

# MISSILE
MISSILE = "missile"
MISSILEENTITYDICT = "MissileEntityDict"
OWNER = "Owner"
MISSILEHELPER = "MissileDict"


TARGET_ENTITY_ID = "target_entity_ID"
SELECTED_SEEKER_TYPE = "selected_seeker_type"
FIREANDREMEMBER = "fire_and_remember"



TRACKTIMER = "track_timer"



# INDEX KEYWORDS FOR RULEAGENTS
SELF_MSL_ALT_INDEX=0
SELF_AGL_ALT_INDEX=1
SELF_SPEED_INDEX=2
SELF_HEADING_INDEX=3

SELF_GET_MISSILE_COUNT_INDEX=4
SELF_GET_ROCKET_COUNT_INDEX=5
SELF_GET_BULLET_COUNT_INDEX=6
SELF_GET_IR_FLARE_COUNT_INDEX=7
SELF_GET_LASER_GUIDED_MISSILE_COUNT_INDEX=8
SELF_GET_RADAR_GUIDED_MISSILE_COUNT_INDEX=9
SELF_GET_IR_GUIDED_MISSILE_COUNT_INDEX=10
SELF_GET_EO_GUIDED_MISSILE_COUNT_INDEX=11
SELF_GET_PROJECTILE_SHOT_BULLET_COUNT_INDEX=12
SELF_GET_FLAT_SHOT_BULLET_COUNT_INDEX=13
SELF_GET_CHAFF_COUNT_INDEX=14
SELF_GET_SMOKE_COUNT_INDEX=15
SELF_GET_ACTIVE_RADAR_GUIDED_MISSILE_COUNT_INDEX=16
SELF_GET_SEMI_ACTIVE_RADAR_GUIDED_MISSILE_COUNT_INDEX=17
SELF_GET_PASSIVE_RADAR_GUIDED_MISSILE_COUNT_INDEX=18

SELF_IS_PLATFORM_INDEX=19
SELF_IS_AIR_PLATFORM_INDEX=20
SELF_IS_GROUND_PLATFORM_INDEX=21
SELF_IS_FIXED_WING_INDEX=22
SELF_IS_ROTARY_WING_INDEX=23
SELF_IS_SHIP_INDEX=24
SELF_IS_LIFE_FORM_INDEX=25
SELF_IS_UAV_INDEX=26
SELF_IS_ANKA_INDEX=27
SELF_IS_F_16_INDEX=28
SELF_IS_F_22_INDEX=29
SELF_IS_F_35_INDEX=30
SELF_IS_F_4_INDEX=31
SELF_IS_MIG_29_INDEX=32
SELF_IS_SA_10_INDEX=33
SELF_IS_PEACEEAGLE_INDEX=34
SELF_IS_SU_27_INDEX=35
SELF_IS_SU_35_INDEX=36
SELF_IS_FIRTINAOBUS_INDEX=37
SELF_IS_LEOPARD_2_INDEX=38
SELF_IS_SA_6_INDEX=39
SELF_IS_TUNGUSKA_INDEX=40
SELF_IS_ATAK_INDEX=41
SELF_IS_UNKNOWN_INDEX=42

SELF_IS_RWR_INDEX=43
SELF_IS_MWR_INDEX=44
SELF_IS_LWR_INDEX=45
SELF_RWR_COLLISION_TIME_INDEX=46
SELF_MWR_COLLISION_TIME_INDEX=47
SELF_RWR_ANGLE_INDEX=48
SELF_MWR_ANGLE_INDEX=49
SELF_LWR_ANGLE_INDEX=50
SELF_IS_RADAR_IO_INDEX=51
SELF_IS_RADAR_SEARCH_INDEX=52
SELF_IS_RADAR_TRACK_INDEX=53
SELF_IS_LASER_IO_INDEX=54
SELF_IS_LASER_DESIGNATION_INDEX=55
SELF_IS_IFF_IN_OPERATION_INDEX=56
SELF_IS_EO_DEVICE_IN_OPERATION_INDEX=57
SELF_IS_IR_JAMMER_IO_INDEX=58
SELF_IS_LASER_JAMMER_IO_INDEX=59
SELF_IS_RADAR_JAMMER_IO_INDEX=60

SELF_HAS_RADAR_SUBSYSTEM_INDEX=61
SELF_HAS_LASER_SUBSYSTEM_INDEX=62
SELF_HAS_IFF_SUBSYSTEM_INDEX=63
SELF_HAS_EO_SUBSYSTEM_INDEX=64
SELF_HAS_RWR_SUBSYSTEM_INDEX=65
SELF_HAS_MWR_SUBSYSTEM_INDEX=66
SELF_HAS_LWR_SUBSYSTEM_INDEX=67
SELF_HAS_RADAR_JAMMER_SUBSYSTEM_INDEX=68
SELF_HAS_LASER_JAMMER_SUBSYSTEM_INDEX=69
SELF_HAS_IR_JAMMER_SUBSYSTEM_INDEX=70

SELF_HAS_PO_ENTITY_INDEX=71

SELF_HAS_ROUTE_INDEX=72
SELF_IS_ROUTE_ACTIVE_INDEX=73
SELF_RELATIVE_WAYPOINT_LLA_LAT_INDEX=74
SELF_RELATIVE_WAYPOINT_LLA_LONG_INDEX=75
SELF_RELATIVE_WAYPOINT_LLA_ALT_INDEX=76

SELF_ENGAGE_COMMAND_INDEX=77

SELF_DAMAGE_INDEX=78

SELF_IS_FIRED_INDEX=79

SELF_IS_CHAFF_RELEASED_INDEX=80

SELF_IS_FLARE_RELEASED_INDEX=81

SELF_RUNAWAY_DIRECTION=82
#
SELF_STATE_SIZE=83


ENTITY_RELATIVE_ECEF_X_WRT_SELF_INDEX=0
ENTITY_RELATIVE_ECEF_Y_WRT_SELF_INDEX=1
ENTITY_RELATIVE_ECEF_Z_WRT_SELF_INDEX=2
ENTITY_RELATIVE_LLA_LAT_WRT_SELF_INDEX=3
ENTITY_RELATIVE_LLA_LONG_WRT_SELF_INDEX=4
ENTITY_RELATIVE_MSL_ALT_WRT_SELF_INDEX=5
ENTITY_RELATIVE_AGL_ALT_WRT_SELF_INDEX=6
ENTITY_SPEED_INDEX=7
ENTITY_HEADING_INDEX=8
ENTITY_RELATIVE_BEARING_ANGLE_WRT_ENTITY_INDEX=9
ENTITY_BEARING_ANGLE_WRT_ENTITY_INDEX=10
ENTITY_DISTANCE_WRT_ENTITY_INDEX=11

ENTITY_IS_UNKNOWN_INDEX=12
ENTITY_IS_FRIEND_INDEX=13
ENTITY_IS_HOSTILE_INDEX=14
ENTITY_FORCE_FRIEND_INDEX=15
ENTITY_FORCE_ENEMY_INDEX=16

ENTITY_IS_PLATFORM_INDEX=17
ENTITY_IS_AIR_PLATFORM_INDEX=18
ENTITY_IS_GROUND_PLATFORM_INDEX=19
ENTITY_IS_FIXED_WING_INDEX=20
ENTITY_IS_ROTARY_WING_INDEX=21
ENTITY_IS_SHIP_INDEX=22
ENTITY_IS_LIFE_FORM_INDEX=23
ENTITY_IS_UAV_INDEX=24
ENTITY_IS_ANKA_INDEX=25
ENTITY_IS_F_16_INDEX=26
ENTITY_IS_F_22_INDEX=27
ENTITY_IS_F_35_INDEX=28
ENTITY_IS_F_4_INDEX=29
ENTITY_IS_MIG_29_INDEX=30
ENTITY_IS_SA_10_INDEX=31
ENTITY_IS_PEACEEAGLE_INDEX=32
ENTITY_IS_SU_27_INDEX=33
ENTITY_IS_SU_35_INDEX=34
ENTITY_IS_FIRTINAOBUS_INDEX=35
ENTITY_IS_LEOPARD_2_INDEX=36
ENTITY_IS_SA_6_INDEX=37
ENTITY_IS_TUNGUSKA_INDEX=38
ENTITY_IS_ATAK_INDEX=39
ENTITY_IS_UNKNOWN_INDEX=40

ENTITY_IS_ACQUISIED_INDEX=41

ENTITY_IS_PO_ENTITY_INDEX=42

ENTITY_IS_ENGAGE_COMMANDED_TARGET_ENTITY_INDEX=43
ENTITY_IS_COMMANDER_INDEX=44

ENTITY_DAMAGE_INDEX=45

ENTITY_IS_ENTITY_IN_DIVE_RANGE_WRT_LASER_GUIDED_MISSILE_INDEX=46
ENTITY_IS_ENTITY_IN_DIVE_RANGE_WRT_ACTIVE_RADAR_GUIDED_MISSILE_INDEX=47
ENTITY_IS_ENTITY_IN_DIVE_RANGE_WRT_IR_GUIDED_MISSILE_INDEX=48
ENTITY_IS_ENTITY_IN_DIVE_RANGE_WRT_SEMI_ACTIVE_RADAR_GUIDED_MISSILE_INDEX=49
ENTITY_IS_ENTITY_IN_DIVE_RANGE_WRT_PASSIVE_RADAR_GUIDED_MISSILE_INDEX=50
ENTITY_IS_ENTITY_IN_DIVE_RANGE_WRT_EO_GUIDED_MISSILE_INDEX=51
ENTITY_IS_ENTITY_IN_FIRING_RANGE_WRT_LASER_GUIDED_MISSILE_INDEX=52
ENTITY_IS_ENTITY_IN_FIRING_RANGE_WRT_ACTIVE_RADAR_GUIDED_MISSILE_INDEX=53
ENTITY_IS_ENTITY_IN_FIRING_RANGE_WRT_IR_GUIDED_MISSILE_INDEX=54
ENTITY_IS_ENTITY_IN_FIRING_RANGE_WRT_SEMI_ACTIVE_RADAR_GUIDED_MISSILE_INDEX=55
ENTITY_IS_ENTITY_IN_FIRING_RANGE_WRT_PASSIVE_RADAR_GUIDED_MISSILE_INDEX=56
ENTITY_IS_ENTITY_IN_FIRING_RANGE_WRT_EO_GUIDED_MISSILE_INDEX=57

#
ENTITY_STATE_SIZE=58
ENTITY_DISC_STATE_SIZE=854
#

MISSILE_ID_INDEX = 0
MISSILE_DISTANCE_INDEX = 1
MISSILE_INFO_INDEX = 2
TARGET_MISSILE_COUNT = 5




TEST = "TEST"
DEV = "DEV"
SIL = "SIL"
TGSPILOT = "TGSPILOT"
TGSGUNNER = "TGSGUNNER"
KGSGUNNER = "KGSGUNNER"
KGSPILOT = "KGSPILOT"
SASE = "SASE"
MINISIL = "MINISIL"

DEV_B = "DEV_B"
SIL_B = "SIL_B"
TGSPILOT_B = "TGSPILOT_B"
TGSGUNNER_B = "TGSGUNNER_B"
KGSGUNNER_B = "KGSGUNNER_B"
KGSPILOT_B = "KGSPILOT_B"
SASE_B = "SASE_B"
MINISIL_B = "MINISIL_B"

RESETPORT = {TEST: 6000, DEV: 6001, DEV_B: 6001, SIL: 6002, SIL_B: 6002, TGSPILOT: 6009, TGSPILOT_B: 6009, TGSGUNNER: 6004, TGSGUNNER_B: 6004,
             KGSGUNNER: 6005, KGSGUNNER_B: 6005, KGSPILOT: 6006, KGSPILOT_B: 6006, SASE: 6007, SASE_B: 6007, MINISIL: 6008, MINISIL_B: 6008}

COMMPORT =  {TEST: 5000, DEV: 5001, DEV_B: 5101, SIL: 5002, SIL_B: 5102, TGSPILOT: 5009, TGSPILOT_B: 5109, TGSGUNNER: 5004, TGSGUNNER_B: 5104,
             KGSGUNNER: 5005, KGSGUNNER_B: 5105, KGSPILOT: 5006, KGSPILOT_B: 5106, SASE: 5007, SASE_B: 5107, MINISIL: 5008, MINISIL_B: 5108}

