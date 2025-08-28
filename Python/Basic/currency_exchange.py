"""
This module contains functions for currency exchange calculations.
"""

def exchange_money(budget, exchange_rate):
    exchanged = budget / exchange_rate
    return exchanged
print("Exchange money: ", exchange_money(127.5, 1.2))

print(30*"-")

def get_change(budget, exchange_value):
    change = budget - exchange_value
    return change
print("Get change: ", get_change(127.5, 120))

print(30*"-")

def get_value_of_bills(denomination, number_of_bills):
    total_value = denomination * number_of_bills
    return int(total_value) 
print("Value of bills: ", get_value_of_bills(5, 128))

print(30*"-")

def get_number_of_bills(amount, denomination):
    currency_bills = amount // denomination
    return int(currency_bills) # using int() to ensure the result is an integer, even if the division results in a float
print("Numer of Bills: ", get_number_of_bills(127.5, 5))

print(30*"-")

def get_leftover_of_bills(amount, denomination):
    leftover = amount // denomination # This gives the number of full bills
    left = int(leftover*denomination) # Checking the total value of the bills   
    leftover = amount - left 
    return leftover

    # OR in a simple way:
    # leftover = amount % denomination
    # return leftover
print("Leftover of bills: ", get_leftover_of_bills(127.5, 20))

print(30*"-")


def exchangeable_value(budget, exchange_rate, spread, denomination):
    # Calculate the actual exchange rate with spread
    actual_rate = exchange_rate + (exchange_rate * spread / 100)
    # Calculate the amount received in the new currency
    exchanged = budget / actual_rate
    # Calculate the number of full bills you can get
    num_bills = int(exchanged // denomination)
    # Calculate the total value of those bills
    total_value = num_bills * denomination
    return int(total_value)
print("Exchangeable value: ", exchangeable_value(127.25, 1.20, 10, 20))