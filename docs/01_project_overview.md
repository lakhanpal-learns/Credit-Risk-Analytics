# Credit Risk Analytics Platform

## Overview

The Credit Risk Analytics Platform is an end-to-end data analytics and data engineering project that simulates the lifecycle of a retail lending portfolio.

The project combines synthetic data generation, PostgreSQL data warehousing, SQL analytics, and Power BI dashboards to demonstrate how financial institutions manage, monitor, and analyze credit risk.

Instead of relying on publicly available datasets, the project generates realistic banking data using business-driven rules, then processes that data through a production-inspired ETL pipeline before presenting analytical insights through interactive dashboards.

## Problem Statement

Many portfolio projects analyze static datasets downloaded from public sources.

While these projects demonstrate visualization and analysis skills, they rarely represent how data is produced, validated, transformed, and consumed in enterprise environments.

This project addresses that gap by building an end-to-end analytics platform that simulates the complete data lifecycle of a banking credit portfolio.

The project focuses not only on reporting but also on data modeling, business rules, ETL design, warehouse construction, and analytical reporting.

## Project Objectives

The primary objectives of this project are:

- Design a realistic banking data model.
- Generate synthetic credit risk data using business rules.
- Build a PostgreSQL-based data warehouse.
- Develop an ETL pipeline for loading and transforming data.
- Perform analytical SQL on the warehouse.
- Build interactive Power BI dashboards.
- Produce business insights and recommendations.

## Project Scope

The project covers the following areas:

- Synthetic Data Generation
- Relational Data Modeling
- ETL Pipeline Development
- PostgreSQL Data Warehouse
- SQL Analytics
- Credit Risk Metrics
- Business Intelligence Dashboards
- Technical Documentation

## System Overview
Python Generator

↓

CSV

↓

PostgreSQL Staging

↓

Validation

↓

Warehouse

↓

Analytics Views

↓

Power BI

## Technology Stack

| Category        | Technology |
| --------------- | ---------- |
| Language        | Python     |
| Database        | PostgreSQL |
| Query Language  | SQL        |
| Data Processing | Pandas     |
| Visualization   | Power BI   |
| Version Control | Git        |
| IDE             | VS Code    |


## High-Level Architecture
Business Rules
       │
       ▼
Synthetic Data Generator
       │
       ▼
Raw CSV Files
       │
       ▼
Staging Database
       │
       ▼
Data Validation
       │
       ▼
Warehouse Tables
       │
       ▼
SQL Analytics
       │
       ▼
Power BI Dashboard

## Project Phases
| Phase                     | Status |
| ------------------------- | ------ |
| Business Understanding    | ✅      |
| Data Modeling             | ✅      |
| Business Rules            | ✅      |
| Portfolio Assumptions     | ✅      |
| Synthetic Data Generation | ✅      |
| PostgreSQL Setup          | ✅      |
| Staging Layer             | ✅      |
| Data Validation           | ⏳      |
| Warehouse Design          | ⏳      |
| SQL Analytics             | ⏳      |
| Power BI Dashboard        | ⏳      |
| Documentation             | 🚧     |

## Current Status

The project has successfully completed the design and data generation phases.

The PostgreSQL environment has been configured, database schemas have been created, and staging tables have been designed to support the ETL pipeline.

The next milestone is implementing the data loading and validation processes before transforming raw data into a normalized warehouse model.

## Repository Structure
credit-risk-analytics/

├── data_generator/
├── datasets/
├── database/
├── sql/
├── powerbi/
├── docs/
└── README.md

## Future Roadmap
Next Steps

✔ Load raw CSV into staging

↓

✔ Validate data quality

↓

✔ Build warehouse tables

↓

✔ Transform data

↓

✔ SQL Analytics

↓

✔ Power BI Dashboard

↓

✔ Documentation

↓

✔ Portfolio Deployment

