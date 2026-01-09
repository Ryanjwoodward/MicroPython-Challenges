# Challenge: Using nested if-else (ATM machine)
# NOTE: this requires the use of Micropy REPL (i.e. via Picocom)

def withdraw(pin, amount):
    user_pin = 1234
    avaialble_amount = 5300

    if pin == user_pin:
        if amount <= avaialble_amount:

            print(f"withdrawing {amount}")
        else:
            print("Insufficient funds for withdrawal")
    else:
        print("incorrect pin")


withdraw(1234, 600)
withdraw(1124, 600)
withdraw(1234, 70000)
