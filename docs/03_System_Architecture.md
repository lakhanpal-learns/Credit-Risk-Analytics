# System Architecture

## Overview

The Credit Risk Analytics Platform follows a layered architecture that separates data generation, data storage, transformation, analytics, and visualization.

Each layer has a clearly defined responsibility, making the system modular, maintainable, and scalable.

Instead of directly analyzing generated datasets, the project follows a production-inspired ETL workflow where raw data is staged, validated, transformed into a normalized warehouse, and finally consumed by reporting tools.

## System Components
| Layer              | Responsibility                    |
| ------------------ | --------------------------------- |
| Business Rules     | Define banking logic              |
| Data Generator     | Generate realistic synthetic data |
| Raw Data           | Store CSV outputs                 |
| PostgreSQL Staging | Load raw files                    |
| Validation         | Check data quality                |
| Warehouse          | Store normalized tables           |
| SQL Analytics      | Business queries                  |
| Analytics Views    | Simplify reporting                |
| Power BI           | Dashboards                        |
| Documentation      | Explain the system                |


## Data Flow
Business Rules
        │
        ▼
Python Generator
        │
        ▼
Raw CSV Files
        │
        ▼
PostgreSQL Staging
        │
        ▼
Data Validation
        │
        ▼
SQL Transformation
        │
        ▼
Warehouse
        │
        ▼
Analytics Views
        │
        ▼
Power BI Dashboard

## Project Layers

### Layer 1 — Business Layer

#### Contains:

Business assumptions
Business rules
Credit risk concepts

#### Purpose:
Defines how banking data should behave.

### Layer 2 — Data Generation

#### Contains:

Python services.

#### Purpose:

Generate realistic banking data.

#### Output:
credit_risk_loans.csv

loan_payments.csv


### Layer 3 — Data Storage

#### Contains:

Raw datasets.

#### Purpose:

Store generated operational data before loading into PostgreSQL.

### Layer 4 — ETL

#### Contains:

Staging
Validation
Transformation

#### Purpose:

Convert raw operational data into relational tables.

### Layer 5 — Warehouse

#### Contains:

Normalized tables.

#### Purpose:

Support analytics.

### Layer 6 — Analytics

#### Contains:

SQL.
Views.
KPIs.

#### Purpose:
Business reporting.

### Layer 7 — Visualization

#### Contains:
Power BI.

#### Purpose:
Decision support.

## Technology Responsibilities

| Technology | Responsibility            |
| ---------- | ------------------------- |
| Python     | Generate synthetic data   |
| Pandas     | CSV processing            |
| PostgreSQL | Data warehouse            |
| SQL        | Transformation & analysis |
| Git        | Version control           |
| Power BI   | Reporting                 |
| VS Code    | Development               |


## Folder Architecture
credit-risk-analytics/

data_generator/

datasets/

database/

sql/

powerbi/

docs/

README.md

## Design Decisions

### Decision 1

Why generate synthetic data?

Answer:

Public datasets don't model the complete lending lifecycle or support controlled business rules.

### Decision 2

Why PostgreSQL?

Answer:

Supports relational modeling, constraints, indexing, and analytical SQL.

### Decision 3

Why a staging schema?

Answer:

Raw operational data should be isolated from production warehouse tables.

### Decision 4

Why normalize?

Answer:

Reduce redundancy, improve integrity, and support scalable analytics.

### Decision 5
Why Power BI?

Answer:

Interactive business reporting.

## Non-Functional Considerations

| Requirement     | Decision                       |
| --------------- | ------------------------------ |
| Scalability     | Designed for 100k+ customers   |
| Maintainability | Modular Python services        |
| Extensibility   | New loan products can be added |
| Data Integrity  | Warehouse constraints          |
| Performance     | Indexes on PK/FK               |
| Reusability     | Separate ETL scripts           |

## Current Architecture Status
Current implementation status:

✅ Business Rules

✅ Portfolio Assumptions

✅ Data Generator

✅ CSV Generation

✅ PostgreSQL Setup

✅ Database Schemas

✅ Staging Tables

⏳ Raw Data Loading

⏳ Validation

⏳ Warehouse

⏳ Analytics

⏳ Power BI

## Future Architecture
CSV

↓

Staging

↓

Validation

↓

Warehouse

↓

Views

↓

Power BI

↓

Deployment
