import random
from datetime import timedelta

import pandas as pd

# ===============================
# Load Loan Dataset
# ===============================

loans = pd.read_csv("../data/credit_risk_loans.csv")

payments = []

# ===============================
# Generate Payment History
# ===============================

for _, loan in loans.iterrows():

    loan_id = loan["loan_id"]
    customer_id = loan["customer_id"]

    tenure = int(loan["tenure_months"])

    emi = float(loan["emi_amount"])

    loan_amount = float(loan["loan_amount"])

    disbursement_date = pd.to_datetime(
        loan["disbursement_date"]
    )

    loan_status = loan["loan_status"]

    # Generate payments only until today
    months_elapsed = min(
        tenure,
        random.randint(1, tenure)
    )

    remaining_balance = loan_amount

    for installment in range(1, months_elapsed + 1):

        due_date = (
            disbursement_date +
            pd.DateOffset(months=installment)
        )

        payment_status = "Paid"

        payment_date = due_date

        days_past_due = 0

        # ---------------------------------
        # Business Logic
        # ---------------------------------

        if loan_status == "Active":

            payment_status = random.choices(
                ["Paid", "Late", "Partial"],
                weights=[80, 15, 5],
                k=1
            )[0]

        elif loan_status == "Closed":

            payment_status = "Paid"

        elif loan_status == "Defaulted":

            if installment >= months_elapsed - 2:

                payment_status = "Missed"

            else:

                payment_status = random.choice(
                    ["Paid", "Late"]
                )

        # ---------------------------------

        if payment_status == "Paid":

            payment_date = due_date

        elif payment_status == "Late":

            days_past_due = random.randint(1, 30)

            payment_date = due_date + timedelta(
                days=days_past_due
            )

        elif payment_status == "Partial":

            payment_date = due_date

        elif payment_status == "Missed":

            payment_date = None

            days_past_due = random.randint(90, 180)

        principal_paid = round(
            emi * 0.70,
            2
        )

        interest_paid = round(
            emi * 0.30,
            2
        )

        payment_amount = round(
            principal_paid + interest_paid,
            2
        )

        remaining_balance = max(
            0,
            remaining_balance - principal_paid
        )

        payments.append({

            "loan_id": loan_id,

            "customer_id": customer_id,

            "installment_number": installment,

            "due_date": due_date,

            "payment_date": payment_date,

            "payment_amount": payment_amount,

            "principal_paid": principal_paid,

            "interest_paid": interest_paid,

            "payment_status": payment_status,

            "days_past_due": days_past_due

        })

# ===============================
# Export
# ===============================

payment_df = pd.DataFrame(payments)

payment_df.to_csv(
    "../data/loan_payments.csv",
    index=False
)

print(payment_df.head())

print(payment_df.shape)