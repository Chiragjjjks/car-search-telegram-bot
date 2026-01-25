import re

COLORS = ["white", "black", "red", "silver", "blue", "grey", "gray"]

def extract_price(text: str):
    text = text.lower()

    match = re.search(r"(under|below|less than)\s*(\d+(\.\d+)?)\s*l", text)
    if match:
        return int(float(match.group(2)) * 100000)

    match = re.search(r"(under|below|less than)\s*(\d+)\s*lakh", text)
    if match:
        return int(match.group(2)) * 100000

    match = re.search(r"(under|below|less than)\s*(\d{5,7})", text)
    if match:
        return int(match.group(2))

    return None


def extract_color(text: str):
    text = text.lower()
    for color in COLORS:
        if color in text:
            return color
    return None


def extract_fuel(text: str):
    text = text.lower()
    if "diesel" in text:
        return "diesel"
    if "petrol" in text:
        return "petrol"
    if "cng" in text:
        return "cng"
    if "electric" in text:
        return "electric"
    return None


def extract_km(text: str):
    text = text.lower()

    match = re.search(r"(under|below|less than)\s*(\d+)\s*lakh\s*km", text)
    if match:
        return int(match.group(2)) * 100000

    match = re.search(r"(under|below|less than)\s*(\d+)\s*km", text)
    if match:
        return int(match.group(2))

    return None


def parse_filters(user_text: str) -> dict:
    return {
        "max_price": extract_price(user_text),
        "color": extract_color(user_text),
        "fuel": extract_fuel(user_text),
        "max_km": extract_km(user_text),
    }
