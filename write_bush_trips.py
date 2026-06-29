# Bush Trip RAW NAV Editions
# Orange River Run: FAWB -> FAUP -> FYND -> FYKT -> FAWB (4 legs)
# Namib Desert:    FYKT -> FYLZ -> FYSM (2 legs)
# Real SA AIP navaids, VOR/NDB waypoint types

# -----------------------------------------------------------------------
# ORANGE RIVER RUN — Leg 1: FAWB -> FAUP
# Wonderboom to Upington via WB NDB / KD NDB / VB NDB / UPV VOR-DME
# -----------------------------------------------------------------------
orm_leg1 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>ORM LEG1 FAWB to FAUP - RAW NAV Orange River Run</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>9500</CruisingAlt>
        <DepartureID>FAWB</DepartureID>
        <DepartureLLA>S25* 39' 14.00",E28* 13' 27.00",+4095.00</DepartureLLA>
        <DestinationID>FAUP</DestinationID>
        <DestinationLLA>S28* 23' 57.00",E21* 15' 37.00",+2791.00</DestinationLLA>
        <Descr>Wonderboom to Upington via WB NDB / KD NDB / VB NDB / UN NDB / UPV VOR-DME</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Wonderboom</DepartureName>
        <DestinationName>Upington</DestinationName>
        <ATCWaypoint id="FAWB">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 39' 14.00",E28* 13' 27.00",+4095.00</WorldPosition>
            <ICAO><ICAOIdent>FAWB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="WB">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S25* 39' 0.00",E28* 13' 0.00",+4095.00</WorldPosition>
            <ICAO><ICAOIdent>WB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="KD">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 52' 0.00",E26* 40' 0.00",+4200.00</WorldPosition>
            <ICAO><ICAOIdent>KD</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="VB">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 59' 0.00",E24* 44' 0.00",+3900.00</WorldPosition>
            <ICAO><ICAOIdent>VB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="UN">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S28* 23' 0.00",E21* 16' 0.00",+2800.00</WorldPosition>
            <ICAO><ICAOIdent>UN</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="UPV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S28* 24' 0.00",E21* 15' 0.00",+2800.00</WorldPosition>
            <ICAO><ICAOIdent>UPV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FAUP">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S28* 23' 57.00",E21* 15' 37.00",+2791.00</WorldPosition>
            <ICAO><ICAOIdent>FAUP</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

# -----------------------------------------------------------------------
# ORANGE RIVER RUN — Leg 2: FAUP -> FYND
# Upington to Noordoewer via UN NDB / Augrabies overfly / Orange River low level
# -----------------------------------------------------------------------
orm_leg2 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>ORM LEG2 FAUP to FYND - RAW NAV Orange River Run</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>4500</CruisingAlt>
        <DepartureID>FAUP</DepartureID>
        <DepartureLLA>S28* 23' 57.00",E21* 15' 37.00",+2791.00</DepartureLLA>
        <DestinationID>FYND</DestinationID>
        <DestinationLLA>S28* 42' 6.00",E17* 37' 28.00",+560.00</DestinationLLA>
        <Descr>Upington to Noordoewer via UN NDB / Augrabies Falls overfly / Orange River low level</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Upington</DepartureName>
        <DestinationName>Noordoewer</DestinationName>
        <ATCWaypoint id="FAUP">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S28* 23' 57.00",E21* 15' 37.00",+2791.00</WorldPosition>
            <ICAO><ICAOIdent>FAUP</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="UN">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S28* 23' 0.00",E21* 16' 0.00",+2800.00</WorldPosition>
            <ICAO><ICAOIdent>UN</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="AUGRABIES">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S28* 35' 37.00",E20* 20' 30.00",+2800.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="ORANGE_RVR">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S28* 40' 0.00",E19* 0' 0.00",+1500.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="FYND">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S28* 42' 6.00",E17* 37' 28.00",+560.00</WorldPosition>
            <ICAO><ICAOIdent>FYND</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

# -----------------------------------------------------------------------
# ORANGE RIVER RUN — Leg 3: FYND -> FYKT
# Noordoewer to Keetmanshoop via KP NDB
# -----------------------------------------------------------------------
orm_leg3 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>ORM LEG3 FYND to FYKT - RAW NAV Orange River Run</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>6500</CruisingAlt>
        <DepartureID>FYND</DepartureID>
        <DepartureLLA>S28* 42' 6.00",E17* 37' 28.00",+560.00</DepartureLLA>
        <DestinationID>FYKT</DestinationID>
        <DestinationLLA>S26* 32' 20.00",E18* 6' 42.00",+3506.00</DestinationLLA>
        <Descr>Noordoewer to Keetmanshoop via KP NDB - climb out of the river valley, track north</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Noordoewer</DepartureName>
        <DestinationName>Keetmanshoop</DestinationName>
        <ATCWaypoint id="FYND">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S28* 42' 6.00",E17* 37' 28.00",+560.00</WorldPosition>
            <ICAO><ICAOIdent>FYND</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="KP">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 32' 0.00",E18* 7' 0.00",+3500.00</WorldPosition>
            <ICAO><ICAOIdent>KP</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FYKT">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S26* 32' 20.00",E18* 6' 42.00",+3506.00</WorldPosition>
            <ICAO><ICAOIdent>FYKT</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

