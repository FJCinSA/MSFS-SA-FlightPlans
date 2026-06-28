# SOLO LEGS: FAWB -> FAPN -> FAMM
# Recreating real flight by Dr Francois Coetzee in ZS-NTP (1978 C172N)
# James Caroto-Coetzee aboard - his first ever flight
# Comms failure into Pilanesberg - relayed via Joburg Information
# James handled cellphone comms, Francois flew the aircraft

leg1 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>SOLO LEG1 FAWB to FAPN - RAW NAV (ZS-NTP Recreation)</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>6500</CruisingAlt>
        <DepartureID>FAWB</DepartureID>
        <DepartureLLA>S25* 39' 6.00",E28* 13' 26.00",+4268.00</DepartureLLA>
        <DestinationID>FAPN</DestinationID>
        <DestinationLLA>S25* 20' 7.74",E27* 10' 17.88",+3412.00</DestinationLLA>
        <Descr>Wonderboom to Pilanesberg via WB NDB / PSV VOR-DME / PLB NDB / PNV VOR-DME</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Wonderboom</DepartureName>
        <DestinationName>Pilanesberg</DestinationName>
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
        <ATCWaypoint id="HARTBEESPOORT">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S25* 44' 0.00",E27* 52' 0.00",+3900.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="PLB">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S25* 22' 0.00",E27* 9' 0.00",+3412.00</WorldPosition>
            <ICAO><ICAOIdent>PLB</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="PNV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S25* 20' 7.74",E27* 10' 17.88",+3412.00</WorldPosition>
            <ICAO><ICAOIdent>PNV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FAPN">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 20' 7.74",E27* 10' 17.88",+3412.00</WorldPosition>
            <ICAO><ICAOIdent>FAPN</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

leg2 = """<?xml version="1.0" encoding="UTF-8"?>
<SimBase.Document Type="AceXML" version="1,0">
    <Descr>AceXML Document</Descr>
    <FlightPlan.FlightPlan>
        <Title>SOLO LEG2 FAPN to FAMM - RAW NAV (ZS-NTP Recreation)</Title>
        <FPType>VFR</FPType>
        <RouteType>LowAlt</RouteType>
        <CruisingAlt>6500</CruisingAlt>
        <DepartureID>FAPN</DepartureID>
        <DepartureLLA>S25* 20' 7.74",E27* 10' 17.88",+3412.00</DepartureLLA>
        <DestinationID>FAMM</DestinationID>
        <DestinationLLA>S25* 47' 53.00",E25* 32' 56.00",+4088.00</DestinationLLA>
        <Descr>Pilanesberg to Mafikeng via PNV VOR-DME / MMV VOR-DME / MH NDB</Descr>
        <DeparturePosition>1</DeparturePosition>
        <DepartureName>Pilanesberg</DepartureName>
        <DestinationName>Mafikeng</DestinationName>
        <ATCWaypoint id="FAPN">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 20' 7.74",E27* 10' 17.88",+3412.00</WorldPosition>
            <ICAO><ICAOIdent>FAPN</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="PNV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S25* 20' 7.74",E27* 10' 17.88",+3412.00</WorldPosition>
            <ICAO><ICAOIdent>PNV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="ZEERUST">
            <ATCWaypointType>User</ATCWaypointType>
            <WorldPosition>S25* 32' 0.00",E26* 4' 0.00",+4200.00</WorldPosition>
        </ATCWaypoint>
        <ATCWaypoint id="MMV">
            <ATCWaypointType>VOR</ATCWaypointType>
            <WorldPosition>S25* 47' 53.00",E25* 32' 56.00",+4088.00</WorldPosition>
            <ICAO><ICAOIdent>MMV</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="MH">
            <ATCWaypointType>NDB</ATCWaypointType>
            <WorldPosition>S25* 47' 53.00",E25* 32' 56.00",+4088.00</WorldPosition>
            <ICAO><ICAOIdent>MH</ICAOIdent></ICAO>
        </ATCWaypoint>
        <ATCWaypoint id="FAMM">
            <ATCWaypointType>Airport</ATCWaypointType>
            <WorldPosition>S25* 47' 53.00",E25* 32' 56.00",+4088.00</WorldPosition>
            <ICAO><ICAOIdent>FAMM</ICAOIdent></ICAO>
        </ATCWaypoint>
    </FlightPlan.FlightPlan>
</SimBase.Document>"""

files = {
    r"C:\FlightPlans\SOLO_FAWB_FAPN.pln": leg1,
    r"C:\FlightPlans\SOLO_FAPN_FAMM.pln": leg2,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path}")

print("All done.")