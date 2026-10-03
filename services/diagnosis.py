"""Rule-based diagnosis. This is NOT AI.

To add AI later, keep the function signature `diagnose(category_slug, text)`
and return the same dict; the rest of the app will keep working.
"""
SAFETY = ("Only perform basic checks. Do not open electronic devices "
          "if you are not familiar with their components.")

# (category, keywords, issue, difficulty 1-5, cost, possible causes, safe steps)
RULES = [
    ("smartphone", ["charging", "charge", "cas", "baterai", "colok"], "Charging Port / Cable / Battery", 2, "Rp30.000 – Rp150.000",
     ["Charging port", "Cable", "Battery"],
     ["Try another cable and adapter.", "Try a different power outlet.", "With the phone off, gently remove lint from the port using a wooden toothpick.", "Restart the phone and test again."]),
    ("smartphone", ["layar", "screen", "retak", "crack", "touch", "sentuh"], "Display / Touch Panel", 4, "Rp250.000 – Rp1.200.000",
     ["Display", "Touch panel", "Screen protector"],
     ["Remove the screen protector and case.", "Clean the screen and your hands.", "Restart the phone.", "Back up your data, then see a repair service."]),
    ("headset", ["suara", "sound", "audio", "kanan", "kiri", "mati"], "Cable / Connector", 2, "Rp20.000 – Rp50.000",
     ["Cable", "Connector", "Speaker"],
     ["Check the cable for visible damage.", "Try another compatible cable or device.", "Check the connector for dirt.", "Test the device again."]),
    ("laptop", ["panas", "overheat", "kipas", "fan", "lemot", "lambat"], "Overheating / Dust Buildup", 3, "Rp75.000 – Rp250.000",
     ["Dust in vents", "Fan", "Thermal paste"],
     ["Place the laptop on a hard, flat surface.", "Blow air gently across the vents with the laptop off.", "Close heavy apps and check for updates.", "If still hot, ask a service to clean the fan."]),
    ("laptop", ["mati", "hidup", "charger", "baterai", "power", "menyala"], "Charger / Battery / Power", 3, "Rp100.000 – Rp600.000",
     ["Charger", "Battery", "Power port"],
     ["Check the charger and the outlet with another device.", "Unplug everything and hold the power button for 15 seconds.", "Reconnect the charger and try again.", "If it fails, see a repair service."]),
    ("electronics", ["mati", "menyala", "konslet", "power", "kabel", "colokan"], "Power Cable / Fuse / Switch", 3, "Rp50.000 – Rp200.000",
     ["Power cable", "Fuse", "Switch"],
     ["Unplug the device first.", "Test another outlet.", "Look for a damaged cable or plug.", "Never open the device; see a technician."]),
    ("bicycle", ["rantai", "chain", "gear", "bunyi", "rem", "brake", "ban", "bocor"], "Chain / Brake / Tire", 2, "Rp20.000 – Rp100.000",
     ["Chain", "Brake pads", "Tire"],
     ["Check tire pressure and look for punctures.", "Clean and lubricate the chain.", "Check that brake pads touch the rim evenly.", "Take a test ride in a safe area."]),
    ("clothing", ["sobek", "robek", "jahit", "lepas", "kancing", "resleting", "zipper"], "Seam / Zipper / Button", 1, "Rp10.000 – Rp50.000",
     ["Loose seam", "Zipper", "Button"],
     ["Wash and dry the area.", "Re-sew the seam or button with matching thread.", "Rub a candle or soap on a sticky zipper.", "Take it to a tailor for zipper replacement."]),
    ("furniture", ["goyang", "patah", "engsel", "longgar", "retak", "lepas"], "Loose Joint / Hinge / Screw", 2, "Rp50.000 – Rp250.000",
     ["Loose screws", "Hinge", "Joint glue"],
     ["Empty the furniture and check every screw.", "Tighten screws with the right screwdriver.", "Add wood glue to loose joints and clamp overnight.", "Replace damaged hinges."]),
]


def diagnose(category_slug, text):
    text = text.lower()
    best, best_hits = None, 0
    for rule in RULES:
        if rule[0] != category_slug:
            continue
        hits = sum(1 for k in rule[1] if k in text)
        if best is None or hits > best_hits:
            best, best_hits = rule, hits
    if best is None:  # unknown category
        return {"issue": "Needs inspection", "difficulty": 3, "cost": "Varies", "causes": [],
                "steps": [], "confidence": 20, "safety": SAFETY}
    _, _, issue, diff, cost, causes, steps = best
    confidence = min(90, 55 + 12 * best_hits) if best_hits else 35
    return {"issue": issue, "difficulty": diff, "cost": cost, "causes": causes,
            "steps": steps, "confidence": confidence, "safety": SAFETY}
