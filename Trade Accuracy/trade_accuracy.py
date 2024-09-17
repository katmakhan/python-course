import random

def simulate_trade(accuracy, target_percent, stoploss_percent, buying_power):
    """Simulates a single trade based on accuracy, target percent, stoploss percent, and buying power."""
    trade_amount = buying_power  # Use the fixed buying power amount for each trade
    if random.uniform(0, 100) <= accuracy:
        # Successful trade
        profit = trade_amount * (target_percent / 100)
        print(f"Trade result: Profit ${profit:.2f}")
        return profit, True
    else:
        # Unsuccessful trade
        loss = trade_amount * (stoploss_percent / 100)
        print(f"Trade result: Loss ${loss:.2f}")
        return -loss, False

def calculate_profit_and_loss(num_trades, accuracy, target_percent, stoploss_percent, initial_amount, buying_power):
    """Calculates the overall profit and loss for a number of trades, including counting profits and losses."""
    current_amount = initial_amount
    num_profits = 0
    num_losses = 0
    
    for _ in range(num_trades):
        trade_result, is_profit = simulate_trade(accuracy, target_percent, stoploss_percent, buying_power)
        current_amount += trade_result
        if is_profit:
            num_profits += 1
        else:
            num_losses += 1
    
    total_profit_loss = current_amount - initial_amount
    percent_profit = (total_profit_loss / initial_amount) * 100
    
    return current_amount, total_profit_loss, percent_profit, num_profits, num_losses

def main():
    try:
        accuracy = float(input("Enter the accuracy percentage (0-100): "))
        target_percent = float(input("Enter the target percentage: "))
        stoploss_percent = float(input("Enter the stoploss percentage: "))
        num_trades = int(input("Enter the number of trades to simulate: "))
        initial_amount = float(input("Enter the initial amount: "))
        buying_power = float(input("Enter the buying power amount: "))
        
        if not (0 <= accuracy <= 100):
            raise ValueError("Accuracy percentage must be between 0 and 100.")
        if buying_power > initial_amount:
            raise ValueError("Buying power cannot exceed the initial amount.")
        
        final_amount, total_profit_loss, percent_profit, num_profits, num_losses = calculate_profit_and_loss(
            num_trades, accuracy, target_percent, stoploss_percent, initial_amount, buying_power
        )
        
        print(f"\nInitial amount: ${initial_amount:.2f}")
        print(f"Final amount after {num_trades} trades: ${final_amount:.2f}")
        print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
        print(f"Overall Percentage Profit/Loss: {percent_profit:.2f}%")
        print(f"Number of Profitable Trades: {num_profits}")
        print(f"Number of Losing Trades: {num_losses}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
