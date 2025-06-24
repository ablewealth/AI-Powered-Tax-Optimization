# run_batch.py
from utma_tax_optimizer.batch_processor import process_accounts_batch
if __name__ == "__main__":
    results = process_accounts_batch("utma_tax_optimizer/your_accounts_file.csv")
    for result in results:
        print(f"Account: {result['account_id']}")
        print("Optimization Plan:")
        for action in result['optimization_plan']:
            print(action)
        print("---")
