# Data Model

## Introduction

The data model defines the logical structure of the Credit Risk Analytics Platform.

It identifies the core business entities involved in the lending lifecycle and the relationships between them.

The model was designed before implementation to ensure consistency, maintainability, and scalability throughout the project.


## Data Modeling Approach

The data model follows a relational design based on business processes rather than technical implementation.

Instead of treating the dataset as a single flat file, the project separates customer information, loan applications, approved loans, payment history, and recovery events into independent entities.

This approach minimizes redundancy and reflects how lending systems are typically structured.

## Core Business Entities
| Entity           | Purpose                    |
| ---------------- | -------------------------- |
| Customer         | Borrower information       |
| Branch           | Loan issuing branch        |
| Credit Profile   | Customer financial profile |
| Loan Application | Application request        |
| Loan Product     | Product catalog            |
| Loan             | Approved loan              |
| Payment          | EMI history                |
| Default Event    | Default occurrence         |
| Recovery         | Recovery activities        |
| Write-off        | Final loan loss            |


## Entity Relationship Diagram

## Entity Descriptions

## Cardinality

## Normalization Strategy

## Data Integrity

## Data Dictionary Summary
| Entity           | Approx Columns |
| ---------------- | -------------: |
| Customer         |             11 |
| Branch           |              6 |
| Credit Profile   |              6 |
| Loan Application |              7 |
| Loan             |             10 |
| Payment          |             13 |
| Recovery         |              5 |
| Write-off        |              4 |

## Design Decisions