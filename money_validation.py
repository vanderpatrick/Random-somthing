# make a hashmap of fixed bills that we need to pay.
fixed_bills_dict = {
    "Rent": 877.5,
    "jiu-jitsu": 50,
    "Mobile": 36,
    "heath plan": 142.50,
    "Current internet plan": 32.76,
    "Spotify": 11,
}
# create var for current salary
current_salary = float(2114.13)


# process fixed bills in relation to current salary to get liquid cash
def liquid_cash(current_money: float) -> float:
    sum_of_bills = sum(fixed_bills_dict.values())
    money_after_bills = int(current_money - sum_of_bills)

    return money_after_bills


current_processed_money = liquid_cash(current_money=current_salary)

print(current_processed_money)
