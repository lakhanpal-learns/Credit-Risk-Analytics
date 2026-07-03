# Business Context

## Industry Background

Financial institutions issue loans to generate revenue through interest income.

However, lending also introduces credit risk—the possibility that borrowers may fail to repay their obligations.

To remain profitable, banks continuously monitor portfolio performance, customer behavior, delinquency trends, defaults, recoveries, and overall portfolio health.

This project simulates that analytical environment using a realistic synthetic banking dataset.

## Business Problem

Banks approve thousands of loan applications every day.

Without proper monitoring, increasing defaults can lead to significant financial losses.

Business teams need reliable analytical systems that can answer questions such as:

- Which customers are most likely to default?
- Which loan products carry the highest risk?
- Which branches generate high-risk portfolios?
- How much money is currently exposed to default?
- How effective are recovery activities?

Answering these questions requires well-structured, reliable, and integrated data.

## Lending Business Overview
Customer

↓

Loan Application

↓

Credit Assessment

↓

Approval / Rejection

↓

Loan Disbursement

↓

EMI Payments

↓

Delinquency

↓

Default

↓

Recovery

↓

Loan Closure

## Credit Risk Lifecycle

Every loan progresses through a defined lifecycle.

Initially, customers submit loan applications.

Approved applications become active loans.

During repayment, customers make periodic EMI payments.

Missed payments increase Days Past Due (DPD), eventually leading to delinquency and potentially default.

Following default, recovery activities begin.

If recovery is unsuccessful, the remaining balance may be written off.

## Business Objectives

This project aims to help business users:

- Monitor overall portfolio health.
- Identify high-risk customer segments.
- Track delinquency and default trends.
- Measure recovery effectiveness.
- Compare branch performance.
- Compare loan product performance.
- Support data-driven lending decisions.

## Stakeholders
| Stakeholder          | Uses               |
| -------------------- | ------------------ |
| Executive Management | Portfolio KPIs     |
| Credit Risk Team     | Risk Monitoring    |
| Loan Operations      | Loan Performance   |
| Branch Managers      | Branch Performance |
| Recovery Team        | Recovery Tracking  |
| Data Analysts        | SQL & Reporting    |
| Power BI Users       | Dashboards         |

## Business Questions

The project is designed to answer questions such as:

- What is the current portfolio value?
- What is the overall approval rate?
- What is the portfolio default rate?
- Which customer segments have the highest default rate?
- Which loan products contribute most to portfolio risk?
- Which branches generate the highest number of defaults?
- What is the recovery rate?
- What is the current outstanding exposure?
- Which regions require additional monitoring?

## KPIs
| KPI                  | Purpose                  |
| -------------------- | ------------------------ |
| Portfolio Value      | Total lending exposure   |
| Outstanding Balance  | Current exposure         |
| Approval Rate        | Lending efficiency       |
| Default Rate         | Portfolio risk           |
| Delinquency Rate     | Early warning            |
| Recovery Rate        | Collection effectiveness |
| Average Credit Score | Portfolio quality        |
| Write-off Amount     | Financial loss           |
| Branch Performance   | Operational comparison   |
| Product Performance  | Product risk             |


## Success Criteria

The project will be considered successful when it can:

- Generate realistic synthetic banking data.
- Load data into PostgreSQL through an ETL pipeline.
- Maintain referential integrity across warehouse tables.
- Support analytical SQL queries.
- Deliver interactive Power BI dashboards.
- Produce actionable business insights based on portfolio performance.
