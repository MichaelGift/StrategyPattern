# Payment Processing System

This project demonstrates the **Strategy Design Pattern** by implementing a flexible payment processing system. The system allows for the addition of new payment methods without modifying the existing codebase, adhering to the **Open/Closed Principle**.

## Project Structure

```
.
├── client.py                  # Entry point for the application
├── strategy/
│   ├── context.py             # Contains the PaymentProcessor class (Context)
│   ├── interface.py           # Defines the PaymentStrategy interface (Abstract Base Class)
│   ├── strategies.py          # Implements concrete payment strategies
```

## Features

- **Flexible Payment Strategies**: Supports multiple payment methods such as Credit Card, PayPal, and M-Pesa.
- **Easily Extendable**: New payment methods can be added by implementing the `PaymentStrategy` interface.
- **Decoupled Design**: The `PaymentProcessor` class is independent of specific payment methods.

## How It Works

1. The `PaymentProcessor` class acts as the **Context** and delegates payment processing to a strategy.
2. The `PaymentStrategy` interface defines the contract for all payment methods.
3. Concrete strategies like `CreditCardPayment`, `PayPalPayment`, and `MpesaPayment` implement the `PaymentStrategy` interface.

## Usage

1. Clone the repository.
2. Run the `client.py` file to see the payment processing scenarios in action.

```bash
python client.py
```

### Example Output

```
--- Scenario 1: Credit Card Payment ---
Initiating payment processing for 5000 KES...
Paying 5000 KES via Credit Card.
Payment processing complete.

--- Scenario 2: PayPal Payment ---
Initiating payment processing for 2500 KES...
Paying 2500 KES via PayPal.
Payment processing complete.

--- Scenario 3: M-Pesa Payment ---
Initiating payment processing for 1000 KES...
Paying 1000 KES via M-Pesa.
Payment processing complete.
```

## Adding a New Payment Method

To add a new payment method (e.g., Bitcoin):
1. Create a new class (e.g., `BitcoinPayment`) in `strategies.py`.
2. Implement the `PaymentStrategy` interface.
3. Use the new strategy in `client.py` without modifying existing code.

Example:

```python
class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} KES via Bitcoin.")
```

## Requirements

- Python 3.7 or higher

## Design Principles Used

- **Strategy Pattern**: Encapsulates payment algorithms in separate classes.
- **Open/Closed Principle**: New payment methods can be added without modifying existing code.
- **Dependency Inversion Principle**: High-level modules depend on abstractions (`PaymentStrategy`).
