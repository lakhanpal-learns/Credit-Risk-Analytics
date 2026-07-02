# Credit Risk Analytics Project

## Development Progress Log

**Date:** July 2026

---

# Phase 1 — Data Generation (Completed)

## Objective

Build a realistic synthetic banking dataset that follows real-world credit risk business rules instead of generating random values.

---

# Architecture Refactoring

Initially, all business logic was written inside one file.

The project was refactored into a modular service architecture.

Current structure:

```
data_generator/

├── generate_loans.py
├── generate_payments.py
│
├── services/
│   ├── ids.py
│   ├── customer.py
│   ├── branch.py
│   ├── credit_profile.py
│   ├── application.py
│   ├── loan.py
│   ├── risk.py
│   └── payment.py
```

Each module is responsible for its own business logic.

---

# Modules Completed

## 1. Customer

Implemented realistic customer generation.

Business rules applied:

- Age between 21–70
- Employment type distribution
- Education level
- Annual income
- Customer since date
- Gender
- Marital status

Improvement:

- Customer Since date is always earlier than the Application Date.

Status:

```
Completed
```

---

## 2. Branch

Implemented branch information.

Business rules:

- Branch Code
- Branch Name
- City
- State
- Region
- Branch Type

Status:

```
Completed
```

---

## 3. Credit Profile

Implemented realistic customer credit profile.

Business rules:

- Credit Score
- Credit Utilization
- Debt-to-Income Ratio
- Previous Defaults
- Existing Loan Count
- Existing Debt Amount

Relationships created between:

Income

↓

Existing Debt

↓

DTI

↓

Credit Score

Status:

```
Completed
```

---

## 4. Loan Application

Implemented complete loan approval engine.

Business rules include:

- Product-based requested amount
- Product-based tenure
- Income eligibility
- Eligibility multiplier
- DTI adjustment
- Credit Score policy
- Previous Default policy
- Requested Amount eligibility
- Approval Amount calculation
- Approval Date
- Rejection Reason

Application decisions are no longer random.

Status:

```
Completed
```

---

## 5. Loan

Implemented loan generation.

Business rules:

- Product-specific interest rates
- Credit Score based pricing
- EMI calculation
- Loan Status
- Outstanding Balance
- Disbursement Date
- Maturity Date

Status:

```
Completed
```

---

## 6. Risk

Implemented complete risk engine.

Business rules:

- Payment Status
- Days Past Due
- Default Flag
- Default Date
- Default Reason
- Recovery Amount
- Recovery Status
- Write-off Flag
- Write-off Amount
- Recovery Method
- Recovery Date
- Write-off Reason
- Write-off Date

Employment type now influences Default Reason.

Status:

```
Completed
```

---

## 7. Payment History

Created a separate transactional dataset.

Output:

```
loan_payments.csv
```

Implemented:

- Payment ID
- Loan ID
- Installment Number
- Due Date
- Payment Date
- EMI Amount
- Payment Amount
- Principal Paid
- Interest Paid
- Payment Status
- Days Past Due
- Payment Mode
- Remaining Balance

Improvements made:

- Unique Payment IDs
- No future payment records
- Closed loans always finish with zero remaining balance

Status:

```
Completed
```

---

# Generated Datasets

Current output:

```
credit_risk_loans.csv

loan_payments.csv
```

These datasets are fully linked using:

```
loan_id
```

Relationship:

```
credit_risk_loans

1

↓

Many

loan_payments
```

---

# Testing Completed

Validation performed on generated data.

Verified:

- Customer dates
- Application dates
- Loan approval logic
- Interest rates
- EMI calculations
- Risk generation
- Recovery logic
- Payment history
- Remaining balances
- Date sequence consistency
- Foreign key relationships

Critical issues fixed during testing.

---

# Current Project Status

```
Data Generation

██████████████████████████████

100% Completed
```

---

# Major Achievement

The project now produces realistic synthetic banking data suitable for:

- SQL
- PostgreSQL
- Power BI
- Data Engineering
- Credit Risk Analytics

instead of simple random datasets.

---

# Next Phase

## Database Engineering

The next decision is **not** to create more CSV files.

Instead, the project will follow a production-style ETL pipeline.

```
CSV Files

↓

PostgreSQL Staging Tables

↓

SQL Normalization

↓

ER Model Tables

↓

Analytics

↓

Power BI Dashboard
```

---

# Planned Database Design

The wide datasets will be transformed into a normalized relational model.

Target tables:

```
Customer

Branch

Credit_Profile

Application

Loan

Risk

Recovery

Writeoff

Loan_Payment

Loan_Product
```

Primary and foreign keys will be created using PostgreSQL.

---

# Why This Approach?

Instead of generating many CSV files directly, the project will simulate a real-world banking data engineering workflow.

Raw operational data

↓

Database staging

↓

Normalization

↓

Analytics

↓

Visualization

This demonstrates both Data Engineering and Data Analytics skills.

---

# Next Milestone

Phase 2

PostgreSQL Data Warehouse

Tasks:

- Create database schema
- Create normalized tables
- Define primary keys
- Define foreign keys
- Load staging CSVs
- Normalize data using SQL
- Validate relationships

After completion:

- Analytical SQL Queries
- Power BI Dashboard
- Project Documentation
- Portfolio Deployment

---

## Overall Progress

```
Phase 1
Synthetic Data Generation

██████████████████████████████

Completed

Phase 2
Database Engineering

□□□□□□□□□□□□□□

Next
```