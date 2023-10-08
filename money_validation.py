from decimal import *
from utils.my_validation import Validation as v

# make a hashmap of fixed bills that we need to pay.
fixed_bills_dict = {
    "Rent": 877.5,
    "jiu-jitsu": 50,
    "Mobile": 36,
    "heath plan": 142.50,
    "Current internet plan": 32.76,
    "Spotify": 11,
}
# expected_value =
# Loose variables
current_salary: Decimal = Decimal(2114.13)
sum_of_bills: Decimal = Decimal(sum(fixed_bills_dict.values()))
current_savings_percentage: Decimal = Decimal(0.60)


def main():
    liquid_amount = v.liquid_cash_per_month(current_salary, sum_of_bills)
    formatted_liquid_amount = v.input_validation(liquid_amount)
    savings_amount = v.savings(liquid_amount, current_savings_percentage)
    formatted_savings_amount = v.input_validation(savings_amount)
    my_allowance = v.allowance(liquid_amount, savings_amount)
    formatted_my_allowance = v.input_validation(my_allowance)
    current_day = v.get_day_percentage()
    formatted_current_day_percent = v.input_validation(current_day)
    print(formatted_my_allowance)
    print(formatted_current_day_percent)
    print(
        v.input_validation(
            v.available_day_cash(formatted_current_day_percent, formatted_my_allowance)
        )
    )


if __name__ == "__main__":
    main()
