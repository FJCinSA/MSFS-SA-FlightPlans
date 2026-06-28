import os

gps_3a = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>LEG3a FACB to FABL - GPS Edition</Title>
        <FPType>IFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>7500</CruisingAlt>
        <DepartureID>FACB</DepartureID>
        <DepartureLLA>S30* 20' 25.20",E25* 35' 30.00",+4757.00</DepartureLLA>
        <DestinationID>FABL</DestinationID>
        <DestinationLLA>S29* 5' 47.00",E26* 18' 7.00",+4458.00</DestinationLLA>
        <Descr>Colesberg to Bloemfontein - GPS Direct</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Colesberg</DepartureName>
        <DestinationName>Bloemfontein</DestinationName>
        <ATCWaypoint id="FACB">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S30* 20' 25.20",E25* 35' 30.00",+4757.00</WorldPosition>
            <ICAO><ICAOIdent>FACB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FABL">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S29* 5' 47.00",E26* 18' 7.00",+4458.00</WorldPosition>
            <ICAO><ICAOIdent>FABL</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

raw_3a = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>LEG3a FACB to FABL - RAW NAV Edition</Title>
        <FPType>IFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>7500</CruilingAlt>
        <DepartureID>FACB</DepartureID>
        <DepartureLLA>S30* 20' 25.20",E25* 35' 30.00",+4757.00</DepartureLLA>
        <DestinationID>FABL</DestinationID>
        <DestinationLLA>S29* 5' 47.00",E26* 18' 7.00",+4458.00</DestinationLLA>
        <Descr>Colesberg to Bloemfontein via BDV VOR / DR / BL NDB / BLV VORTAC</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Colesberg</DepartureName>
        <DestinationName>Bloemfontein</DestinationName>
        <ATCWaypoint id="FACB">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S30* 20' 25.20",E25* 35' 30.00",+4757.00</WorldPosition>
            <ICAO><ICAOIdent>FACB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="BDV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S30* 57' 54.00",E26* 19' 21.72",+4715.00</WorldPosition>
            <ICAO><ICAOIdent>BDV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="TROMPSBURG">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S30* 0' 0.00",E25* 46' 0.00",+4800.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="SPRINGFONTEIN">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S29* 40' 0.00",E25* 44' 0.00",+4700.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="BL">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S29* 6' 1.80",E26* 18' 2.52",+4416.00</WorldPosition>
            <ICAO><ICAOIdent>BL</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="BLV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S29* 6' 1.80",E26* 18' 2.52",+4416.00</WorldPosition>
            <ICAO><ICAOIdent>BLV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FABL">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S29* 5' 47.00",E26* 18' 7.00",+4458.00</WorldPosition>
            <ICAO><ICAOIdent>FABL</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

gps_3b = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>LEG3b FABL to FALA - GPS Edition</Title>
        <FPType>IFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>7500</CruisingAlt>
        <DepartureID>FABL</DepartureID>
        <DepartureLLA>S29* 5' 47.00",E26* 18' 7.00",+4458.00</DepartureLLA>
        <DestinationID>FALA</DestinationID>
        <DestinationLLA>S25* 56' 19.00",E27* 55' 34.00",+4517.00</DestinationLLA>
        <Descr>Bloemfontein to Lanseria - GPS Direct</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Bloemfontein</DepartureName>
        <DestinationName>Lanseria</DestinationName>
        <ATCWaypoint id="FABL">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S29* 5' 47.00",E26* 18' 7.00",+4458.00</WorldPosition>
            <ICAO><ICAOIdent>FABL</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FALA">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 56' 19.00",E27* 55' 34.00",+4517.00</WorldPosition>
            <ICAO><ICAOIdent>FALA</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

raw_3b = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>LEG3b FABL to FALA - RAW NAV Edition</Title>
        <FPType>IFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>7500</CruisingAlt>
        <DepartureID>FABL</DepartureID>
        <DepartureLLA>S29* 5' 47.00",E26* 18' 7.00",+4458.00</DepartureLLA>
        <DestinationID>FALA</DestinationID>
        <DestinationLLA>S25* 56' 19.00",E27* 55' 34.00",+4517.00</DestinationLLA>
        <Descr>Bloemfontein to Lanseria via BLV VORTAC / KS NDB / Potchefstroom / LIV VOR-DME</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Bloemfontein</DepartureName>
        <DestinationName>Lanseria</DestinationName>
        <ATCWaypoint id="FABL">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S29* 5' 47.00",E26* 18' 7.00",+4458.00</WorldPosition>
            <ICAO><ICAOIdent>FABL</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="BLV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S29* 6' 1.80",E26* 18' 2.52",+4416.00</WorldPosition>
            <ICAO><ICAOIdent>BLV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="BRANDFORT">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S28* 42' 0.00",E26* 27' 0.00",+4500.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="KS">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S27* 40' 44.04",E27* 17' 13.96",+4500.00</WorldPosition>
            <ICAO><ICAOIdent>KS</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="POTCHEFSTROOM">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S26* 40' 0.00",E27* 5' 0.00",+4700.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="KRUGERSDORP">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S26* 6' 0.00",E27* 46' 0.00",+5200.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="LIV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S25* 56' 56.04",E27* 54' 49.16",+4570.00</WorldPosition>
            <ICAO><ICAOIdent>LIV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FALA">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 56' 19.00",E27* 55' 34.00",+4517.00</WorldPosition>
            <ICAO><ICAOIdent>FALA</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

files = {
    r"C:\FlightPlans\LEG3a_FACB_FABL_GPS.pln": gps_3a,
    r"C:\FlightPlans\LEG3a_FACB_FABL_RAW.pln": raw_3a,
    r"C:\FlightPlans\LEG3b_FABL_FALA_GPS.pln": gps_3b,
    r"C:\FlightPlans\LEG3b_FABL_FALA_RAW.pln": raw_3b,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path}")

print("All done.")
