import random
from datetime import timedelta

import pandas as pd


PAYMENT_MODES = [
    "Auto Debit",
    "UPI",
    "NEFT",
    "Debit Card",
    "Cash"
]


def generate_payment_schedule(loan: dict,payment_counter: int) -> tuple:
    """
    Generate complete payment schedule
    for one approved loan.
    """

    payments = []

    loan_id = loan["loan_id"]

    tenure = int(loan["tenure_months"])

    emi = float(loan["emi_amount"])

    loan_amount = float(loan["loan_amount"])

    disbursement_date = pd.to_datetime(
        loan["disbursement_date"]
    )

    loan_status = loan["loan_status"]

    today = pd.Timestamp.today().normalize()

    months_elapsed = 0

    for installment in range(1, tenure + 1):

        due_date = (
            disbursement_date +
            pd.DateOffset(months=installment)
        )

        if due_date <= today:

            months_elapsed += 1

        else:

            break

    remaining_balance = loan_amount

    

    for installment in range(1, months_elapsed + 1):

        due_date = (
            disbursement_date +
            pd.DateOffset(months=installment)
        )

        payment_status = generate_payment_status(
            loan_status,
            installment,
            months_elapsed
        )

        payment_date, days_past_due = generate_payment_date(
            payment_status,
            due_date
        )

        payment_amount = generate_payment_amount(
            payment_status,
            emi
        )

        principal_paid, interest_paid = split_payment(
            payment_amount
        )

        remaining_balance = calculate_remaining_balance(
            remaining_balance,
            principal_paid
        )
        # ==========================================
        # Closed Loan Balance Adjustment
        # ==========================================

        if (
            loan_status == "Closed"
            and installment == months_elapsed
        ):

          remaining_balance = 0

        payments.append({

            "payment_id":
                f"PAY{payment_counter:08d}",

            "loan_id":
                loan_id,

            "installment_number":
                installment,

            "due_date":
                due_date,

            "payment_date":
                payment_date,

            "emi_amount":
                emi,

            "payment_amount":
                payment_amount,

            "principal_paid":
                principal_paid,

            "interest_paid":
                interest_paid,

            "payment_status":
                payment_status,

            "days_past_due":
                days_past_due,

            "payment_mode":
                generate_payment_mode(),

            "remaining_balance":
                remaining_balance

        })

        payment_counter += 1

    return payments, payment_counter


def generate_payment_status(
    loan_status,
    installment,
    months_elapsed
):

    if loan_status == "Closed":

        return "Paid"

    if loan_status == "Active":

        return random.choices(

            [
                "Paid",
                "Late",
                "Partial"
            ],

            weights=[80,15,5],

            k=1

        )[0]

    if loan_status == "Defaulted":

        if installment >= months_elapsed - 2:

            return "Missed"

        return random.choice([
            "Paid",
            "Late"
        ])


def generate_payment_date(
    payment_status,
    due_date
):

    if payment_status == "Paid":

        return due_date, 0

    if payment_status == "Late":

        dpd = random.randint(1,30)

        return (
            due_date + timedelta(days=dpd),
            dpd
        )

    if payment_status == "Partial":

        dpd = random.randint(1,60)

        return (
            due_date + timedelta(days=dpd),
            dpd
        )

    if payment_status == "Missed":

        dpd = random.randint(90,180)

        return None, dpd


def generate_payment_amount(
    payment_status,
    emi
):

    if payment_status == "Paid":

        return emi

    if payment_status == "Late":

        return emi

    if payment_status == "Partial":

        return round(

            emi *
            random.uniform(0.30,0.80),

            2

        )

    return 0


def split_payment(
    payment_amount
):

    principal = round(
        payment_amount * 0.70,
        2
    )

    interest = round(
        payment_amount * 0.30,
        2
    )

    return principal, interest


def calculate_remaining_balance(
    remaining_balance,
    principal_paid
):

    return round(

        max(
            0,
            remaining_balance -
            principal_paid
        ),

        2

    )


def generate_payment_mode():

    return random.choice(
        PAYMENT_MODES
    )