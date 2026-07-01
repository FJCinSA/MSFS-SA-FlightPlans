# Created: 30 June 2026 session.
# Scans all .pln files in C:\FlightPlans for ATCWaypoint entries whose id or
# ICAOIdent exactly matches a target navaid ident (BDV, JF, BL). Reports the
# file and leg number for each match; avoids false positives from airport
# codes that merely contain the ident as a substring (e.g. FABL).

import glob
import xml.etree.ElementTree as ET

TARGETS = {"BDV", "JF", "BL"}

for path in sorted(glob.glob(r"C:\FlightPlans\*.pln")):
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        print(f"{path}: PARSE ERROR ({e})")
        continue

    root = tree.getroot()
    waypoints = root.findall(".//ATCWaypoint")

    for leg_num, wp in enumerate(waypoints, start=1):
        wp_id = wp.get("id")
        icao_ident_el = wp.find("./ICAO/ICAOIdent")
        icao_ident = icao_ident_el.text.strip() if icao_ident_el is not None and icao_ident_el.text else None

        hits = []
        if wp_id in TARGETS:
            hits.append(f"id='{wp_id}'")
        if icao_ident in TARGETS and icao_ident != wp_id:
            hits.append(f"ICAOIdent='{icao_ident}'")

        if hits:
            wp_type_el = wp.find("./ATCWaypointType")
            wp_type = wp_type_el.text if wp_type_el is not None else "?"
            print(f"{path} | leg {leg_num}/{len(waypoints)} | {', '.join(hits)} | type={wp_type}")
