from datetime import date, timedelta
TODAY = date(2026, 3, 1)
# (report id, date reported, policy days, extension days granted, date patched or None)
REPORTS = [
("R1", date(2026, 1, 5), 90, 0, date(2026, 2, 20)),
("R2", date(2026, 1, 20), 45, 14, None),
("R3", date(2025, 11, 10), 90, 0, None),
]
def deadline(reported, policy_days, extension_days):
"""Returns the date on which details may be published."""
# TODO 1: Return reported + policy_days + extension_days as a date (use timedelta)
pass # replace this line with your code
def status(reported, policy_days, extension_days, patched):
due = deadline(reported, policy_days, extension_days)
if patched is not None:
# TODO 2: Return "PATCHED on time" if patched <= due, otherwise
# "PATCHED late by N days" where N is the number of days after the deadline
pass # replace this line with your code
left = (due - TODAY).days
return f"OPEN, {left} days left" if left >= 0 else f"OVERDUE by {-left} days - publish"
for rid, rep, pol, ext, pat in REPORTS:
print(f"{rid} due {deadline(rep, pol, ext)} {status(rep, pol, ext, pat)}")