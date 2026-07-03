# Business Rules

## Document Information

| Attribute | Details |
|------------|---------|
| Project | Credit Risk Analytics Platform |
| Document | Business Rules |
| Version | 1.0 |
| Author | Lakhanpal |
| Status | In Progress |

---

# 1. Introduction

## Purpose

The purpose of this document is to define the business rules used throughout the Credit Risk Analytics Platform.

Unlike projects that rely on publicly available datasets, this platform generates synthetic banking data using realistic lending policies and business constraints.

These rules ensure that customer profiles, loan applications, loan approvals, repayments, defaults, recoveries, and write-offs behave consistently and support meaningful analytical reporting.

The rules described in this document guide:

- Synthetic Data Generation
- ETL Validation
- SQL Analytics
- Power BI Dashboards
- Business KPI Calculation

---

# 2. Business Rule Design Principles

The project follows five design principles.

## 2.1 Realistic

Generated data should resemble a real retail lending portfolio.

Example

- High credit score customers should generally have lower default probability.
- Low income customers should have higher average debt-to-income ratios.

---

## 2.2 Consistent

Relationships between entities must always remain valid.

Example

Application Date

↓

Approval Date

↓

Disbursement Date

↓

Payment Due Date

↓

Default

↓

Recovery

↓

Write-off

---

## 2.3 Analytical

Rules should generate patterns that can later be discovered through SQL and Power BI.

Example

Credit Score ↓

↓

Default Rate ↑

---

## 2.4 Modular

Each business rule should affect only one business process whenever possible.

---

## 2.5 Extensible

New loan products, customer types, or risk models can be added without redesigning the platform.

---

# 3. Customer Rules

Customer represents an individual borrower.

| Rule ID     | Business Rule     | Description                                                     | Expected Behavior                                                     |
| ----------- | ----------------- | --------------------------------------------------------------- | --------------------------------------------------------------------- |
| BR-CUST-001 | Customer Age      | Customer age must be between 21 and 70 years.                   | Customers outside this range are not generated.                       |
| BR-CUST-002 | Employment Type   | Employment type must be one of the predefined categories.       | Salaried, Self-Employed, Business Owner, Government Employee, Retired |
| BR-CUST-003 | Annual Income     | Income depends on employment type.                              | Higher income generally supports larger loan approvals.               |
| BR-CUST-004 | Customer Since    | Customer registration date must be before any loan application. | Ensures valid customer history.                                       |
| BR-CUST-005 | Customer Identity | Every customer must have a unique Customer ID.                  | No duplicate customers.                                               |

---

# 4. Branch Rules

Branches represent loan originating locations.

| Rule ID     | Business Rule     | Description                                                     | Expected Behavior                                                     |
| ----------- | ----------------- | --------------------------------------------------------------- | --------------------------------------------------------------------- |
| BR-CUST-001 | Customer Age      | Customer age must be between 21 and 70 years.                   | Customers outside this range are not generated.                       |
| BR-CUST-002 | Employment Type   | Employment type must be one of the predefined categories.       | Salaried, Self-Employed, Business Owner, Government Employee, Retired |
| BR-CUST-003 | Annual Income     | Income depends on employment type.                              | Higher income generally supports larger loan approvals.               |
| BR-CUST-004 | Customer Since    | Customer registration date must be before any loan application. | Ensures valid customer history.                                       |
| BR-CUST-005 | Customer Identity | Every customer must have a unique Customer ID.                  | No duplicate customers.                                               |


---

# 5. Credit Profile Rules

Credit Profile stores financial risk information.

| Rule ID       | Business Rule        | Description                                           | Expected Behavior                           |
| ------------- | -------------------- | ----------------------------------------------------- | ------------------------------------------- |
| BR-CREDIT-001 | Credit Score         | Credit score must be between 300 and 850.             | Realistic credit scoring.                   |
| BR-CREDIT-002 | Credit Utilization   | Credit utilization must remain between 0% and 100%.   | Invalid utilization values are not allowed. |
| BR-CREDIT-003 | Debt-to-Income Ratio | DTI must remain between 0% and 100%.                  | Used for affordability analysis.            |
| BR-CREDIT-004 | Existing Loan Count  | Existing loan count cannot be negative.               | Valid customer borrowing history.           |
| BR-CREDIT-005 | Existing Debt        | Existing debt amount cannot be negative.              | Prevents invalid balances.                  |
| BR-CREDIT-006 | Previous Defaults    | Previous defaults cannot exceed total existing loans. | Maintains logical consistency.              |

