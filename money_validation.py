from decimal import *
from datetime import datetime
from utils.my_validation import Validation

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



# think of a way to get the weeks,
# week days are 5 and bellow
def get_week_weekend_day_percentage(processed) -> Decimal:
    get_day = datetime.now()
    week_day: Decimal = processed
    weekend_day: Decimal = Decimal(0.12)
    if get_day.weekday() < 5:
        return week_day
    else:
        return weekend_day


# function to control cash with the week/weekend allowed cash
def available_day_cash(
    current_day_percentage: Decimal, my_current_allowence: Decimal
) -> Decimal:
    print(current_day_percentage)
    print(my_current_allowence)


def main():
    my_salary = Validation.input_validation(current_salary)
    # my_total_bills = Validation.input_validation(sum_of_bills)
    # month_liquid_money = liquid_cash_per_month(my_salary, my_total_bills)
    # amount_to_savings = Validation.input_validation(
    #     saving(month_liquid_money, current_savings_percentage)
    # )
    # allowance_cash = allowance(month_liquid_money, amount_to_savings)
    current_week_day_allowed_percentage: Decimal = Decimal(0.05)
    current_weekend_day_allowed_percentage: Decimal = Decimal(0.12)
    # allowed_to_expend_percentage = get_week_weekend_day_percentage()
    print(f"{my_salary = }")
    # print(f"{month_liquid_money = }")
    # print(f"{month_liquid_money - amount_to_savings = }")
    # print(f"{amount_to_savings =}")
    # print(allowed_to_expend_percentage)
    # print(available_day_cash(allowed_to_expend_percentage, allowance_cash))
    # test = available_day_cash(allowed_to_expend_percentage, allowance_cash)


if __name__ == "__main__":
    main()
