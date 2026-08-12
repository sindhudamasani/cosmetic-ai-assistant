"""
Cosmetic Product Info Assistant
--------------------------------
Type a product name and get back: ingredients, uses/benefits,
directions to use, suitable skin type, and expiration info.

This is v1 -- a skeleton. It doesn't look anything up yet,
it just confirms we can pass a product name in and get output.

Usage:
    python app.py "CeraVe Moisturizing Cream"
"""

import sys


def main():
    if len(sys.argv) < 2:
        print('Usage: python app.py "Product Name"')
        return

    product_name = " ".join(sys.argv[1:])
    print(f"You asked about: {product_name}")
    print("(Lookup logic coming in the next step.)")


if __name__ == "__main__":
    main()
