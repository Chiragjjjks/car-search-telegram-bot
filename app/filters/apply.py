def apply_filters(cars: list, filters: dict) -> list:
    """
    Applies structured filters on MongoDB car documents.

    cars    : list of car dicts from MongoDB
    filters : {
        max_price: int | None,
        color    : str | None,
        fuel     : str | None,
        max_km   : int | None
    }
    """

    filtered_cars = []

    for car in cars:
        # Price filter
        if filters.get("max_price") is not None:
            if car.get("price", 0) > filters["max_price"]:
                continue

        # Color filter
        if filters.get("color") is not None:
            if car.get("color", "").lower() != filters["color"]:
                continue

        # Fuel filter
        if filters.get("fuel") is not None:
            if car.get("fuel", "").lower() != filters["fuel"]:
                continue

        # KM filter
        if filters.get("max_km") is not None:
            if car.get("km", 0) > filters["max_km"]:
                continue

        # Passed all filters
        filtered_cars.append(car)

    return filtered_cars
