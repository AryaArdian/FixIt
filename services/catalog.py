"""All FixIt data lives here (no database). Edit this file to change categories or services.

To move to a real database later, only the three functions at the bottom
(get_category, get_service, list_services) need to be rewritten.
"""
_CATEGORIES = [  # (slug, name, icon)
    ("smartphone", "Smartphone", "📱"), ("laptop", "Laptop", "💻"),
    ("headset", "Headset", "🎧"), ("electronics", "Electronics", "🔌"),
    ("bicycle", "Bicycle", "🚲"), ("clothing", "Clothing", "👕"),
    ("furniture", "Furniture", "🪑"),
]
CATEGORIES = [dict(slug=s, name=n, icon=i) for s, n, i in _CATEGORIES]

# Dummy data: (name, category, address, phone, rating, price, hours, lat, lng, km)
_SERVICES = [
    ("FixTech Service", "Smartphone, Laptop, Electronics", "Jl. Contoh No. 12", "0812-0000-0001", 4.8, "Starting from Rp30.000", "09:00 – 20:00", -6.2, 106.8, 1.2),
    ("Audio Care", "Headset, Electronics", "Jl. Mawar No. 5", "0812-0000-0002", 4.6, "Starting from Rp20.000", "10:00 – 18:00", -6.21, 106.81, 2.4),
    ("Pedal Garage", "Bicycle", "Jl. Melati No. 9", "0812-0000-0003", 4.7, "Starting from Rp15.000", "08:00 – 17:00", -6.22, 106.79, 3.1),
    ("Jahit Cepat", "Clothing", "Jl. Anggrek No. 3", "0812-0000-0004", 4.5, "Starting from Rp10.000", "09:00 – 19:00", -6.19, 106.82, 1.8),
    ("Kayu & Engsel", "Furniture", "Jl. Kenanga No. 21", "0812-0000-0005", 4.4, "Starting from Rp50.000", "08:00 – 16:00", -6.23, 106.83, 4.0),
]
_KEYS = ("name", "category", "address", "phone", "rating", "price_range",
         "opening_hours", "latitude", "longitude", "distance_km")
SERVICES = [dict(zip(_KEYS, row), id=i) for i, row in enumerate(_SERVICES, start=1)]


def get_category(slug):
    return next((c for c in CATEGORIES if c["slug"] == slug), None)


def get_service(service_id):
    return next((s for s in SERVICES if s["id"] == service_id), None)


def list_services(category=""):
    rows = [s for s in SERVICES if category.lower() in s["category"].lower()]
    return sorted(rows, key=lambda s: s["distance_km"])
