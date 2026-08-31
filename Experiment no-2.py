from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} payment completed using Credit Card.")


# Concrete Strategy 2
class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} payment completed using Debit Card.")


# Concrete Strategy 3
class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} payment completed using UPI.")


# Context Class
class PaymentProcessor:

    def __init__(self):
        self.strategy = None

    def choose_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):

        if self.strategy is None:
            print("Select a payment method first.")
        else:
            self.strategy.pay(amount)


def main():

    processor = PaymentProcessor()

    while True:

        print("\n========== PAYMENT SYSTEM ==========")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        print("4. Exit")

        choice = input("Choose payment option: ")

        if choice == "4":
            print("Payment system closed. Thank You!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid option! Please try again.")
            continue

        amount = float(input("Enter amount: ₹"))

        if choice == "1":
            processor.choose_strategy(CreditCardPayment())

        elif choice == "2":
            processor.choose_strategy(DebitCardPayment())

        elif choice == "3":
            processor.choose_strategy(UpiPayment())

        processor.make_payment(amount)


if __name__ == "__main__":
    main()