---

# 6. Loan Application Rules

Loan Application represents a customer's request before approval.

| Rule ID    | Business Rule         | Description                                          | Expected Behavior              |
| ---------- | --------------------- | ---------------------------------------------------- | ------------------------------ |
| BR-APP-001 | Application Date      | Must occur after customer registration.              | Valid application timeline.    |
| BR-APP-002 | Requested Amount      | Requested loan amount must be positive.              | No negative or zero requests.  |
| BR-APP-003 | Application Status    | Status must be Approved or Rejected.                 | Standard application outcome.  |
| BR-APP-004 | Approval Date         | Approval date must be after application date.        | Logical approval workflow.     |
| BR-APP-005 | Approved Amount       | Approved amount cannot exceed requested amount.      | Partial approvals are allowed. |
| BR-APP-006 | Rejected Applications | Rejected applications do not create loans.           | Loan record is not generated.  |
| BR-APP-007 | Approved Applications | Every approved application creates exactly one loan. | One-to-one relationship.       |

---

# 7. Loan Rules

| Rule ID     | Business Rule       | Description                                       | Expected Behavior             |
| ----------- | ------------------- | ------------------------------------------------- | ----------------------------- |
| BR-LOAN-001 | Loan Amount         | Loan amount must be greater than zero.            | Valid lending amount.         |
| BR-LOAN-002 | Interest Rate       | Interest rate must be positive.                   | No negative interest.         |
| BR-LOAN-003 | Loan Tenure         | Loan tenure must follow supported durations.      | 12, 24, 36, 48, 60 months.    |
| BR-LOAN-004 | EMI Calculation     | EMI is calculated using amount, rate, and tenure. | Consistent monthly repayment. |
| BR-LOAN-005 | Disbursement Date   | Loan is disbursed after approval.                 | Correct loan lifecycle.       |
| BR-LOAN-006 | Maturity Date       | Maturity occurs after disbursement.               | Valid loan duration.          |
| BR-LOAN-007 | Outstanding Balance | Outstanding balance cannot be negative.           | Prevents invalid balances.    |
| BR-LOAN-008 | Loan Status         | Loan status must be predefined.                   | Active, Closed, Defaulted     |

# 8. Payment Rules

Each row represents one EMI payment.

| Rule ID    | Business Rule       | Description                                           | Expected Behavior                           |
| ---------- | ------------------- | ----------------------------------------------------- | ------------------------------------------- |
| BR-PAY-001 | Payment Generation  | Every approved loan generates multiple EMI payments.  | One payment per installment.                |
| BR-PAY-002 | Installment Number  | Installments start at 1 and end at loan tenure.       | Sequential numbering.                       |
| BR-PAY-003 | Due Date            | Due dates occur monthly after disbursement.           | Monthly repayment schedule.                 |
| BR-PAY-004 | Payment Status      | Payment status follows predefined values.             | Paid, Partial, Late, Missed                 |
| BR-PAY-005 | Remaining Balance   | Remaining balance decreases after successful payment. | Running balance maintained.                 |
| BR-PAY-006 | Days Past Due (DPD) | DPD depends on payment behavior.                      | Paid=0, Late=1–30, Partial=1–60, Missed=90+ |
| BR-PAY-007 | Payment Mode        | Payment mode follows supported methods.               | UPI, Net Banking, Auto Debit, Cash, Cheque  |


---

# 9. Default Rules

| Rule ID    | Business Rule   | Description                                            | Expected Behavior                                                 |
| ---------- | --------------- | ------------------------------------------------------ | ----------------------------------------------------------------- |
| BR-DEF-001 | Default Trigger | Default occurs after significant delinquency.          | Based on payment behavior.                                        |
| BR-DEF-002 | Default Flag    | Default flag must be Yes or No.                        | Indicates loan default status.                                    |
| BR-DEF-003 | Default Date    | Default date occurs after missed payments.             | Correct event sequence.                                           |
| BR-DEF-004 | Default Reason  | Default reason is selected from predefined categories. | Financial Hardship, Job Loss, Business Failure, Medical Emergency |


---

# 10. Recovery Rules

Recovery begins only after default.

