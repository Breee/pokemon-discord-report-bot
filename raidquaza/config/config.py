from utility.enums import DataSource

# Directory where the log file of the bot shall be stored
LOG_PATH = '.'

"""
Discord Section.
"""
# The Token of your botuser.
BOT_TOKEN = 'NDExNTQzMTExNDA0MDkzNDQx.XQThpQ.-UAkXrHThf3SIHBTkT2ynf0xG0g'
# Discord Status
PLAYING = 'RaidquazaTesting'
# Command prefix
PREFIX = '!'

"""
Poll Section.
"""
# If you want to use the poll COG, set this to true
POLL_ENABLED = True
# The host of the DB in which we store polls
POLL_DB_HOST = 'localhost'
# The user of the DB
POLL_DB_USER = 'pollman'
# The password of user POLL_DB_USER
POLL_DB_PASSWORD = 'bestpw'
# The port of the DB-server
POLL_DB_PORT = 3307
# The name of the DB in which we store polls
POLL_DB_NAME = 'polldb'
# The dialect of the database-server
POLL_DB_DIALECT = 'mysql'
# The driver of the database-server
POLL_DB_DRIVER = 'mysqlconnector'

"""
Search section.

Here we define the settings for the Search.
"""
# If you want to use the search COG, set this to True.
SEARCH_ENABLED = True

"""
Choosing the datasource for gyms / stops. 

The datasource is either DataSource.DATABASE or DataSource.CSV
If DataSource.DATABASE is chosen, we pull the gyms and stops from a database.
If DataSource.CSV is chosen, we pull the gyms and stops from a csv file, an example can be found in 
'data/gyms_stops.csv'
"""
SEARCH_DATASOURCE = DataSource.DATABASE

# The csv file we pull data from, example in 'data/gyms_stops.csv'. Leave this empty if you do not need it.
SEARCH_CSV_FILE = 'data/gyms_stops.csv'
SEARCH_CSV_DELIMITER = ','

# If you have chosen DataSource.DATABASE, you have to define from which database you pull data.
# The host of the DB
SEARCH_DB_HOST = 'localhost'
# The name of the database
SEARCH_DB_NAME = 'monocledb'
# The user of the database
SEARCH_DB_USER = 'monocleuser'
# The password to connect with SEARCH_DB_USER.
SEARCH_DB_PASSWORD = 'test123'
# The port of the database-server
SEARCH_DB_PORT = 3309
# The dialect of the database-server
SEARCH_DB_DIALECT = 'mysql'
# The driver of the database-server
SEARCH_DB_DRIVER = 'mysqlconnector'

# The table in database SEARCH_DB_NAME, which contains pokestops
SEARCH_POKESTOP_TABLE = 'pokestops'
# The table in database SEARCH_DB_NAME, which contains gyms
SEARCH_GYM_TABLE = 'forts'

"""
Choosing the datasource for portals. 

The datasource is either DataSource.DATABASE or DataSource.CSV
If DataSource.DATABASE is chosen, we pull the gyms and stops from a database.
If DataSource.CSV is chosen, we pull the from a csv file SEARCH_CSV_FILE an example can be found in 
'data/gyms_stops.csv'
"""
SEARCH_USE_PORTALS = True
# if you want CSV, use SEARCH_CSV_FILE
SEARCH_PORTALS_DATASOURCE = DataSource.DATABASE

# If you have chosen DataSource.DATABASE, you have to define from which database you pull data.
# The host of the DB
SEARCH_PORTALS_DB_HOST = 'localhost'
# The name of the database
SEARCH_PORTALS_DB_NAME = 'monocledb'
# The user of the database
SEARCH_PORTALS_DB_USER = 'monocleuser'
# The password to connect with SEARCH_DB_USER.
SEARCH_PORTALS_DB_PASSWORD = 'test123'
# The port of the database-server
SEARCH_PORTALS_DB_PORT = 3309
# The dialect of the database-server
SEARCH_PORTALS_DB_DIALECT = 'mysql'
# The driver of the database-server
SEARCH_PORTALS_DB_DRIVER = 'mysqlconnector'

# The table in database SEARCH_PORTALS_DB_NAME, which contains portals
SEARCH_PORTALS_DB_TABLE = 'ingress_portals'

"""
Geofencing.

When the amount of pokestops/gyms if big and you cover different cities / regions, you might want to restrict the 
search space for different channels.
We define a mapping DISCORD_CHANNEL -> GEOFENCE, if you then use the search functionality in a specified 
DISCORD_CHANNEL, the search space is restricted to point of interests which are in the according GEOFENCE.
"""
# Set to true if you want to use geofencing.
SEARCH_USE_GEOFENCES = False
# DISCORD_CHANNEL -> GEOFENCE
SEARCH_CHANNELS_TO_GEOFENCES = {}
