"""
Cosmetic Product Info Assistant
--------------------------------
Type a product name and get back: ingredients, uses/benefits,
directions to use, suitable skin type, and expiration info.

v3 -- formats the output into clean, readable sections instead
of a raw dictionary dump.

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


def print_product(product):
    print("=" * 50)
    print(product["name"])
    print("=" * 50)

    print("\nIngredients:")
    for ingredient in product["ingredients"]:
        print(f"  - {ingredient}")

    print("\nUses & Benefits:")
    print(f"  {product['uses_and_benefits']}")

    print("\nDirections to Use:")
    for i, step in enumerate(product["directions"], start=1):
        print(f"  {i}. {step}")

    print("\nSuitable Skin Type:")
    print(f"  {product['skin_type']}")

    print("\nExpiration:")
    print(f"  {product['expiration']}")
    print()


def main():
    if len(sys.argv) < 2:
        print('Usage: python app.py "Product Name"')
        return

    product_name = " ".join(sys.argv[1:])
    result = lookup_product(product_name)

    if result is None:
        print(f"No data found for '{product_name}' (only a couple of sample products are loaded so far).")
        return

    print_product(result)


if __name__ == "__main__":
    main()
