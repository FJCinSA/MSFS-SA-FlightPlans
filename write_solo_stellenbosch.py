# SOLO LEGS: FAWB -> FATM -> FABW -> FAWC -> FASH
# Recreating real flight by Dr Francois Coetzee in ZS-NTP (1978 C172N)
# Solo flight. Low cloud base. Diverted Worcester. Flew Du Toitskloof under cloud.
# Afternoon, east to west through the pass. Summer.

leg1 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>STELL LEG1 FAWB to FATM - RAW NAV (ZS-NTP Recreation)</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>7500</CruisingAlt>
        <DepartureID>FAWB</DepartureID>
        <DepartureLLA>S25* 39' 6.00",E28* 13' 26.00",+4268.00</DepartureLLA>
        <DestinationID>FATM</DestinationID>
        <DestinationLLA>S29* 1' 39.00",E26* 9' 0.00",+4547.00</DestinationLLA>
        <Descr>Wonderboom to New Tempe via WB NDB / PSV VOR-DME / BLV VORTAC</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Wonderboom</DepartureName>
        <DestinationName>New Tempe Bloemfontein</DestinationName>
        <ATCWaypoint id="FAWB">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 39' 6.00",E28* 13' 26.00",+4268.00</WorldPosition>
            <ICAO><ICAOIdent>FAWB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="WB">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S25* 39' 0.00",E28* 13' 0.00",+4268.00</WorldPosition>
            <ICAO><ICAOIdent>WB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="PSV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S26* 43' 0.00",E27* 6' 0.00",+4593.00</WorldPosition>
            <ICAO><ICAOIdent>PSV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="BLV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S29* 6' 1.80",E26* 18' 2.52",+4416.00</WorldPosition>
            <ICAO><ICAOIdent>BLV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FATM">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S29* 1' 39.00",E26* 9' 0.00",+4547.00</WorldPosition>
            <ICAO><ICAOIdent>FATM</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

leg2 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>STELL LEG2 FATM to FABW - RAW NAV (ZS-NTP Recreation)</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>7500</CruisingAlt>
        <DepartureID>FATM</DepartureID>
        <DepartureLLA>S29* 1' 39.00",E26* 9' 0.00",+4547.00</DepartureLLA>
        <DestinationID>FABW</DestinationID>
        <DestinationLLA>S32* 20' 39.00",E22* 53' 34.00",+2887.00</DestinationLLA>
        <Descr>New Tempe to Beaufort West via BLV VORTAC / VWV VOR / SWV VOR</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>New Tempe Bloemfontein</DepartureName>
        <DestinationName>Beaufort West</DestinationName>
        <ATCWaypoint id="FATM">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S29* 1' 39.00",E26* 9' 0.00",+4547.00</WorldPosition>
            <ICAO><ICAOIdent>FATM</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="BLV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S29* 6' 1.80",E26* 18' 2.52",+4416.00</WorldPosition>
            <ICAO><ICAOIdent>BLV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="VWV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S31* 37' 0.00",E23* 9' 0.00",+4000.00</WorldPosition>
            <ICAO><ICAOIdent>VWV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FABW">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S32* 20' 39.00",E22* 53' 34.00",+2887.00</WorldPosition>
            <ICAO><ICAOIdent>FABW</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

leg3 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>STELL LEG3 FABW to FAWC - RAW NAV (ZS-NTP Recreation)</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>7500</CruisingAlt>
        <DepartureID>FABW</DepartureID>
        <DepartureLLA>S32* 20' 39.00",E22* 53' 34.00",+2887.00</DepartureLLA>
        <DestinationID>FAWC</DestinationID>
        <DestinationLLA>S33* 39' 47.00",E19* 24' 55.00",+673.00</DestinationLLA>
        <Descr>Beaufort West to Worcester via SWV VOR / GGV VOR-DME / Hex River Valley</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Beaufort West</DepartureName>
        <DestinationName>Worcester</DestinationName>
        <ATCWaypoint id="FABW">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S32* 20' 39.00",E22* 53' 34.00",+2887.00</WorldPosition>
            <ICAO><ICAOIdent>FABW</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="SWV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S33* 55' 0.00",E20* 26' 0.00",+1000.00</WorldPosition>
            <ICAO><ICAOIdent>SWV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="HEXRIVER">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S33* 30' 0.00",E19* 37' 0.00",+1500.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="FAWC">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S33* 39' 47.00",E19* 24' 55.00",+673.00</WorldPosition>
            <ICAO><ICAOIdent>FAWC</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

leg4 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>STELL LEG4 FAWC to FASH - RAW NAV Du Toitskloof (ZS-NTP Recreation)</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>2500</CruisingAlt>
        <DepartureID>FAWC</DepartureID>
        <DepartureLLA>S33* 39' 47.00",E19* 24' 55.00",+673.00</DepartureLLA>
        <DestinationID>FASH</DestinationID>
        <DestinationLLA>S33* 58' 47.00",E18* 49' 11.00",+295.00</DestinationLLA>
        <Descr>Worcester to Stellenbosch via Du Toitskloof Pass - LOW LEVEL 500ft AGL - follow N1</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Worcester</DepartureName>
        <DestinationName>Stellenbosch</DestinationName>
        <ATCWaypoint id="FAWC">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S33* 39' 47.00",E19* 24' 55.00",+673.00</WorldPosition>
            <ICAO><ICAOIdent>FAWC</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="DUTOIT_EAST">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S33* 43' 0.00",E19* 11' 0.00",+1200.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="DUTOIT_PASS">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S33* 46' 0.00",E19* 4' 0.00",+1400.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="DUTOIT_WEST">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S33* 50' 0.00",E18* 58' 0.00",+800.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="PAARL">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S33* 44' 0.00",E18* 58' 0.00",+500.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="FASH">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S33* 58' 47.00",E18* 49' 11.00",+295.00</WorldPosition>
            <ICAO><ICAOIdent>FASH</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

files = {
    r"C:\FlightPlans\STELL_LEG1_FAWB_FATM.pln": leg1,
    r"C:\FlightPlans\STELL_LEG2_FATM_FABW.pln": leg2,
    r"C:\FlightPlans\STELL_LEG3_FABW_FAWC.pln": leg3,
    r"C:\FlightPlans\STELL_LEG4_FAWC_FASH.pln": leg4,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path}")

print("All done.")