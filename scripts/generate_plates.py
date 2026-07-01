#!/usr/bin/env python3
# Created: 30 June 2026 session.
"""
Generate approach/joining plates for:
  FACT - Cape Town Intl    - ILS RWY 01
  FABW - Beaufort West     - VFR Joining Procedure (no published IAP)
  FAGG - George             - ILS RWY 11
  FAOH - Oudtshoorn         - VFR Joining Procedure (no published IAP)

Run from C:\\FlightPlans :
    python generate_plates.py

Output -> C:\\FlightPlans\\Approaches\\
Matches dark Jeppesen-style plates already in the repo (FABL, FALA, FAWB).
"""

import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Approaches")
os.makedirs(OUT_DIR, exist_ok=True)

CSS = """
:root{
  --bg:#0a1018; --panel:#101926; --line:#2a3a4d; --text:#dce6ef;
  --amber:#e8b84b; --cyan:#5fd0d8; --red:#d65a5a; --dim:#7d8a99;
}
*{box-sizing:border-box;}
body{
  background:var(--bg); color:var(--text);
  font-family:'Consolas','Courier New',monospace;
  margin:0; padding:20px;
}
.plate{
  max-width:980px; margin:0 auto; background:var(--panel);
  border:1px solid var(--line); border-radius:4px; padding:18px 24px;
}
.header{
  display:flex; justify-content:space-between; align-items:baseline;
  border-bottom:2px solid var(--amber); padding-bottom:8px; margin-bottom:14px;
}
.header h1{font-size:20px; color:var(--amber); margin:0; letter-spacing:1px;}
.header .sub{font-size:13px; color:var(--cyan);}
.header .meta{text-align:right; font-size:11px; color:var(--dim); line-height:1.4;}
.row{display:flex; gap:16px; flex-wrap:wrap; margin-bottom:14px;}
.box{
  flex:1; min-width:220px; border:1px solid var(--line); border-radius:3px;
  padding:10px 12px; background:#0d141f;
}
.box h2{font-size:12px; color:var(--cyan); margin:0 0 6px 0; text-transform:uppercase; letter-spacing:1px;}
.box p, .box li{font-size:13px; margin:2px 0; line-height:1.5;}
.freqline{display:flex; justify-content:space-between; border-bottom:1px dotted var(--line); padding:3px 0;}
.freqline span:first-child{color:var(--dim);}
.freqline span:last-child{color:var(--amber); font-weight:bold;}
.profile{
  border:1px solid var(--line); border-radius:3px; padding:14px;
  background:#0d141f; margin-bottom:14px;
}
.profile svg{width:100%; height:auto; display:block;}
.minima{
  border:2px solid var(--amber); border-radius:3px; padding:10px 14px;
  background:#1a1408; margin-bottom:14px;
}
.minima h2{color:var(--amber); font-size:13px; margin:0 0 8px 0; letter-spacing:1px;}
table{width:100%; border-collapse:collapse; font-size:13px;}
table th, table td{border:1px solid var(--line); padding:5px 8px; text-align:center;}
table th{color:var(--cyan); background:#0d141f;}
.warning{
  border:1px solid var(--red); border-radius:3px; padding:10px 14px;
  background:#1a0d0d; color:#f0b8b8; font-size:13px; margin-bottom:14px;
}
.warning b{color:var(--red);}
.missed{font-size:13px; line-height:1.6;}
.footer{
  border-top:1px solid var(--line); margin-top:10px; padding-top:8px;
  font-size:11px; color:var(--dim); display:flex; justify-content:space-between;
}
.disclaimer{
  font-size:11px; color:var(--dim); font-style:italic; margin-top:10px;
  border-top:1px dashed var(--line); padding-top:8px;
}
"""

