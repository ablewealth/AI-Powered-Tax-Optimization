import pandas as pd

# Sample tax regulations data
data = {
    'tax_bracket': [1, 2, 3, 4, 5],
    'income_range': [
        '0-10000',
        '10001-30000',
        '30001-70000',
        '70001-150000',
        '150001+'
    ],
    'min_rate': [0.01, 0.05, 0.1, 0.15, 0.2],
    'max_rate': [0.05, 0.1, 0.15, 0.2, 0.25],
    'deduction_limit': [1000, 2000, 5000, 10000, 20000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Expand to create more rows with different tax rates (hypothetical example)
expanded_data = []

for i in range(5000):  # Generating 5000 rows
    tax_bracket = (i % 5) + 1
    income_range = data['income_range'][tax_bracket - 1]
    min_rate = data['min_rate'][tax_bracket - 1]
    max_rate = data['max_rate'][tax_bracket - 1]
    deduction_limit = data['deduction_limit'][tax_bracket - 1]
    
    expanded_data.append({
        'tax_bracket': tax_bracket,
        'income_range': income_range,
        'min_rate': min_rate,
        'max_rate': max_rate,
        'deduction_limit': deduction_limit
    })

# Create DataFrame from expanded data
expanded_df = pd.DataFrame(expanded_data)

# Save to CSV
expanded_df.to_csv("D:/AI-Powered Tax Optimization/data/tax_regulations.csv", index=False)
