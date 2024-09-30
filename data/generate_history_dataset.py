import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Sample size
n_samples = 5000

# Generate sample data
data = {
    'income': np.random.randint(30000, 150000, size=n_samples),
    'investment_income': np.random.randint(0, 20000, size=n_samples),
    'deductions': np.random.randint(0, 30000, size=n_samples),
    'age': np.random.randint(18, 70, size=n_samples),
    'state': np.random.choice(['CA', 'TX', 'NY', 'FL', 'WA'], size=n_samples),
}

# Create target variable (simple example logic)
data['target'] = (data['income'] * 0.2 + data['investment_income'] * 0.15 - data['deductions'] * 0.25).clip(0)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('D:\AI-Powered Tax Optimization\data\historical_data.csv', index=False)
