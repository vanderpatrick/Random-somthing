from decimal import *
import datetime


class Validation:
    @classmethod
    def input_validation(cls, user_input: Decimal) -> Decimal:
        return Decimal(user_input.quantize(Decimal("0.00")))

    @classmethod
    def liquid_cash_per_month(cls, my_salary: Decimal, my_total_bills: Decimal) -> Decimal:
        return my_salary - my_total_bills


    @classmethod
    def savings(cls, liquid_cash: Decimal, percentage: Decimal) ->:
        return percentage * liquid_cash


    @classmethod
    def allowance(cls, liquid_cash: Decimal, savings_cash: Decimal) ->:
        return liquid_cash - savings_cash

    # we gotta see how to work with percentages
    # for this class, this one stays in standby
    @classmethod
    def get_day_percentage(cls):
        get_day = datetime.now()
        week_day_percentage: str = "5%"
        weekend_day_percentage: str = "12%"

        if get_day.weekday() < 5:
            return week_day_percentage
        else:
            return weekend_day_percentage

    # this one needs to make that stupid calculation
    @classmethod
    def available_day_cash(cls, current_day_percentage: Decimal, allowence: Decimal) -> Decimal:
        pass