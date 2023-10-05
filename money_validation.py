from decimal import *

# make a hashmap of fixed bills that we need to pay.
fixed_bills_dict = {
    "Rent": 877.5,
    "jiu-jitsu": 50,
    "Mobile": 36,
    "heath plan": 142.50,
    "Current internet plan": 32.76,
    "Spotify": 11,
}
# Loose variables
current_salary: Decimal = Decimal(2114.13)
sum_of_bills: Decimal = Decimal(sum(fixed_bills_dict.values()))
current_savings_percentage: Decimal = Decimal(0.60)


# This function validates input to decimals
def input_validation(user_input: Decimal) -> Decimal:
    return Decimal(user_input).quantize(Decimal("0.01"), rounding=ROUND_DOWN)


# Returns liquid amount of cash
def liquid_cash_per_month(my_salary: Decimal, my_total_bills: Decimal) -> Decimal:
    return my_salary - my_total_bills


# saving function i want 60% to go to savings
def saving(validated_liquid_cash: Decimal, percentage: Decimal) -> Decimal:
    return percentage * validated_liquid_cash


# allowance function
def allowance(liquid_mont_cash: Decimal, current_saving_cash: Decimal) -> Decimal:
    return liquid_mont_cash - current_saving_cash


def main():
    my_salary = input_validation(current_salary)
    my_total_bills = input_validation(sum_of_bills)
    month_liquid_money = liquid_cash_per_month(my_salary, my_total_bills)
    amount_to_savings = input_validation(
        saving(month_liquid_money, current_savings_percentage)
    )
    test = allowance(month_liquid_money, amount_to_savings)
    print(f"{my_salary = }")
    print(f"{my_total_bills = }")
    print(f"{month_liquid_money = }")
    print(month_liquid_money - amount_to_savings)
    print(f"{amount_to_savings =}")
    print(test)


if __name__ == "__main__":
    main()
