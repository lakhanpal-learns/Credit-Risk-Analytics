# Portfolio Assumptions

## Document Information

| Attribute | Details |
|------------|---------|
| Project | Credit Risk Analytics Platform |
| Document | Portfolio Assumptions |
| Version | 1.0 |
| Author | Lakhanpal |
| Status | In Progress |

---

# 1. Purpose

The Credit Risk Analytics Platform uses synthetic data instead of production banking data. Since no real customer or loan information is available, portfolio assumptions are required to simulate a realistic retail lending environment.

These assumptions define the expected characteristics of the lending portfolio and guide the synthetic data generation process. They ensure that the generated data reflects common banking practices while remaining suitable for analytics, SQL reporting, ETL processing, and business intelligence dashboards.

These assumptions influence:

- Customer generation
- Credit profile generation
- Loan applications
- Loan approvals
- Loan performance
- Payment behavior
- Default behavior
- Recovery activities
- Portfolio analytics

---

# 2. Portfolio Overview

| Assumption | Value |
|------------|------|
| Portfolio Type | Retail Lending Portfolio |
| Industry | Banking / Financial Services |
| Currency | Indian Rupee (INR) |
| Geographic Scope | Multiple States and Cities in India |
| Initial Portfolio Size | 10,000 Customers |
| Target Portfolio Size | 100,000+ Customers |
| Loan Products | Personal, Home, Auto, Education, Business |
| Reporting Period | Multi-Year Lending Portfolio |

---

# 3. Customer Portfolio Assumptions

The portfolio represents a diverse customer base with different demographic and financial characteristics.

| Assumption | Description |
|------------|-------------|
| Customer Age | Between 21 and 70 years |
| Average Customer Age | Majority between 25 and 55 years |
| Gender Distribution | Male and Female customers |
| Employment Types | Salaried, Self-Employed, Government Employee, Business Owner, Retired |
| Income Groups | Low, Medium and High income categories |
| Returning Customers | Existing customers may apply for multiple loans |
| Customer Registration | Every customer is registered before submitting a loan application |

---

# 4. Branch Portfolio Assumptions

The simulated bank operates through multiple branches.

| Assumption | Description |
|------------|-------------|
| Branch Coverage | Multiple branches across India |
| Branch Types | Urban, Semi-Urban and Rural |
| Geographic Hierarchy | Branch → City → State → Region |
| Loan Processing | Every application is processed by one branch |
| Branch Performance | Loan volume differs across branches |

---

# 5. Credit Portfolio Assumptions

Credit profiles are designed to reflect realistic customer financial behavior.

| Assumption | Description |
|------------|-------------|
| Credit Score Range | 300–850 |
| Majority Credit Scores | Between 650 and 800 |
| Credit Utilization | Between 0% and 100% |
| Debt-to-Income Ratio | Majority below 50% |
| Existing Loan Count | Varies by customer |
| Existing Debt | Depends on borrowing history |
| Previous Defaults | Only a small percentage of customers |

---

# 6. Loan Portfolio Assumptions

Loan characteristics represent a typical retail lending portfolio.

| Assumption | Description |
|------------|-------------|
| Loan Products | Personal, Home, Auto, Education and Business Loans |
| Loan Amount | Depends on customer income and loan product |
| Interest Rate | Depends on customer risk profile |
| Loan Tenure | 12, 24, 36, 48 and 60 months |
| EMI Frequency | Monthly |
| Loan Approval Rate | Majority of applications are approved |
| Loan Rejection Rate | Minority of applications are rejected |

---

# 7. Payment Portfolio Assumptions

Repayment behavior is generated using realistic payment patterns.

| Assumption | Description |
|------------|-------------|
| EMI Frequency | Monthly |
| Installments | Equal to loan tenure |
| Majority Payments | Paid on time |
| Late Payments | Small percentage |
| Missed Payments | Limited to higher-risk customers |
| Payment Modes | UPI, Net Banking, Auto Debit, Debit Card, Cash, Cheque |
| Remaining Balance | Decreases after every successful payment |

---

# 8. Default Portfolio Assumptions

Default events follow realistic lending behavior rather than random generation.

| Assumption | Description |
|------------|-------------|
| Portfolio Default Rate | Small percentage of total loans |
| High Risk Customers | More likely to default |
| Credit Score Impact | Lower scores increase default probability |
| DTI Impact | Higher DTI increases default probability |
| Previous Defaults | Increase future default risk |
| Payment Behavior | Multiple missed payments may lead to default |
| Default Reasons | Financial Hardship, Job Loss, Business Failure, Medical Emergency |

---

# 9. Recovery Portfolio Assumptions

Recovery activities begin after a loan defaults.

| Assumption | Description |
|------------|-------------|
| Recovery Trigger | Loan Default |
| Recovery Types | Partial Recovery and Full Recovery |
| Recovery Methods | Settlement, Collection Agency, Legal Action |
| Recovery Success | Depends on customer profile |
| Recovery Amount | Cannot exceed outstanding balance |
| Recovery Date | Always after default date |

---

# 10. Write-off Portfolio Assumptions

Write-offs represent unrecoverable loan losses.

| Assumption | Description |
|------------|-------------|
| Write-off Eligibility | Recovery attempts unsuccessful |
| Portfolio Percentage | Small percentage of defaulted loans |
| Write-off Amount | Remaining outstanding balance |
| Write-off Reasons | Insolvency, Fraud, Deceased Borrower, Untraceable Customer |
| Write-off Date | Occurs after recovery process |

---

# 11. Portfolio Growth Assumptions

The project is designed to support increasing portfolio sizes during development.

| Development Stage | Portfolio Size |
|-------------------|---------------|
| Initial Development | 10,000 Customers |
| Functional Testing | 25,000 Customers |
| Performance Testing | 50,000 Customers |
| Final Portfolio | 100,000+ Customers |

---

# 12. Analytical Assumptions

The generated portfolio is expected to support business analytics.

The synthetic dataset should produce meaningful trends for:

- Portfolio Growth Analysis
- Customer Risk Segmentation
- Credit Score Distribution
- Loan Product Performance
- Branch Performance
- Default Trend Analysis
- Delinquency Monitoring
- Recovery Analysis
- Exposure Analysis
- Executive KPI Reporting

---

# 13. Project Limitations

The generated portfolio is intended for educational and analytical purposes only.

The assumptions do not represent the lending policies of any specific financial institution.

Customer behavior, approval decisions, default probabilities, and recovery outcomes are simplified to demonstrate realistic business scenarios while maintaining manageable project complexity.

---

# 14. Assumption Summary

| Category | Objective |
|----------|-----------|
| Customer | Simulate realistic borrower demographics |
| Branch | Simulate geographically distributed lending |
| Credit Profile | Represent customer financial health |
| Loan | Model realistic lending products |
| Payment | Simulate repayment behavior |
| Default | Model portfolio credit risk |
| Recovery | Represent post-default collection activities |
| Write-off | Simulate final credit losses |
| Portfolio Growth | Support scalability testing |

---

# Conclusion

The portfolio assumptions defined in this document establish the foundation for the synthetic lending portfolio used throughout the Credit Risk Analytics Platform.

These assumptions guide the Python data generation process, support ETL validation, maintain consistency across the PostgreSQL warehouse, and enable meaningful SQL analysis and Power BI reporting.

By defining portfolio characteristics before implementation, the project follows a business-first design approach that closely resembles the planning process used in enterprise data engineering and analytics projects.