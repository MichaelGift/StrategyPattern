def process_payment_legacy(method, amount):
    if method == "CreditCard":
        # Credit card processing logic
        print(f"Processing credit card payment of {amount} KES.")
    elif method == "PayPal":
        # PayPal processing logic
        print(f"Processing PayPal payment of {amount} KES.")
    elif method == "Mpesa":
        # M-Pesa processing logic
        print(f"Processing M-Pesa payment of {amount} KES.")
    else:
        raise ValueError("Unknown payment method")


process_payment_legacy("CreditCard", 400)
process_payment_legacy("PayPal", 500)
process_payment_legacy("Mpesa", 600)

# To add a new payment you would need to edit the function
process_payment_legacy("Bitcoin", 50)