def page(title, body_html, footer_left, footer_right):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<div class="plate">
{body_html}
<div class="footer"><span>{footer_left}</span><span>{footer_right}</span></div>
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# FACT - Cape Town International - ILS RWY 01
# ---------------------------------------------------------------------------
fact_body = """
<div class="header">
  <div>
    <h1>FACT — CAPE TOWN INTL</h1>
    <div class="sub">ILS RWY 01</div>
  </div>
  <div class="meta">
    ELEV 151 FT &nbsp;|&nbsp; CTR<br>
    CoetzeeMed Flight Ops — FJCinSA
  </div>
</div>

<div class="row">
  <div class="box">
    <h2>Communications</h2>
    <div class="freqline"><span>ATIS</span><span>127.00</span></div>
    <div class="freqline"><span>Approach</span><span>119.70</span></div>
    <div class="freqline"><span>Director</span><span>124.35</span></div>
    <div class="freqline"><span>Tower</span><span>118.10</span></div>
    <div class="freqline"><span>Ground</span><span>121.90</span></div>
  </div>
  <div class="box">
    <h2>Navaids</h2>
    <div class="freqline"><span>ILS CTI (RWY 01)</span><span>110.30</span></div>
    <div class="freqline"><span>CTV VOR/DME</span><span>115.70</span></div>
    <div class="freqline"><span>RWY 01 Heading</span><span>010° MAG</span></div>
    <div class="freqline"><span>RWY 01 THR ELEV</span><span>144 FT</span></div>
  </div>
  <div class="box">
    <h2>Runway</h2>
    <p>RWY 01/19 — 10,502 x 200 FT, hard surface.</p>
    <p>Secondary RWY 16/34 — 5,581 x 151 FT.</p>
    <p>Prevailing wind NW in winter favours RWY 01; strong SE "Cape Doctor" in summer favours RWY 19.</p>
  </div>
</div>

<div class="profile">
  <svg viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg">
    <line x1="40" y1="160" x2="860" y2="160" stroke="#2a3a4d" stroke-width="2"/>
    <line x1="700" y1="160" x2="860" y2="40" stroke="#5fd0d8" stroke-width="2"/>
    <text x="430" y="180" fill="#7d8a99" font-size="12">FINAL APPROACH TRACK 010°(M) — GLIDE PATH 3.0°</text>
    <text x="700" y="35" fill="#e8b84b" font-size="12">IF / GS INTERCEPT 3000FT</text>
    <circle cx="860" cy="40" r="4" fill="#e8b84b"/>
    <line x1="780" y1="160" x2="780" y2="60" stroke="#5fd0d8" stroke-dasharray="4,4"/>
    <text x="760" y="55" fill="#dce6ef" font-size="11">OM / 4 DME CTI</text>
    <polygon points="700,160 692,148 708,148" fill="#dce6ef"/>
    <text x="40" y="155" fill="#dce6ef" font-size="11">RWY 01 THR 144FT</text>
  </svg>
</div>

<div class="minima">
  <h2>MINIMA — ILS RWY 01</h2>
  <table>
    <tr><th>CAT</th><th>DA(H)</th><th>RVR/VIS</th></tr>
    <tr><td>A/B/C</td><td>~544 FT (400 FT AGL)</td><td>800 M</td></tr>
    <tr><td>D</td><td>~544 FT (400 FT AGL)</td><td>1000 M</td></tr>
  </table>
</div>

<div class="missed">
  <b>MISSED APPROACH:</b> Climb straight ahead on RWY heading to 1500 FT, then as directed by ATC /
  comply with published lost-comms routing (KODES 1A north / TETAN 1C east / OKTED 1A south-east).
</div>

<div class="warning">
  <b>NOTE:</b> Cape Town sits in a TMA with multiple parallel-style traffic flows and the "Cape Doctor"
  SE wind regularly forces a runway change to 19. Confirm active runway and ATIS before planning approach.
</div>

<div class="disclaimer">
  Simplified plate for MSFS 2024 simulator use — built from public AIP/SkyVector data, June 2026.
  Minima are representative, not for real-world navigation. Verify against current AIP/Jeppesen before any real-world use.
</div>
"""

# ---------------------------------------------------------------------------
# FABW - Beaufort West - VFR Joining Procedure (no published IAP)
# ---------------------------------------------------------------------------
fabw_body = """
<div class="header">
  <div>
    <h1>FABW — BEAUFORT WEST (KAROO GATEWAY)</h1>
    <div class="sub">VFR JOINING PROCEDURE — NO PUBLISHED IAP</div>
  </div>
  <div class="meta">
    ELEV 2929 FT &nbsp;|&nbsp; UNCONTROLLED<br>
    CoetzeeMed Flight Ops — FJCinSA
  </div>
</div>

<div class="row">
  <div class="box">
    <h2>Communications</h2>
    <div class="freqline"><span>CTAF / Flight Info</span><span>125.60</span></div>
    <p style="color:#7d8a99;font-size:11px;">No control tower. Make blind broadcasts on CTAF — position, intentions, runway in use.</p>
  </div>
  <div class="box">
    <h2>Runway</h2>
    <p>RWY 08/26, unpaved/gravel surface typical for Karoo strips — confirm in-sim scenery surface.</p>
    <p>Field elevation 2929 FT — high veld, density altitude matters on hot Karoo afternoons.</p>
  </div>
  <div class="box">
    <h2>Field notes</h2>
    <p>Fuel stop on the FACT→FALA cross-country (Leg 1, GPS &amp; RAW NAV editions).</p>
    <p>No NDB, VOR, or ILS. Field is below controlled airspace — VFR-only operation.</p>
  </div>
</div>

<div class="profile">
  <svg viewBox="0 0 900 160" xmlns="http://www.w3.org/2000/svg">
    <line x1="40" y1="120" x2="860" y2="120" stroke="#2a3a4d" stroke-width="2"/>
    <text x="350" y="140" fill="#7d8a99" font-size="12">JOIN OVERHEAD 1000FT AGL ABOVE CIRCUIT TO DETERMINE ACTIVE RWY</text>
    <line x1="700" y1="120" x2="780" y2="60" stroke="#5fd0d8" stroke-dasharray="4,4"/>
    <text x="700" y="50" fill="#dce6ef" font-size="11">OVERHEAD JOIN — CIRCUIT ALT 4929FT (2000FT AGL)</text>
    <polygon points="700,120 692,108 708,108" fill="#dce6ef"/>
    <text x="40" y="115" fill="#dce6ef" font-size="11">RWY 08/26, ELEV 2929FT</text>
  </svg>
</div>

<div class="minima">
  <h2>JOINING PROCEDURE</h2>
  <p>1. Make blind broadcast 10 NM out — callsign, position, intentions.</p>
  <p>2. Join overhead aerodrome at 1000 FT above circuit altitude to identify active runway / windsock.</p>
  <p>3. Descend on the dead side, join downwind for active runway.</p>
  <p>4. Continue broadcasts through circuit — base, final, clear of runway.</p>
</div>

<div class="warning">
  <b>NOTE:</b> Mountainous high-veld terrain surrounds the field. Watch for thermal turbulence and
  density altitude on warm-weather ops — this matches the Karoo conditions flown on the personal-history
  ZS-NTP legs (FATM→FABW night sector).
</div>

<div class="disclaimer">
  Simplified plate for MSFS 2024 simulator use — built from public airport data, June 2026.
  FABW has no published instrument approach; this is a VFR joining reference, not an IAP.
</div>
"""

