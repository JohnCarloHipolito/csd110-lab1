PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100


def get_num_of_cents():
    pennies = int(input("Enter the number of pennies: "))
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))
    return pennies, nickels, dimes, quarters

def calculate_total_cents(pennies, nickels, dimes, quarters):
    return (pennies * PENNY_VALUE) + (nickels * NICKEL_VALUE) + (dimes * DIME_VALUE) + (quarters * QUARTER_VALUE)

def prompt_result(total_cents):
    if total_cents > PENNIES_IN_DOLLAR:
        print("Sorry, the amount you entered was more than one dollar.")

    elif total_cents < PENNIES_IN_DOLLAR:
        print("Sorry, the amount you entered was less than one dollar.")

    else:
        print("Congratulations!")
        print("The amount you entered was exactly one dollar!")
        print("You win the game!!")

#MAIN PROGRAM FLOW
(pennies, nickels, dimes, quarters) = get_num_of_cents()
total_cents = calculate_total_cents(pennies, nickels, dimes, quarters)
prompt_result(total_cents)

