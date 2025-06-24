# utils.py -- Utility functions for UTMA/UGMA tax optimization

def get_kiddie_tax_thresholds(year, thresholds):
    """Retrieve kiddie tax thresholds for a given year from a thresholds dictionary."""
    return thresholds.get(str(year), {
        "tax_free": 1350,
        "child_rate_threshold": 1350,
        "parent_rate_threshold": 2700
    })

def calculate_unrealized_gain(cost_basis, current_value):
    """Calculate unrealized gain given cost basis and current value."""
    return current_value - cost_basis

def calculate_tax_impact(unrealized_gain, tax_rate):
    """Estimate tax impact of realizing a gain at a given tax rate."""
    if unrealized_gain <= 0:
        return 0
    return unrealized_gain * tax_rate

def format_currency(amount):
    """Format a number as currency string."""
    return f"${amount:,.2f}"

# Example usage (for testing)
if __name__ == "__main__":
    thresholds = {
        "2025": {
            "tax_free": 1350,
            "child_rate_threshold": 1350,
            "parent_rate_threshold": 2700
        }
    }
    year = 2025
    print("Kiddie Tax Thresholds:", get_kiddie_tax_thresholds(year, thresholds))
    gain = calculate_unrealized_gain(1000, 1500)
    print("Unrealized Gain:", gain)
    tax_impact = calculate_tax_impact(gain, 0.22)
    print("Estimated Tax Impact:", format_currency(tax_impact))
