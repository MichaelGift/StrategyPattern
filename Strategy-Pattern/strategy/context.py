# Context
class PaymentProcessor:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def process_payment(self, amount):
        print(f"Initiating payment processing for {amount} KES...")
        self._payment_strategy.pay(amount)
        print("Payment processing complete.")