# ---------------------------------------------------------------------------
# FAGG - George - ILS RWY 11
# ---------------------------------------------------------------------------
fagg_body = """
<div class="header">
  <div>
    <h1>FAGG — GEORGE</h1>
    <div class="sub">ILS RWY 11</div>
  </div>
  <div class="meta">
    ELEV 648 FT &nbsp;|&nbsp; CTR<br>
    CoetzeeMed Flight Ops — FJCinSA
  </div>
</div>

<div class="row">
  <div class="box">
    <h2>Communications</h2>
    <div class="freqline"><span>TWR/APP (combined)</span><span>118.90</span></div>
    <div class="freqline"><span>Apron/Radio Control</span><span>122.65</span></div>
  </div>
  <div class="box">
    <h2>Navaids</h2>
    <div class="freqline"><span>GRV VOR/DME</span><span>116.60</span></div>
    <div class="freqline"><span>RWY 11 Heading</span><span>110° MAG</span></div>
    <div class="freqline"><span>Field elevation</span><span>648 FT</span></div>
  </div>
  <div class="box">
    <h2>Runway / terrain</h2>
    <p>RWY 11/29. High ground inland of the field — go-around on RWY 11 turns RIGHT to GRV; RWY 29 turns LEFT to GRV.</p>
    <p>Garden Route coastal terrain — expect orographic cloud and sea-fog (especially RWY 29 side).</p>
  </div>
</div>

<div class="profile">
  <svg viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg">
    <line x1="40" y1="160" x2="860" y2="160" stroke="#2a3a4d" stroke-width="2"/>
    <line x1="700" y1="160" x2="860" y2="40" stroke="#5fd0d8" stroke-width="2"/>
    <text x="380" y="180" fill="#7d8a99" font-size="12">FINAL APPROACH TRACK 110°(M) — GLIDE PATH 3.0°</text>
    <text x="660" y="35" fill="#e8b84b" font-size="12">INITIAL APCH ALT 5500FT — 20DME GRV</text>
    <circle cx="860" cy="40" r="4" fill="#e8b84b"/>
    <line x1="780" y1="160" x2="780" y2="60" stroke="#5fd0d8" stroke-dasharray="4,4"/>
    <text x="760" y="55" fill="#dce6ef" font-size="11">9 DME GRV</text>
    <polygon points="700,160 692,148 708,148" fill="#dce6ef"/>
    <text x="40" y="155" fill="#dce6ef" font-size="11">RWY 11 THR 648FT</text>
  </svg>
</div>

<div class="minima">
  <h2>MINIMA — ILS RWY 11 (CAT I)</h2>
  <table>
    <tr><th>CAT</th><th>DA(H)</th><th>RVR/VIS</th></tr>
    <tr><td>A/B/C/D</td><td>~898 FT (250 FT AGL)</td><td>800 M</td></tr>
  </table>
</div>

<div class="missed">
  <b>MISSED APPROACH (RWY 11):</b> Maintain RWY track, climb to 7000 FT; passing 6000 FT turn RIGHT
  direct to GRV for radar vectors. At 9 DME GRV, turn LEFT direct to GRV and hold if not radar vectored.
  <br><b>MISSED APPROACH (RWY 29):</b> Maintain RWY track, climb on R296 "GRV" to 6200 FT; at 9 DME GRV
  turn LEFT direct to GRV.
</div>

<div class="warning">
  <b>NOTE:</b> George is radar-vectored for the visual/ILS approach in normal ops — expect vectors rather
  than a full procedural pattern. Circling approach north of RWY 11/29 is not authorised.
</div>

<div class="disclaimer">
  Simplified plate for MSFS 2024 simulator use — built from public AIP/NOTAM data, June 2026.
  Minima are representative, not for real-world navigation. Verify against current AIP/Jeppesen before any real-world use.
</div>
"""

