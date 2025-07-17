from strategy.context import PaymentProcessor
from strategy.strategies import CreditCardPayment, PayPalPayment, MpesaPayment

if __name__ == "__main__":
    # Scenario 1: Process payment using Credit Card
    print("--- Scenario 1: Credit Card Payment ---")
    credit_card_strategy = CreditCardPayment()
    processor = PaymentProcessor(credit_card_strategy)
    processor.process_payment(5000)
    print("\n")

    # Scenario 2: Switch to PayPal for the next payment
    print("--- Scenario 2: PayPal Payment ---")
    paypal_strategy = PayPalPayment()
    processor.set_payment_strategy(paypal_strategy)
    processor.process_payment(2500)
    print("\n")

    # Scenario 3: Process payment using M-Pesa
    print("--- Scenario 3: M-Pesa Payment ---")
    mpesa_strategy = MpesaPayment()
    processor_mpesa = PaymentProcessor(mpesa_strategy)
    processor_mpesa.process_payment(1000)
    print("\n")

    # Adding a new payment method like Bitcoin simply means:
    # 1. Creating a new BitcoinPayment class implementing PaymentStrategy.
    # 2. No changes to PaymentProcessor. Just use the new strategy.
