"""SandBase published list prices.

Source: https://www.sandbase.ai/models/deepseek/deepseek-v4-flash
Verified November 14, 2026.
"""


def fetch_prices() -> dict:
    """Return the published list prices before promotional discounts."""
    return {
        "deepseek/deepseek-v4-flash": {
            "input_price_per_1m": 0.30,
            "output_price_per_1m": 1.20,
        },
    }
