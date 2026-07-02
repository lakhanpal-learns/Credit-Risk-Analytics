"""
=========================================
Utility Functions
Credit Risk Analytics Project
=========================================
"""

import random
from datetime import date, timedelta

import pandas as pd


# =========================================
# Random Date Generator
# =========================================

def random_date(start_date: date, end_date: date) -> date:
    """Generate a random date between two dates."""
    days = (end_date - start_date).days
    return start_date + timedelta(days=random.randint(0, days))


# =========================================
# Weighted Random Choice
# =========================================

def weighted_choice(options, weights):
    """Return one value based on weights."""
    return random.choices(options, weights=weights, k=1)[0]


# =========================================
# Age Calculator
# =========================================

def calculate_age(date_of_birth: date) -> int:
    """Calculate age from date of birth."""
    today = date.today()

    return (
        today.year
        - date_of_birth.year
        - (
            (today.month, today.day)
            < (date_of_birth.month, date_of_birth.day)
        )
    )


# =========================================
# EMI Calculator
# =========================================

def calculate_emi(
    principal: float,
    annual_interest_rate: float,
    tenure_months: int
) -> float:
    """
    Calculate monthly EMI.
    """

    monthly_rate = annual_interest_rate / (12 * 100)

    if monthly_rate == 0:
        return round(principal / tenure_months, 2)

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** tenure_months
    ) / (
        (1 + monthly_rate) ** tenure_months - 1
    )

    return round(emi, 2)


# =========================================
# Save CSV
# =========================================

def save_csv(df: pd.DataFrame, filepath: str):

    df.to_csv(filepath, index=False)

    print(f"Dataset saved -> {filepath}")