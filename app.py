"""
Cosmetic Product Info Assistant
--------------------------------
Type a product name and get back: ingredients, uses/benefits,
directions to use, suitable skin type, and expiration info.

v2 -- adds a small built-in database of sample products and a
lookup function. Real AI lookup (for ANY product) comes later --
this step is just to get the shape of the data right.

Usage:
    python app.py "CeraVe Moisturizing Cream"
"""

import sys

PRODUCT_DATABASE = {
    "cerave moisturizing cream": {
        "name": "CeraVe Moisturizing Cream",
        "ingredients": ["Ceramides", "Hyaluronic Acid", "Glycerin", "Petrolatum"],
        "uses_and_benefits": "Deep hydration for dry to very dry skin; helps restore the skin barrier.",
        "directions": [
            "Apply to clean skin.",
            "Massage in gently until absorbed.",
            "Use daily, morning and night.",
        ],
        "skin_type": "Dry, sensitive, and normal skin.",
        "expiration": "Typically 12 months after opening (check the jar symbol, e.g. '12M').",
    },
    "neutrogena hydro boost": {
        "name": "Neutrogena Hydro Boost Water Gel",
        "ingredients": ["Hyaluronic Acid", "Dimethicone", "Glycerin"],
        "uses_and_benefits": "Lightweight hydration; plumps skin without feeling greasy.",
        "directions": [
            "Apply to face and neck after cleansing.",
            "Use morning and night.",
            "Follow with sunscreen during the day.",
        ],
        "skin_type": "Normal, combination, and oily skin.",
        "expiration": "Typically 12 months after opening.",
    },
}


def lookup_product(product_name):
    key = product_name.strip().lower()
    return PRODUCT_DATABASE.get(key)


def main():
    if len(sys.argv) < 2:
        print('Usage: python app.py "Product Name"')
        return

    product_name = " ".join(sys.argv[1:])
    result = lookup_product(product_name)

    if result is None:
        print(f"No data found for '{product_name}' (only a couple of sample products are loaded so far).")
        return

    print(result)


if __name__ == "__main__":
    main()
