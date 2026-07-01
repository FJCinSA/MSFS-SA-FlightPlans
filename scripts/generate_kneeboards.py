#!/usr/bin/env python3
# Created: 30 June 2026 session.
"""
Generate kneeboard reference pages for the ZS-NTP Personal History Flights.

  1. Kneeboard_FAWB_FAPN_FAMM.html  - Wonderboom -> Pilanesberg -> Mafikeng
  2. Kneeboard_Stellenbosch.html    - Wonderboom -> Stellenbosch (4 legs)

Run from C:\\FlightPlans :
    python generate_kneeboards.py

Output -> C:\\FlightPlans\\Approaches\\
(kept alongside the approach plates - both are "fly with this" reference material)

Style: steam-gauge era, VFR, ADF/VOR only, no GPS - matches ZS-NTP ops.
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
.narrative{
  border-left:3px solid var(--cyan); padding:8px 14px; margin-bottom:16px;
  background:#0d141f; font-size:13px; line-height:1.6; color:var(--text);
}
.narrative b{color:var(--cyan);}
.leg{
  border:1px solid var(--line); border-radius:3px; margin-bottom:14px;
  background:#0d141f; overflow:hidden;
}
.leg-head{
  background:#152133; padding:8px 14px; display:flex; justify-content:space-between;
  align-items:baseline; border-bottom:1px solid var(--line);
}
.leg-head h2{font-size:14px; color:var(--amber); margin:0; letter-spacing:1px;}
.leg-head span{font-size:12px; color:var(--cyan);}
.leg-body{padding:10px 14px;}
table{width:100%; border-collapse:collapse; font-size:13px; margin-bottom:8px;}
table th, table td{border:1px solid var(--line); padding:5px 8px; text-align:center;}
table th{color:var(--cyan); background:#0d141f; font-size:11px; text-transform:uppercase;}
.notes{font-size:12px; color:var(--text); line-height:1.5; padding-top:4px;}
.notes b{color:var(--amber);}
.warning{
  border:1px solid var(--red); border-radius:3px; padding:8px 14px;
  background:#1a0d0d; color:#f0b8b8; font-size:12px; margin-top:8px;
}
.warning b{color:var(--red);}
.aircraft-box{
  border:1px solid var(--line); border-radius:3px; padding:10px 14px;
  background:#0d141f; margin-bottom:16px; font-size:13px;
}
.aircraft-box h2{font-size:12px; color:var(--cyan); margin:0 0 6px 0; text-transform:uppercase; letter-spacing:1px;}
.footer{
  border-top:1px solid var(--line); margin-top:10px; padding-top:8px;
  font-size:11px; color:var(--dim); display:flex; justify-content:space-between;
}
.disclaimer{
  font-size:11px; color:var(--dim); font-style:italic; margin-top:10px;
  border-top:1px dashed var(--line); padding-top:8px;
}
"""

def page(title, body_html):
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
<div class="footer"><span>CoetzeeMed Flight Operations &middot; FJCinSA</span><span>MSFS 2024 Southern Africa Flight Pack</span></div>
</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Kneeboard 1: FAWB -> FAPN -> FAMM
# ---------------------------------------------------------------------------
pilanesberg_body = """
<div class="header">
  <div>
    <h1>ZS-NTP &mdash; WONDERBOOM TO MAFIKENG</h1>
    <div class="sub">via Pilanesberg &middot; FAWB &rarr; FAPN &rarr; FAMM</div>
  </div>
  <div class="meta">
    VFR &middot; ADF/VOR ONLY &middot; NO GPS<br>
    CoetzeeMed Flight Operations &middot; FJCinSA
  </div>
</div>

<div class="narrative">
  James's first ever flight in ZS-NTP. Midsummer, midmorning departure &mdash; thermal turbulence built
  through the route, a bumpy ride throughout. Comms failure on the inbound to Pilanesberg, relayed via
  Johannesburg Information. <b>James handled the cellphone. Francois flew the aircraft.</b>
</div>

<div class="aircraft-box">
  <h2>Aircraft</h2>
  <p>ZS-NTP &mdash; 1978 Cessna 172N. Steam gauges. ADF + VOR, no GPS, no autopilot. Ex-Blue Crane Flying School, Wonderboom.</p>
</div>

<div class="leg">
  <div class="leg-head">
    <h2>LEG 1 &mdash; FAWB &rarr; FAPN</h2>
    <span>Wonderboom &rarr; Pilanesberg</span>
  </div>
  <div class="leg-body">
    <table>
      <tr><th>Cruise ALT</th><th>Conditions</th><th>Season</th><th>Departure</th></tr>
      <tr><td>Per sector plan</td><td>Scattered cumulus, thermal turbulence</td><td>Midsummer</td><td>~09:00 SAST</td></tr>
    </table>
    <div class="notes">
      <b>Fly it rough.</b> Expect bumps from mid-morning thermals over the bushveld. First-timer in the right seat &mdash; brief the turbulence before departure.
    </div>
    <div class="warning">
      <b>COMMS FAILURE:</b> Radio failure on the approach into Pilanesberg. Relayed via Johannesburg
      Information &mdash; James worked the cellphone while Francois continued flying the approach.
    </div>
  </div>
</div>

<div class="leg">
  <div class="leg-head">
    <h2>LEG 2 &mdash; FAPN &rarr; FAMM</h2>
    <span>Pilanesberg &rarr; Mafikeng</span>
  </div>
  <div class="leg-body">
    <table>
      <tr><th>Cruise ALT</th><th>Conditions</th><th>Track</th></tr>
      <tr><td>6,500 FT</td><td>VFR, scattered cumulus</td><td>RAW NAV &mdash; ADF/VOR</td></tr>
    </table>
    <div class="notes">
      Continuation leg onward to Mafikeng. RAW NAV ops throughout &mdash; no GPS reference, ADF and VOR only, matching the real ZS-NTP equipment fit.
    </div>
  </div>
</div>

<div class="disclaimer">
  Kneeboard reference for MSFS 2024 personal-history recreation &mdash; recreating Dr Francois Coetzee's
  real flights in ZS-NTP. PLN files: SOLO_FAWB_FAPN.pln / SOLO_FAPN_FAMM.pln. Fly VFR, steam gauges, no autopilot.
</div>
"""

