# batch_processor.py -- Batch process UTMA/UGMA accounts for tax optimization

import csv
from utma_optimizer import optimize_utma  # adjust import as needed

def process_accounts_batch(file_path, year=2025):
    """Process a batch of UTMA/UGMA accounts from a CSV file."""
    results = []
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            account_id = row.get('account_id')
            ytd_income = float(row.get('ytd_income', 0))
            # 'positions' should be a string representation of a list of dicts
            positions = eval(row.get('positions', '[]'))  
            account_data = {
                'year': year,
                'positions': positions,
                'ytd_income': ytd_income
            }
            optimization_plan = optimize_utma(account_data)
            results.append({'account_id': account_id, 'optimization_plan': optimization_plan})
    return results

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python batch_processor.py <csv_file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    batch_results = process_accounts_batch(file_path)
    for result in batch_results:
        print(f"Account: {result['account_id']}")
        print("Optimization Plan:")
        for action in result['optimization_plan']:
            print(action)
        print("---")