# -----------------------------------------------------------------------
# ORANGE RIVER RUN — Leg 4: FYKT -> FAWB
# Keetmanshoop to Wonderboom via KP NDB / VB NDB / KD NDB / WB NDB
# -----------------------------------------------------------------------
orm_leg4 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>ORM LEG4 FYKT to FAWB - RAW NAV Orange River Run</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>9500</CruisingAlt>
        <DepartureID>FYKT</DepartureID>
        <DepartureLLA>S26* 32' 20.00",E18* 6' 42.00",+3506.00</DepartureLLA>
        <DestinationID>FAWB</DestinationID>
        <DestinationLLA>S25* 39' 14.00",E28* 13' 27.00",+4095.00</DestinationLLA>
        <Descr>Keetmanshoop to Wonderboom via KP NDB / VB NDB / KD NDB / WB NDB - long return across the Karoo</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Keetmanshoop</DepartureName>
        <DestinationName>Wonderboom</DestinationName>
        <ATCWaypoint id="FYKT">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S26* 32' 20.00",E18* 6' 42.00",+3506.00</WorldPosition>
            <ICAO><ICAOIdent>FYKT</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="KP">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 32' 0.00",E18* 7' 0.00",+3500.00</WorldPosition>
            <ICAO><ICAOIdent>KP</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="VB">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 59' 0.00",E24* 44' 0.00",+3900.00</WorldPosition>
            <ICAO><ICAOIdent>VB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="KD">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 52' 0.00",E26* 40' 0.00",+4200.00</WorldPosition>
            <ICAO><ICAOIdent>KD</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="WB">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S25* 39' 0.00",E28* 13' 0.00",+4095.00</WorldPosition>
            <ICAO><ICAOIdent>WB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FAWB">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 39' 14.00",E28* 13' 27.00",+4095.00</WorldPosition>
            <ICAO><ICAOIdent>FAWB</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

# -----------------------------------------------------------------------
# NAMIB DESERT — Leg 1: FYKT -> FYLZ
# Keetmanshoop to Luderitz via KP NDB / LU NDB
# -----------------------------------------------------------------------
nam_leg1 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>NAM LEG1 FYKT to FYLZ - RAW NAV Namib Desert</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>9500</CruisingAlt>
        <DepartureID>FYKT</DepartureID>
        <DepartureLLA>S26* 32' 20.00",E18* 6' 42.00",+3506.00</DepartureLLA>
        <DestinationID>FYLZ</DestinationID>
        <DestinationLLA>S26* 41' 7.00",E15* 14' 44.00",+457.00</DestinationLLA>
        <Descr>Keetmanshoop to Luderitz via KP NDB / LU NDB - track west across Namib, descend to the coast</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Keetmanshoop</DepartureName>
        <DestinationName>Luderitz</DestinationName>
        <ATCWaypoint id="FYKT">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S26* 32' 20.00",E18* 6' 42.00",+3506.00</WorldPosition>
            <ICAO><ICAOIdent>FYKT</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="KP">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 32' 0.00",E18* 7' 0.00",+3500.00</WorldPosition>
            <ICAO><ICAOIdent>KP</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="LU">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 41' 0.00",E15* 14' 0.00",+460.00</WorldPosition>
            <ICAO><ICAOIdent>LU</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FYLZ">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S26* 41' 7.00",E15* 14' 44.00",+457.00</WorldPosition>
            <ICAO><ICAOIdent>FYLZ</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

# -----------------------------------------------------------------------
# NAMIB DESERT — Leg 2: FYLZ -> FYSM
# Luderitz to Swakopmund via LU NDB / Sossusvlei overfly / SW NDB
# -----------------------------------------------------------------------
nam_leg2 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>NAM LEG2 FYLZ to FYSM - RAW NAV Namib Desert</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>9500</CruisingAlt>
        <DepartureID>FYLZ</DepartureID>
        <DepartureLLA>S26* 41' 7.00",E15* 14' 44.00",+457.00</DepartureLLA>
        <DestinationID>FYSM</DestinationID>
        <DestinationLLA>S22* 39' 43.00",E14* 34' 7.00",+170.00</DestinationLLA>
        <Descr>Luderitz to Swakopmund via LU NDB / Sossusvlei overfly / coastal track / SW NDB</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Luderitz</DepartureName>
        <DestinationName>Swakopmund</DestinationName>
        <ATCWaypoint id="FYLZ">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S26* 41' 7.00",E15* 14' 44.00",+457.00</WorldPosition>
            <ICAO><ICAOIdent>FYLZ</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="LU">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S26* 41' 0.00",E15* 14' 0.00",+460.00</WorldPosition>
            <ICAO><ICAOIdent>LU</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="SOSSUSVLEI">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S24* 43' 39.00",E15* 20' 33.00",+9500.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="COAST_TRK">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S23* 30' 0.00",E14* 34' 0.00",+2000.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="SW">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S22* 40' 0.00",E14* 34' 0.00",+175.00</WorldPosition>
            <ICAO><ICAOIdent>SW</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FYSM">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S22* 39' 43.00",E14* 34' 7.00",+170.00</WorldPosition>
            <ICAO><ICAOIdent>FYSM</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

files = {
    r"C:\FlightPlans\BUSH_ORM_LEG1_FAWB_FAUP.pln": orm_leg1,
    r"C:\FlightPlans\BUSH_ORM_LEG2_FAUP_FYND.pln": orm_leg2,
    r"C:\FlightPlans\BUSH_ORM_LEG3_FYND_FYKT.pln": orm_leg3,
    r"C:\FlightPlans\BUSH_ORM_LEG4_FYKT_FAWB.pln": orm_leg4,
    r"C:\FlightPlans\BUSH_NAM_LEG1_FYKT_FYLZ.pln": nam_leg1,
    r"C:\FlightPlans\BUSH_NAM_LEG2_FYLZ_FYSM.pln": nam_leg2,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path}")

print("All done.")