# ---------------------------------------------------------------------------
# Kneeboard 2: Wonderboom -> Stellenbosch (4 legs)
# ---------------------------------------------------------------------------
stellenbosch_body = """
<div class="header">
  <div>
    <h1>ZS-NTP &mdash; WONDERBOOM TO STELLENBOSCH</h1>
    <div class="sub">Solo &middot; FAWB &rarr; FATM &rarr; FABW &rarr; FAWC &rarr; FASH</div>
  </div>
  <div class="meta">
    VFR &middot; ADF/VOR ONLY &middot; NO GPS<br>
    CoetzeeMed Flight Operations &middot; FJCinSA
  </div>
</div>

<div class="narrative">
  Solo flight, ZS-NTP. Four legs, including a moonless night sector across the Karoo and a low-level
  pass through Du Toitskloof to finish. No flight plan filed on the night leg.
</div>

<div class="aircraft-box">
  <h2>Aircraft</h2>
  <p>ZS-NTP &mdash; 1978 Cessna 172N. Steam gauges. ADF + VOR, no GPS, no autopilot.</p>
</div>

<div class="leg">
  <div class="leg-head">
    <h2>LEG 1 &mdash; FAWB &rarr; FATM</h2>
    <span>Wonderboom &rarr; New Tempe</span>
  </div>
  <div class="leg-body">
    <table>
      <tr><th>Notes</th></tr>
      <tr><td>New Tempe used in place of Bloemfontein (FABL) &mdash; avoided FABL landing fees.</td></tr>
    </table>
  </div>
</div>

<div class="leg">
  <div class="leg-head">
    <h2>LEG 2 &mdash; FATM &rarr; FABW</h2>
    <span>New Tempe &rarr; Beaufort West &mdash; NIGHT</span>
  </div>
  <div class="leg-body">
    <table>
      <tr><th>Cruise ALT</th><th>Conditions</th><th>Flight Plan</th></tr>
      <tr><td>8,000 FT</td><td>Dark moon, Karoo black below</td><td>None filed</td></tr>
    </table>
    <div class="warning">
      <b>NIGHT SECTOR &mdash; NO MOON:</b> Below is featureless Karoo dark, scattered farmhouse lights
      only. No flight plan filed. Steam gauges, ADF/VOR only &mdash; trust the instruments, not the ground.
    </div>
  </div>
</div>

<div class="leg">
  <div class="leg-head">
    <h2>LEG 3 &mdash; FABW &rarr; FAWC</h2>
    <span>Beaufort West &rarr; Worcester (diversion)</span>
  </div>
  <div class="leg-body">
    <table>
      <tr><th>Notes</th></tr>
      <tr><td>Cloud base dropping on approach to the mountains &mdash; diverted to Worcester rather than push on toward Stellenbosch direct.</td></tr>
    </table>
    <div class="notes">Decision point: lowering ceiling against rising terrain &mdash; divert early, land, reassess.</div>
  </div>
</div>

<div class="leg">
  <div class="leg-head">
    <h2>LEG 4 &mdash; FAWC &rarr; FASH</h2>
    <span>Worcester &rarr; Stellenbosch via Du Toitskloof Pass</span>
  </div>
  <div class="leg-body">
    <table>
      <tr><th>Cruise ALT</th><th>Routing</th><th>Time of day</th></tr>
      <tr><td>~2,000 FT</td><td>Du Toitskloof Pass, low level, following the N1</td><td>Afternoon</td></tr>
    </table>
    <div class="notes">
      East to west through the pass, mountains visible on both wings, N1 followed under the cloud deck as a line feature into Stellenbosch.
    </div>
  </div>
</div>

<div class="disclaimer">
  Kneeboard reference for MSFS 2024 personal-history recreation &mdash; recreating Dr Francois Coetzee's
  real flights in ZS-NTP. PLN files: STELL_LEG1_FAWB_FATM.pln / STELL_LEG2_FATM_FABW.pln /
  STELL_LEG3_FABW_FAWC.pln / STELL_LEG4_FAWC_FASH.pln. Fly VFR, steam gauges, no autopilot.
</div>
"""

PAGES = [
    ("Kneeboard_FAWB_FAPN_FAMM.html", "ZS-NTP - Wonderboom to Mafikeng", pilanesberg_body),
    ("Kneeboard_Stellenbosch.html", "ZS-NTP - Wonderboom to Stellenbosch", stellenbosch_body),
]

if __name__ == "__main__":
    for filename, title, body in PAGES:
        html = page(title, body)
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Written: {path}")
    print("\nDone. 2 kneeboards written to Approaches\\")