import random
from faker import Faker

from config import *
from utils import *

fake = Faker("en_IN")


def generate_application(
    customer: dict,
    profile: dict,
    product: dict,
    branch: dict
) -> dict:
    """
    Generate loan application based on
    customer and credit profile.
    """

    application_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )

    loan_product = product["loan_product"]

    # ==========================================
    # Requested Amount
    # ==========================================

    if loan_product == "Personal Loan":
        requested_amount = random.randint(50_000, 2_000_000)

    elif loan_product == "Home Loan":
        requested_amount = random.randint(500_000, 10_000_000)

    elif loan_product == "Auto Loan":
        requested_amount = random.randint(200_000, 3_000_000)

    elif loan_product == "Education Loan":
        requested_amount = random.randint(100_000, 2_500_000)

    elif loan_product == "Business Loan":
        requested_amount = random.randint(200_000, 7_500_000)

    # ==========================================
    # Requested Tenure
    # ==========================================

    if loan_product == "Personal Loan":

        requested_tenure = random.choice([
            12, 24, 36, 48, 60
        ])

    elif loan_product == "Home Loan":

        requested_tenure = random.choice([
            120, 180, 240, 300, 360
        ])

    elif loan_product == "Auto Loan":

        requested_tenure = random.choice([
            36, 48, 60, 72, 84
        ])

    elif loan_product == "Education Loan":

        requested_tenure = random.choice([
            24, 36, 48, 60, 84, 120
        ])

    elif loan_product == "Business Loan":

        requested_tenure = random.choice([
            12, 24, 36, 48, 60, 84, 120
        ])

    # ==========================================
    # Customer Profile
    # ==========================================

    score = profile["credit_score"]
    dti = profile["debt_to_income_ratio"]
    defaults = profile["previous_defaults"]
    income = customer["annual_income"]

    # ==========================================
    # Eligibility Multiplier
    # ==========================================

    if loan_product == "Personal Loan":
        eligibility_multiplier = 3

    elif loan_product == "Auto Loan":
        eligibility_multiplier = 4

    elif loan_product == "Home Loan":
        eligibility_multiplier = 8

    elif loan_product == "Education Loan":
        eligibility_multiplier = 5

    elif loan_product == "Business Loan":
        eligibility_multiplier = 6

    max_eligible_amount = income * eligibility_multiplier

    # ==========================================
    # DTI Eligibility Adjustment
    # ==========================================

    if dti <= 20:

        eligibility_factor = 1.00

    elif dti <= 40:

        eligibility_factor = 0.90

    elif dti <= 60:

        eligibility_factor = 0.75

    else:

        eligibility_factor = 0.50

    max_eligible_amount *= eligibility_factor

    # ==========================================
    # Loan Decision
    # ==========================================

    approved_amount = None
    approval_date = None
    rejection_reason = None

    # Hard Rejection Rules

    if dti > 50:

        status = "Rejected"
        rejection_reason = "High Debt-to-Income Ratio"

    elif defaults > 0:

        status = "Rejected"
        rejection_reason = "Previous Defaults"

    elif requested_amount > max_eligible_amount:

        status = "Rejected"
        rejection_reason = "Requested Amount Exceeds Eligibility"

    # Excellent Credit Score

    elif score >= 700:

        status = "Approved"

    # Borderline Credit Score

    elif score >= 650:

        status = random.choices(
            ["Approved", "Rejected"],
            weights=[70, 30],
            k=1
        )[0]

        if status == "Rejected":

            rejection_reason = "Borderline Credit Score"

    # Poor Credit Score

    else:

        status = "Rejected"
        rejection_reason = "Low Credit Score"

    # ==========================================
    # Approved Loan Details
    # ==========================================

    if status == "Approved":

        approved_amount = round(
            requested_amount * random.uniform(0.85, 1.00),
            2
        )

        approval_date = application_date

    # ==========================================
    # Return
    # ==========================================

    return {

        "application_date": application_date,

        "requested_amount": requested_amount,

        "requested_tenure_months": requested_tenure,

        "application_status": status,

        "approved_amount": approved_amount,

        "approval_date": approval_date,

        "rejection_reason": rejection_reason

    }