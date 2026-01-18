from app.db.mongo import get_cars_collection


def get_all_available_cars():
    cars_col = get_cars_collection()
    return list(cars_col.find({"status": "not_sold"}))
