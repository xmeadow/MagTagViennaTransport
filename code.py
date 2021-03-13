import time
import terminalio
from adafruit_magtag.magtag import MagTag
 
# in seconds, we can refresh about 100 times on a battery
TIME_BETWEEN_REFRESHES = 60  # in seconds
# Set up data location and fields
desired_line = "42"
desired_station = "Antonigasse"
desired_richtung = "Schottentor"
DATA_SOURCE = "https://apps.static-access.net/ViennaTransport/monitor/?line=" + desired_line + "&station=" + desired_station +  "&towards=" + desired_richtung + "&countdown"
STATION = [0,'station']
LINIE = [0,'line']
RICHTUNG = [0,'towards']
COUNTDOWN1 = [0,'countdown',0]
COUNTDOWN2 = [0,'countdown',1]

 
def station_transform(val):
    if val == None:
        val = "Unavailable"
    return val

def line_transform(val2):
    if val2 == None:
        val2 = "Unavailable"
    return val2

def richtung_transform(val3):
    if val3 == None:
        val3 = "Unavailable"
    return val3

def countdown1_transform(val4):
    if val4 == None:
        val4 = "Unavailable"
    return val4

def countdown2_transform(val5):
    if val5 == None:
        val5 = "Unavailable"
    return val5
 
# Set up the MagTag with the JSON data parameters
magtag = MagTag(
    url=DATA_SOURCE,
    json_path=(STATION, LINIE, RICHTUNG, COUNTDOWN1, COUNTDOWN2)
)
 
magtag.add_text(
    text_font="/fonts/Impact-16.pcf",
    text_position=(10, 15),
    is_data=False
)
# Display heading text below with formatting above
magtag.set_text("Wiener Linien - Bring me home")

# LINE
magtag.add_text(
    text_font="/fonts/Impact-16.pcf",
    text_position=(40, 40),
    text_transform=line_transform
)


# STATION
magtag.add_text(
    text_font="/fonts/Impact-24.pcf",
    text_position=(10, 45),
    text_transform=station_transform
)

# RICHTUNG
magtag.add_text(
    text_font="/fonts/Impact-10.pcf",
    text_position=(40, 50),
    text_transform=richtung_transform
)


# COUNTDOWN1
magtag.add_text(
    text_font="/fonts/Impact-24.pcf",
    text_position=(160, 45),
    text_transform=countdown1_transform
)

# COUNTDOWN2
magtag.add_text(
    text_font="/fonts/Impact-24.pcf",
    text_position=(190, 45),
    text_transform=countdown2_transform
)

try:
    # Have the MagTag connect to the internet
    magtag.network.connect()
    # This statement gets the JSON data and displays it automagically
    value = magtag.fetch()
    print("Response is", value)
except (ValueError, RuntimeError) as e:
    print("Some error occured, retrying! -", e)
 
# wait 2 seconds for display to complete
time.sleep(2)
magtag.exit_and_deep_sleep(TIME_BETWEEN_REFRESHES)
