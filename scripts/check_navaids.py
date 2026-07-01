# Created: 30 June 2026 session.
# Searches the Little Navmap SQLite databases (AppData\Roaming\ABarthel\little_navmap_db)
# for VOR/NDB/waypoint idents (BDV, JF, BL) to check whether they resolve as real navdata,
# and against which region. Prints matches per table/database, or 0 if not found.

import sqlite3, glob, os

# Locate the LNM database automatically
search_paths = glob.glob(
    os.path.expanduser(r"~\AppData\Roaming\ABarthel\little_navmap_db\*.sqlite")
)
print("Found databases:", search_paths)

for db_path in search_paths:
    print(f"\n--- Checking {db_path} ---")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # List tables so we confirm schema before querying
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [t[0] for t in cur.fetchall()]

    for table in ("vor", "ndb", "waypoint"):
        if table not in tables:
            continue
        cur.execute(f"PRAGMA table_info({table})")
        cols = [c[1] for c in cur.fetchall()]
        ident_col = "ident" if "ident" in cols else None
        if not ident_col:
            continue
        for ident in ("BDV", "JF", "BL"):
            cur.execute(f"SELECT * FROM {table} WHERE {ident_col}=? AND region=?", (ident, "FA"))
            rows = cur.fetchall()
            print(f"{table:10s} {ident:5s} (region=FA) -> {len(rows)} match(es)")
            if rows:
                print("   ", dict(zip(cols, rows[0])))

    conn.close()
