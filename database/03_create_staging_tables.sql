-- ==========================================================
-- Staging Tables
-- Raw data imported from CSV
-- No PK
-- No FK
-- No Constraints
-- ==========================================================

DROP TABLE IF EXISTS staging.loan_raw;
DROP TABLE IF EXISTS staging.payment_raw;

-- ==========================================================
-- Loan Raw
-- ==========================================================

CREATE TABLE staging.loan_raw (

    loan_id VARCHAR(20),
    application_id VARCHAR(20),

    loan_product VARCHAR(50),
    loan_purpose VARCHAR(100),

    first_name VARCHAR(50),
    last_name VARCHAR(50),

    date_of_birth DATE,
    age INT,

    gender VARCHAR(20),
    marital_status VARCHAR(30),
    education_level VARCHAR(50),
    employment_type VARCHAR(50),

    annual_income BIGINT,
    customer_since DATE,

    branch_code VARCHAR(20),
    branch_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    region VARCHAR(50),
    branch_type VARCHAR(30),

    credit_score SMALLINT,
    credit_utilization_pct DECIMAL(5,2),
    debt_to_income_ratio DECIMAL(5,2),
    previous_defaults SMALLINT,
    existing_loan_count SMALLINT,
    existing_debt_amount DECIMAL(15,2),

    application_date DATE,
    requested_amount DECIMAL(15,2),
    requested_tenure_months SMALLINT,
    application_status VARCHAR(30),
    approved_amount DECIMAL(15,2),
    approval_date DATE,
    rejection_reason VARCHAR(100),

    loan_amount DECIMAL(15,2),
    interest_rate DECIMAL(5,2),
    tenure_months SMALLINT,
    emi_amount DECIMAL(15,2),

    disbursement_date DATE,
    maturity_date DATE,

    outstanding_balance DECIMAL(15,2),
    loan_status VARCHAR(30),

    payment_status VARCHAR(30),
    days_past_due SMALLINT,

    default_flag VARCHAR(5),
    default_date DATE,
    default_reason VARCHAR(100),

    recovery_amount DECIMAL(15,2),
    recovery_status VARCHAR(30),
    recovery_method VARCHAR(50),
    recovery_date DATE,

    writeoff_flag VARCHAR(5),
    writeoff_amount DECIMAL(15,2),
    writeoff_reason VARCHAR(100),
    writeoff_date DATE
);

-- ==========================================================
-- Payment Raw
-- ==========================================================

CREATE TABLE staging.payment_raw (

    payment_id VARCHAR(30),
    loan_id VARCHAR(20),

    installment_number SMALLINT,

    due_date DATE,
    payment_date DATE,

    emi_amount DECIMAL(15,2),
    payment_amount DECIMAL(15,2),

    principal_paid DECIMAL(15,2),
    interest_paid DECIMAL(15,2),

    payment_status VARCHAR(30),

    days_past_due SMALLINT,

    payment_mode VARCHAR(30),

    remaining_balance DECIMAL(15,2)

);