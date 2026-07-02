"""
=========================================
Credit Risk Analytics Project
Configuration File
=========================================
"""

# =========================================
# Dataset Size
# =========================================

TOTAL_LOANS = 10

# =========================================
# Time Range
# =========================================

START_YEAR = 2018
END_YEAR = 2026

# =========================================
# Branch Configuration
# =========================================

TOTAL_BRANCHES = 30

# =========================================
# Loan Products
# =========================================

LOAN_PRODUCTS = [
    "Personal Loan",
    "Home Loan",
    "Auto Loan",
    "Education Loan",
    "Business Loan"
]

# Portfolio Distribution
LOAN_PRODUCT_WEIGHTS = [
    0.40,
    0.30,
    0.15,
    0.10,
    0.05
]

# =========================================
# Loan Status
# =========================================

LOAN_STATUS = [
    "Active",
    "Closed",
    "Defaulted"
]

LOAN_STATUS_WEIGHTS = [
    0.65,
    0.25,
    0.10
]

# =========================================
# Application Status
# =========================================

APPLICATION_STATUS = [
    "Approved",
    "Rejected",
    "Pending",
    "Cancelled"
]

APPLICATION_STATUS_WEIGHTS = [
    0.75,
    0.18,
    0.05,
    0.02
]

# =========================================
# Payment Status
# =========================================

PAYMENT_STATUS = [
    "Paid",
    "Late",
    "Missed",
    "Partial"
]

PAYMENT_STATUS_WEIGHTS = [
    0.82,
    0.10,
    0.05,
    0.03
]

# =========================================
# Customer
# =========================================

GENDERS = ["Male", "Female", "Other"]

EMPLOYMENT_TYPES = [
    "Salaried",
    "Self-employed",
    "Business Owner",
    "Retired"
]

EMPLOYMENT_WEIGHTS = [
    0.65,
    0.20,
    0.10,
    0.05
]

# =========================================
# Output
# =========================================

OUTPUT_PATH = "../data"
RANDOM_SEED = 42