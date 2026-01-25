from app.db.mongo import get_cars_collection
from app.filters.apply import apply_filters


def search_cars(filters: dict):
    cars_col = get_cars_collection()

    # 🔥 Pull only valid cars
    cars = list(cars_col.find({"status": "not_sold"}))

    print(f"📦 Cars in DB: {len(cars)}")

    # 🔥 Apply structured filters
    filtered = apply_filters(cars, filters)

    print(f"✅ Cars after filtering: {len(filtered)}")

    return filtered