# ---------------------------------------------------------------------------
# FAOH - Oudtshoorn - VFR Joining Procedure (no published IAP)
# ---------------------------------------------------------------------------
faoh_body = """
<div class="header">
  <div>
    <h1>FAOH — OUDTSHOORN</h1>
    <div class="sub">VFR JOINING PROCEDURE — NO PUBLISHED IAP</div>
  </div>
  <div class="meta">
    ELEV 1063 FT &nbsp;|&nbsp; UNCONTROLLED<br>
    CoetzeeMed Flight Ops — FJCinSA
  </div>
</div>

<div class="row">
  <div class="box">
    <h2>Communications</h2>
    <div class="freqline"><span>CTAF</span><span>124.80</span></div>
    <div class="freqline"><span>George Approach (advisory)</span><span>118.90</span></div>
    <p style="color:#7d8a99;font-size:11px;">No control tower. Blind broadcasts on CTAF.</p>
  </div>
  <div class="box">
    <h2>Runway</h2>
    <p>RWY 04/22, 5,577 x 98 FT.</p>
    <p>Field elevation 1063 FT. Klein Karoo valley floor, ringed by the Swartberg and Outeniqua ranges.</p>
  </div>
  <div class="box">
    <h2>Field notes — Klein Karoo home ground</h2>
    <p>Oudtshoorn/George area — Francois's Klein Karoo roots. 48 km from George (FAGG), 47 km from Prince Albert (FAPC).</p>
    <p>No NDB, VOR, or ILS at the field.</p>
  </div>
</div>

<div class="profile">
  <svg viewBox="0 0 900 160" xmlns="http://www.w3.org/2000/svg">
    <line x1="40" y1="120" x2="860" y2="120" stroke="#2a3a4d" stroke-width="2"/>
    <text x="330" y="140" fill="#7d8a99" font-size="12">JOIN OVERHEAD 1000FT AGL ABOVE CIRCUIT TO DETERMINE ACTIVE RWY</text>
    <line x1="700" y1="120" x2="780" y2="60" stroke="#5fd0d8" stroke-dasharray="4,4"/>
    <text x="700" y="50" fill="#dce6ef" font-size="11">OVERHEAD JOIN — CIRCUIT ALT 2063FT (1000FT AGL)</text>
    <polygon points="700,120 692,108 708,108" fill="#dce6ef"/>
    <text x="40" y="115" fill="#dce6ef" font-size="11">RWY 04/22, ELEV 1063FT</text>
  </svg>
</div>

<div class="minima">
  <h2>JOINING PROCEDURE</h2>
  <p>1. Make blind broadcast 10 NM out — callsign, position, intentions, on CTAF 124.8.</p>
  <p>2. Join overhead aerodrome at 1000 FT above circuit altitude to identify active runway / windsock.</p>
  <p>3. Descend on the dead side, join downwind for active runway.</p>
  <p>4. Continue broadcasts through circuit — base, final, clear of runway.</p>
</div>

<div class="warning">
  <b>NOTE:</b> Mountain-ringed valley — expect katabatic/thermal effects off the Swartberg and Outeniqua
  ranges, and check for low cloud trapped against the escarpment, especially on the Swartberg Pass side.
</div>

<div class="disclaimer">
  Simplified plate for MSFS 2024 simulator use — built from public airport data, June 2026.
  FAOH has no published instrument approach; this is a VFR joining reference, not an IAP.
</div>
"""

PLATES = [
    ("FACT_ILS_RWY01.html", "FACT - ILS RWY 01", fact_body),
    ("FABW_VFR_JOINING.html", "FABW - VFR Joining Procedure", fabw_body),
    ("FAGG_ILS_RWY11.html", "FAGG - ILS RWY 11", fagg_body),
    ("FAOH_VFR_JOINING.html", "FAOH - VFR Joining Procedure", faoh_body),
]

if __name__ == "__main__":
    for filename, title, body in PLATES:
        html = page(title, body, "CoetzeeMed Flight Operations · FJCinSA", "MSFS 2024 Southern Africa Flight Pack")
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Written: {path}")
    print("\nDone. 4 plates written to Approaches\\")