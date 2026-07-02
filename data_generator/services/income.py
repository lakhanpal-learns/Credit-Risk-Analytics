import random


def generate_income(
    employment_type: str,
    education_level: str,
    age: int
) -> int:
    """
    Generate annual income based on
    employment, education and age.
    """

    # ==========================================
    # Base Income by Employment
    # ==========================================

    if employment_type == "Salaried":
        income = random.randint(300_000, 1_800_000)

    elif employment_type == "Self-employed":
        income = random.randint(500_000, 3_000_000)

    elif employment_type == "Business Owner":
        income = random.randint(800_000, 6_000_000)

    elif employment_type == "Retired":
        income = random.randint(200_000, 1_000_000)

    else:
        income = random.randint(100_000, 400_000)

    # ==========================================
    # Education Adjustment
    # ==========================================

    education_multiplier = {

        "High School": 1.00,
        "Bachelor": 1.10,
        "Master": 1.20,
        "PhD": 1.30

    }

    income *= education_multiplier[education_level]

    # ==========================================
    # Experience (Age) Adjustment
    # ==========================================

    if age < 25:

        income *= 0.80

    elif age < 35:

        income *= 1.00

    elif age < 50:

        income *= 1.20

    else:

        income *= 1.10

    return round(income)