| Rule ID    | Business Rule   | Description                                            | Expected Behavior                                                 |
| ---------- | --------------- | ------------------------------------------------------ | ----------------------------------------------------------------- |
| BR-DEF-001 | Default Trigger | Default occurs after significant delinquency.          | Based on payment behavior.                                        |
| BR-DEF-002 | Default Flag    | Default flag must be Yes or No.                        | Indicates loan default status.                                    |
| BR-DEF-003 | Default Date    | Default date occurs after missed payments.             | Correct event sequence.                                           |
| BR-DEF-004 | Default Reason  | Default reason is selected from predefined categories. | Financial Hardship, Job Loss, Business Failure, Medical Emergency |

---

# 11. Write-off Rules

## Rule W-01

Write-off occurs only if recovery efforts fail.

---

## Rule W-02

Write-off Amount

Cannot exceed remaining balance.

---

## Rule W-03

Write-off Dater

| Rule ID   | Business Rule         | Description                                        | Expected Behavior                                 |
| --------- | --------------------- | -------------------------------------------------- | ------------------------------------------------- |
| BR-WO-001 | Write-off Eligibility | Write-off occurs only after unsuccessful recovery. | Final loan closure.                               |
| BR-WO-002 | Write-off Amount      | Write-off amount cannot exceed remaining balance.  | Prevents invalid losses.                          |
| BR-WO-003 | Write-off Date        | Write-off occurs after recovery attempts.          | Valid event sequence.                             |
| BR-WO-004 | Write-off Reason      | Write-off reason follows predefined categories.    | Insolvency, Fraud, Deceased, Untraceable Borrower |


---

# 12. Cross-Entity Rules

| Rule ID    | Relationship               | Business Rule                                      | Expected Behavior |
| ---------- | -------------------------- | -------------------------------------------------- | ----------------- |
| BR-REL-001 | Customer → Application     | One customer can submit multiple applications.     | One-to-Many       |
| BR-REL-002 | Customer → Credit Profile  | Every customer has one credit profile.             | One-to-One        |
| BR-REL-003 | Branch → Application       | One branch processes many applications.            | One-to-Many       |
| BR-REL-004 | Loan Product → Application | One product can have many applications.            | One-to-Many       |
| BR-REL-005 | Application → Loan         | Approved application creates exactly one loan.     | One-to-One        |
| BR-REL-006 | Loan → Payment             | One loan generates many payment records.           | One-to-Many       |
| BR-REL-007 | Loan → Default             | A loan can default at most once.                   | Zero-or-One       |
| BR-REL-008 | Default → Recovery         | Recovery exists only after default.                | Zero-or-One       |
| BR-REL-009 | Recovery → Write-off       | Write-off occurs only after unsuccessful recovery. | Zero-or-One       |

---

# 13. Business Rule Validation

The ETL pipeline validates all generated data before loading it into the warehouse.

| Validation              | Rule                                                                              |
| ----------------------- | --------------------------------------------------------------------------------- |
| Duplicate Check         | Customer ID, Application ID, Loan ID, Payment ID must be unique where applicable. |
| Null Check              | Mandatory fields cannot be NULL.                                                  |
| Date Validation         | Application < Approval < Disbursement < Maturity                                  |
| Numeric Validation      | Loan Amount, EMI, Interest Rate, Outstanding Balance ≥ 0                          |
| Credit Score Validation | Score must be between 300–850                                                     |
| DTI Validation          | DTI must be between 0–100%                                                        |
| Payment Validation      | Payment cannot occur before due date generation.                                  |
| Recovery Validation     | Recovery date must be after default date.                                         |
| Write-off Validation    | Write-off date must be after recovery process.                                    |


Records that violate business rules are identified during the staging validation process before transformation into warehouse tables.

---

# 14. Rule Classification

| Category | Rule Type |
|-----------|-----------|
| Customer | Validation |
| Branch | Validation |
| Credit Profile | Validation + Calculation |
| Loan Application | Decision |
| Loan | Calculation |
| Payment | Calculation |
| Default | Decision |
| Recovery | Decision |
| Write-off | Decision |

---

# 15. Summary

The Business Rules defined in this document ensure that the generated lending portfolio behaves consistently across all stages of the project.

These rules drive:

- Synthetic Data Generation
- Data Validation
- ETL Processing
- Warehouse Integrity
- SQL Analytics
- Power BI Dashboards
- Business Recommendations

Following these rules enables the platform to simulate a realistic retail lending environment suitable for demonstrating data engineering, analytics, and business intelligence workflows.