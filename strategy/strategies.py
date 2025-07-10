from .interface import PaymentStrategy


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} KES via Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} KES via PayPal.")


class MpesaPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} KES via M-Pesa.")
