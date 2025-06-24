def get_kiddie_thresholds(year):
    thresholds = {
        2025: {
            "tax_free": 1350,
            "child_rate_threshold": 1350,
            "parent_rate_threshold": 2700
        }
    }
    return thresholds.get(year)
