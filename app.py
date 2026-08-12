"""
Cosmetic Product Info Assistant
--------------------------------
Type a product name and get back: ingredients, uses/benefits,
directions to use, suitable skin type, and expiration info.

v4 -- expanded the product database from 2 to 5 real products.

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
    "the ordinary niacinamide": {
        "name": "The Ordinary Niacinamide 10% + Zinc 1%",
        "ingredients": ["Niacinamide (Vitamin B3)", "Zinc PCA"],
        "uses_and_benefits": "Helps reduce the look of blemishes and oiliness; supports a more balanced, even skin tone.",
        "directions": [
            "Apply a few drops to face morning and/or evening.",
            "Use before heavier creams; can sting if layered with pure Vitamin C.",
            "Always follow with sunscreen in the morning.",
        ],
        "skin_type": "Oily and blemish-prone skin, but generally tolerated by most types.",
        "expiration": "Typically 6-12 months after opening.",
    },
    "cetaphil gentle skin cleanser": {
        "name": "Cetaphil Gentle Skin Cleanser",
        "ingredients": ["Water", "Cetyl Alcohol", "Propylene Glycol", "Sodium Lauryl Sulfate"],
        "uses_and_benefits": "Gently removes dirt, oil, and makeup without stripping the skin's natural moisture.",
        "directions": [
            "Apply to face with fingertips or a cotton pad.",
            "Rinse with water, or wipe off for a no-rinse option.",
            "Use once or twice daily.",
        ],
        "skin_type": "Normal, dry, and sensitive skin.",
        "expiration": "Typically 12-24 months after opening.",
    },
    "vaseline original petroleum jelly": {
        "name": "Vaseline Original Petroleum Jelly",
        "ingredients": ["100% Petrolatum"],
        "uses_and_benefits": "Locks in moisture; protects and helps heal dry or chapped skin.",
        "directions": [
            "Apply a small amount to the affected area.",
            "Can be used on lips, hands, elbows, and minor skin irritations.",
            "Reapply as needed.",
        ],
        "skin_type": "All skin types, especially very dry or compromised skin.",
        "expiration": "Very long shelf life; typically fine for years if kept clean and sealed.",
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
        print(f"No data found for '{product_name}' (only a few sample products are loaded so far).")
        return

    print_product(result)


if __name__ == "__main__":
    main()
