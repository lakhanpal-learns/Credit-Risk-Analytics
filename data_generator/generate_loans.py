import random
from datetime import date

import pandas as pd
from faker import Faker

from config import *
from utils import *



# generate the ids
from services.ids import generate_ids

# genrate the brach 
from services.branch import generate_branch

# generate the credit profile 

from services.credit_profile import generate_credit_profile

# generate the customer 
from services.customer import generate_customer


# generate the application
from services.application import generate_application

# generate loan and loan product
from services.loan import (
    generate_loan,
    generate_loan_product
)

# generate the risk outcome ,recovery deatils ,write_off_deatails
from services.risk import (
    generate_risk_outcome,
    generate_recovery_details,
    generate_writeoff_details
)

def build_dataset():

    records = []

    for loan_number in range(1, TOTAL_LOANS + 1):

        # Generate IDs
        ids = generate_ids(loan_number)

        # Loan Product & Purpose
        product = generate_loan_product()

        # Customer
        customer = generate_customer()

        # Branch
        branch = generate_branch()

        # Credit Profile
        profile = generate_credit_profile(customer)

        # Loan Application
        application = generate_application(customer,profile, product,branch)

        # Loan
        loan = generate_loan( application, profile,product)

        row = {}

        # Merge all available data
        row.update(ids)
        row.update(product)
        row.update(customer)
        row.update(branch)
        row.update(profile)
        row.update(application)

        if loan is not None:

            row.update(loan)

            risk = generate_risk_outcome(
                loan,
                customer["employment_type"]
            )

            row.update(loan)
            row.update(risk)

            recovery = generate_recovery_details(risk)
            row.update(recovery)

            writeoff = generate_writeoff_details({
                **risk,
                **recovery
            })
            row.update(writeoff)

        records.append(row)

    df = pd.DataFrame(records)

    return df

def main():

    random.seed(RANDOM_SEED)

    dataset = build_dataset()

    save_csv(
        dataset,
        f"{OUTPUT_PATH}/credit_risk_loans.csv"
    )

    print(dataset.head())

    print(dataset.shape)


if __name__ == "__main__":
    main()