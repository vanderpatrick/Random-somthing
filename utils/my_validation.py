import decimal
from decimal import *
from datetime import datetime
from typing import Any


class Validation:
    @classmethod
    def input_validation(cls, user_input: Decimal) -> Decimal:
        return Decimal(
            user_input.quantize(Decimal("0.00"), rounding=decimal.ROUND_HALF_EVEN)
        )

    @classmethod
    def liquid_cash_per_month(
        cls, my_salary: Decimal, my_total_bills: Decimal
    ) -> Decimal:
        return my_salary - my_total_bills

    @classmethod
    def savings(cls, liquid_cash: Decimal, percentage: Decimal) -> Decimal:
        return percentage * liquid_cash

    @classmethod
    def allowance(cls, liquid_cash: Decimal, savings_cash: Decimal) -> Decimal:
        return liquid_cash - savings_cash

    # we gotta see how to work with percentages
    # for this class, this one stays in standby
    @classmethod
    def get_day_percentage(cls) -> Decimal | Any:
        get_day = datetime.now()
        week_percent: Decimal = Decimal(0.05)
        weekend_percent: Decimal = Decimal(0.10)
        if get_day.weekday() < 5:
            return Decimal(week_percent)
        else:
            return Decimal(weekend_percent)

    # this one needs to make that stupid calculation
    @classmethod
    def available_day_cash(
        cls, formatted_current_day_percent: Decimal, allowence: Decimal
    ) -> Decimal:
        return formatted_current_day_percent * allowence


    # Next method is to add to savings what was not expended no fucking idea how that will work but im drunk now