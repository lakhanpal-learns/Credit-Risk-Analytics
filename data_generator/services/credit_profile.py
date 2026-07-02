import random
from faker import Faker
from config import *
from utils import *

def generate_credit_profile(customer: dict) -> dict:
    """
    Generate a realistic credit profile based on customer characteristics.
    """

    income = customer["annual_income"]
    employment = customer["employment_type"]

    # ==========================================
    # Existing Loan Count
    # ==========================================

    if employment == "Salaried":
        existing_loan_count = random.randint(0, 4)

    elif employment == "Business Owner":
        existing_loan_count = random.randint(1, 6)

    elif employment == "Self-employed":
        existing_loan_count = random.randint(0, 5)

    else:
        existing_loan_count = random.randint(0, 2)

    # ==========================================
    # Existing Debt
    # ==========================================

    # debt_multiplier = random.uniform(0.0, 2.5)

    # ==========================================
    # Debt Multiplier based on Existing Loans
    # ==========================================

    if existing_loan_count == 0:

        debt_multiplier = random.uniform(
        0.00,
        0.30
    )

    elif existing_loan_count == 1:

        debt_multiplier = random.uniform(
            0.20,
            0.70
        )

    elif existing_loan_count == 2:

        debt_multiplier = random.uniform(
            0.50,
            1.00
        )

    elif existing_loan_count <= 4:

        debt_multiplier = random.uniform(
            0.80,
            1.50
        )

    else:

        debt_multiplier = random.uniform(
            1.20,
            2.20
        )

    existing_debt_amount = round(
        income * debt_multiplier,
        2
    )

    # ==========================================
    # Debt-to-Income Ratio
    # ==========================================
    # ==========================================
    # Debt Multiplier based on Existing Loans
    # ==========================================

    if existing_loan_count == 0:

        debt_multiplier = random.uniform(0.05, 0.30)

    elif existing_loan_count == 1:

        debt_multiplier = random.uniform(0.20, 0.50)

    elif existing_loan_count == 2:

        debt_multiplier = random.uniform(0.40, 0.70)

    elif existing_loan_count <= 4:

        debt_multiplier = random.uniform(0.60, 0.90)

    else:

        debt_multiplier = random.uniform(0.80, 1.10)
   
   
   
    existing_debt_amount = round(
    income * debt_multiplier,
    2
    )

    debt_to_income_ratio = round(
    (existing_debt_amount / income) * 100,
    2
    )

    # ==========================================
    # Credit Utilization
    # ==========================================

    if debt_to_income_ratio <= 20:

        credit_utilization = round(
            random.uniform(5, 30),
            2
        )

    elif debt_to_income_ratio <= 40:

        credit_utilization = round(
            random.uniform(20, 50),
            2
        )

    elif debt_to_income_ratio <= 60:

        credit_utilization = round(
            random.uniform(40, 70),
            2
        )

    else:

        credit_utilization = round(
            random.uniform(60, 95),
            2
        )

    # ==========================================
    # Previous Defaults
    # ==========================================

    if debt_to_income_ratio <= 30:

        previous_defaults = random.choices(
            [0, 1],
            weights=[97, 3],
            k=1
        )[0]

    elif debt_to_income_ratio <= 60:

        previous_defaults = random.choices(
            [0, 1, 2],
            weights=[88, 10, 2],
            k=1
        )[0]

    else:

        previous_defaults = random.choices(
            [0, 1, 2],
            weights=[70, 20, 10],
            k=1
        )[0]

    # ==========================================
    # Credit Score
    # ==========================================

    credit_score = 850

    # DTI Penalty
    credit_score -= int(debt_to_income_ratio * 1.2)

    # Utilization Penalty
    credit_score -= int(credit_utilization * 1.0)

    # Default Penalty
    credit_score -= previous_defaults * 120

    # Small Random Noise
    credit_score += random.randint(-15, 15)

    # Limit Score
    credit_score = max(
        300,
        min(850, credit_score)
    )

    return {

        "credit_score": credit_score,

        "credit_utilization_pct": credit_utilization,

        "debt_to_income_ratio": debt_to_income_ratio,

        "previous_defaults": previous_defaults,

        "existing_loan_count": existing_loan_count,

        "existing_debt_amount": existing_debt_amount

    }