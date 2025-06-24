from config.thresholds import get_kiddie_thresholds

def calculate_quantity(position, harvest_amount):
    """
    Calculate the number of shares to sell to realize the specified harvest_amount.
    Assumes you have 'current_price' and 'unrealized_gain' in the position dict.
    """
    # Estimate per-share gain
    per_share_gain = position.get('unrealized_gain', 0) / position.get('quantity', 1)
    if per_share_gain == 0:
        return 0
    # Number of shares to sell to realize harvest_amount
    qty = harvest_amount / per_share_gain
    # Can't sell more than you have
    return min(qty, position.get('quantity', 1))

def optimize_utma(account_data):
    thresholds = get_kiddie_thresholds(account_data['year'])
    remaining_budget = thresholds['parent_rate_threshold'] - account_data['ytd_income']
    
    optimization_plan = []
    for position in sorted(account_data['positions'], key=lambda x: x['tax_efficiency']):
        if remaining_budget <= 0: 
            break
        harvest_amount = min(position['unrealized_gain'], remaining_budget)
        optimization_plan.append({
            'symbol': position['symbol'],
            'action': 'SELL',
            'quantity': calculate_quantity(position, harvest_amount)
        })
        remaining_budget -= harvest_amount
    return optimization_plan
