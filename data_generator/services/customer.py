import random

from faker import Faker

from config import *
from utils import *

from services.income import generate_income

fake = Faker("en_IN")


def generate_customer(application_date) -> dict:
    """
    Generate customer information.
    """

    dob = fake.date_of_birth(
        minimum_age=21,
        maximum_age=70
    )

    age = calculate_age(dob)

    education_level = random.choice([
        "High School",
        "Bachelor",
        "Master",
        "PhD"
    ])

    employment_type = weighted_choice(
        EMPLOYMENT_TYPES,
        EMPLOYMENT_WEIGHTS
    )

    annual_income = generate_income(
        employment_type,
        education_level,
        age
    )

    # ==========================================
    # Marital Status
    # ==========================================

    if age <= 25:

      marital_status = random.choices(
          ["Single", "Married"],
          weights=[95, 5],
          k=1
      )[0]    

    elif age <= 35:
    
        marital_status = random.choices(
            ["Single", "Married", "Divorced"],
            weights=[35, 60, 5],
            k=1
        )[0]

    elif age <= 50:

        marital_status = random.choices(
            ["Married", "Single", "Divorced"],
            weights=[70, 10, 20],
            k=1
        )[0]

    else:

        marital_status = random.choices(
            ["Married", "Divorced", "Single"],
            weights=[60, 35, 5],
            k=1
        )[0]

    return {

        "first_name": fake.first_name(),

        "last_name": fake.last_name(),

        "date_of_birth": dob,

        "age": age,

        "gender": random.choice(GENDERS),

       "marital_status": marital_status,

        "education_level": education_level,

        "employment_type": employment_type,

        "annual_income": annual_income,

        "customer_since": fake.date_between(
            start_date="-10y",
            end_date=application_date
        )

    }