"""Session 01: variables, types and f-strings.

Replace every None with your own answer, then run:  python3 s01_basics.py
"""

app_name = None      # str: "EA Portal"
app_id = None        # int: 1042
annual_cost = None   # float: 125000.50
is_active = None     # bool: True
summary = None       # f-string: "EA Portal (ID 1042) costs 125,000.50/yr - active: True"
apps = None          # list: 3 application names

raw_cost = "250000"
uplifted = None      # raw_cost converted to a number, plus a 10% uplift (~275000)

# --- Checks (do not edit below) ---
assert isinstance(app_name, str) and app_name == "EA Portal", "app_name should be the str 'EA Portal'"
assert isinstance(app_id, int) and not isinstance(app_id, bool) and app_id == 1042, "app_id should be the int 1042"
assert isinstance(annual_cost, float) and annual_cost == 125000.50, "annual_cost should be the float 125000.50"
assert is_active is True, "is_active should be the bool True"
assert summary == "EA Portal (ID 1042) costs 125,000.50/yr - active: True", (
    f"summary should be 'EA Portal (ID 1042) costs 125,000.50/yr - active: True', got {summary!r}"
)
assert isinstance(apps, list) and len(apps) == 3, "apps should be a list of exactly 3 names"
assert all(isinstance(a, str) for a in apps), "every item in apps should be a str"
assert isinstance(uplifted, (int, float)) and abs(uplifted - 275000) < 1, (
    f"uplifted should be about 275000 (convert raw_cost, add 10%), got {uplifted!r}"
)

print("✅ All checks passed — Session 01 complete")
