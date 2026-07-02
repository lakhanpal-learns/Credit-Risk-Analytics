import random
from faker import Faker

from config import *
from utils import *

fake = Faker("en_IN")


def generate_risk_outcome(loan: dict, employment_type: str) -> dict:
    """
    Generate payment, default, recovery and write-off information.
    """

    status = loan["loan_status"]

    payment_status = "Paid"
    days_past_due = 0

    default_flag = "No"
    default_date = None
    default_reason = None

    recovery_amount = 0
    recovery_status = None

    writeoff_flag = "No"
    writeoff_amount = 0

    # ==========================================
    # Active Loan
    # ==========================================

    if status == "Active":

        days_past_due = random.choices(
            [
                0,
                random.randint(1, 30),
                random.randint(31, 89)
            ],
            weights=[80, 15, 5],
            k=1
        )[0]

        if days_past_due == 0:

            payment_status = "Paid"

        elif days_past_due <= 30:

            payment_status = "Late"

        else:

            payment_status = "Partial"

    # ==========================================
    # Closed Loan
    # ==========================================

    elif status == "Closed":

        payment_status = "Paid"
        days_past_due = 0

    # ==========================================
    # Defaulted Loan
    # ==========================================

    elif status == "Defaulted":

        days_past_due = random.randint(90, 365)

        payment_status = "Missed"

        default_flag = "Yes"

        default_date = fake.date_between(
            start_date=loan["disbursement_date"],
            end_date="today"
        )

        # Temporary rule
        # (Later we'll derive this from employment type)

        if employment_type == "Salaried":

            default_reason = "Job Loss"

        elif employment_type == "Business Owner":

            default_reason = "Business Failure"

        elif employment_type == "Self-employed":

            default_reason = "Cash Flow Issues"

        elif employment_type == "Retired":

            default_reason = "Medical Emergency"

        else:

           default_reason = "Financial Hardship"

        recovery_amount = round(
            loan["outstanding_balance"] *
            random.uniform(0.10, 0.70),
            2
        )

        recovery_status = random.choice([
            "Partial",
            "Full",
            "Failed"
        ])

        if recovery_status == "Failed":

            writeoff_flag = "Yes"

            writeoff_amount = round(
                loan["outstanding_balance"] -
                recovery_amount,
                2
            )

    return {

        "payment_status": payment_status,

        "days_past_due": days_past_due,

        "default_flag": default_flag,

        "default_date": default_date,

        "default_reason": default_reason,

        "recovery_amount": recovery_amount,

        "recovery_status": recovery_status,

        "writeoff_flag": writeoff_flag,

        "writeoff_amount": writeoff_amount

    }


# ==========================================
# Recovery Details
# ==========================================

def generate_recovery_details(risk: dict) -> dict:

    if risk["recovery_amount"] == 0:

        return {
            "recovery_method": None,
            "recovery_date": None
        }

    return {

        "recovery_method": random.choice([
            "Settlement",
            "Collection Agency",
            "Legal Action",
            "Asset Sale"
        ]),

        "recovery_date": fake.date_between(
            start_date=risk["default_date"],
            end_date="today"
        )

    }


# ==========================================
# Write-off Details
# ==========================================

def generate_writeoff_details(risk: dict) -> dict:

    if risk["writeoff_flag"] == "No":

        return {
            "writeoff_reason": None,
            "writeoff_date": None
        }

    recovery_date = risk.get("recovery_date")

    if recovery_date is None:
        recovery_date = "-1y"

    return {

        "writeoff_reason": random.choice([
            "Customer Insolvency",
            "Long-term Default",
            "Bank Policy",
            "Legal Closure"
        ]),

        "writeoff_date": fake.date_between(
            start_date=recovery_date,
            end_date="today"
        )

    }