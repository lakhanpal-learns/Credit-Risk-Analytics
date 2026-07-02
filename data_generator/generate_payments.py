import pandas as pd

from services.payment import generate_payment_schedule

# ===============================
# Load Loan Dataset
# ===============================

loans = pd.read_csv("../data/credit_risk_loans.csv")

payments = []

payment_counter = 1

# ===============================
# Generate Payment History
# ===============================

for _, loan in loans.iterrows():

    # Skip rejected applications
    if pd.isna(loan["loan_amount"]):
        continue

    payment_schedule, payment_counter = generate_payment_schedule(
        loan,
        payment_counter
    )

    payments.extend(payment_schedule)

# ===============================
# Export
# ===============================

payment_df = pd.DataFrame(payments)

payment_df.to_csv(
    "../data/loan_payments.csv",
    index=False
)

print(payment_df.head())

print()
print(payment_df.shape)