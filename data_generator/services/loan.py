import random
from faker import Faker
from config import *
from utils import *

def generate_loan( application: dict,profile: dict,product: dict ) -> dict | None:
    """
    Generate loan information for approved applications.
    """

    if application["application_status"] != "Approved":
        return None

    loan_amount = application["approved_amount"]
    tenure = application["requested_tenure_months"]

    score = profile["credit_score"]
    loan_product = product["loan_product"]

    # # Interest Rate Logic
    # if score >= 750:
    #     interest_rate = round(random.uniform(7.0, 9.0), 2)
    # elif score >= 700:
    #     interest_rate = round(random.uniform(9.0, 11.0), 2)
    # elif score >= 650:
    #     interest_rate = round(random.uniform(11.0, 13.0), 2)
    # else:
    #     interest_rate = round(random.uniform(13.0, 16.0), 2)

    
    # ==============================
    # Interest Rate Logic
    # ==============================

    loan_product = product["loan_product"]

    if loan_product == "Home Loan":

      if score >= 750:
        interest_rate = round(random.uniform(7.0, 8.0), 2)
      elif score >= 700:
        interest_rate = round(random.uniform(8.0, 9.0), 2)
      elif score >= 650:
        interest_rate = round(random.uniform(9.0, 10.0), 2)
      else:
        interest_rate = round(random.uniform(10.0, 11.0), 2)

    elif loan_product == "Personal Loan":

     if score >= 750:
        interest_rate = round(random.uniform(10.0, 11.5), 2)
     elif score >= 700:
        interest_rate = round(random.uniform(11.5, 13.0), 2)
     elif score >= 650:
        interest_rate = round(random.uniform(13.0, 14.5), 2)
     else:
        interest_rate = round(random.uniform(14.5, 16.0), 2)

    elif loan_product == "Auto Loan":

     if score >= 750:
        interest_rate = round(random.uniform(8.0, 9.5), 2)
     elif score >= 700:
        interest_rate = round(random.uniform(9.5, 11.0), 2)
     elif score >= 650:
        interest_rate = round(random.uniform(11.0, 12.5), 2)
     else:
        interest_rate = round(random.uniform(12.5, 14.0), 2)

    elif loan_product == "Education Loan":

     if score >= 750:
        interest_rate = round(random.uniform(8.0, 9.0), 2)
     elif score >= 700:
        interest_rate = round(random.uniform(9.0, 10.5), 2)
     elif score >= 650:
        interest_rate = round(random.uniform(10.5, 12.0), 2)
     else:
        interest_rate = round(random.uniform(12.0, 13.5), 2)

    elif loan_product == "Business Loan":

      if score >= 750:
        interest_rate = round(random.uniform(9.0, 10.5), 2)
      elif score >= 700:
        interest_rate = round(random.uniform(10.5, 12.0), 2)
      elif score >= 650:
        interest_rate = round(random.uniform(12.0, 14.0), 2)
      else:
        interest_rate = round(random.uniform(14.0, 16.0), 2)

    emi = calculate_emi(
        loan_amount,
        interest_rate,
        tenure
    )

    disbursement_date = application["approval_date"]

    maturity_date = disbursement_date + pd.DateOffset(months=tenure)

    # ==========================================
    # Outstanding Balance
    # ==========================================

    today = pd.Timestamp.today().normalize()

    months_elapsed = max(
        0,
        min(
            tenure,
            (today.year - disbursement_date.year) * 12
            + (today.month - disbursement_date.month)
        )
    )

    principal_repaid = emi * months_elapsed

    outstanding_balance = max(
        0,
        round(
            loan_amount - principal_repaid,
            2
        )
    )

    # ==========================================
    # Loan Status
    # ==========================================

    if outstanding_balance <= 0:

        status = "Closed"

    elif profile["previous_defaults"] > 0:

        if random.random() < 0.30:

            status = "Defaulted"

        else:

            status = "Active"

    else:

        status = "Active"

    return {

        "loan_amount": loan_amount,

        "interest_rate": interest_rate,

        "tenure_months": tenure,

        "emi_amount": emi,

        "disbursement_date": disbursement_date,

        "maturity_date": maturity_date,

        "outstanding_balance": outstanding_balance,

        "loan_status": status

    }

def generate_loan_product() -> dict:

    products = {
        "Personal Loan": [
            "Medical Expense",
            "Wedding",
            "Travel",
            "Home Renovation"
        ],
        "Home Loan": [
            "Home Purchase",
            "Home Construction",
            "Home Renovation"
        ],
        "Auto Loan": [
            "New Car",
            "Used Car",
            "Two Wheeler"
        ],
        "Education Loan": [
            "Higher Education",
            "Study Abroad"
        ],
        "Business Loan": [
            "Working Capital",
            "Business Expansion",
            "Equipment Purchase"
        ]
    }

    product = weighted_choice(
        LOAN_PRODUCTS,
        LOAN_PRODUCT_WEIGHTS
    )

    purpose = random.choice(products[product])

    return {
        "loan_product": product,
        "loan_purpose": purpose
    }
