from modules.custodian_adapters import get_adapter
from modules.utma_optimizer import optimize_utma
from modules.compliance_recorder import generate_report

def execute_annual_review(account_id, year=2025):
    custodian = get_adapter('schwab')
    positions = custodian.fetch_positions(account_id)
    account_data = {
        'year': year,
        'positions': positions,
        'ytd_income': get_ytd_income(account_id)
    }
    
    optimization_plan = optimize_utma(account_data)
    generate_report(account_id, optimization_plan)
    return optimization_plan
