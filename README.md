# Banking Data Analytics & BI Project

A complete end-to-end data analytics project that generates, loads, cleans, and analyzes a **synthetic banking dataset of 440,100 records** stored in **Oracle Database 26ai Free**, then produces business insights, Excel/CSV reports, and visualization charts — ready for portfolio and job-application review.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Database Architecture](#database-architecture)
- [Dataset Information](#dataset-information)
- [Data Analysis Workflow](#data-analysis-workflow)
- [Business Insights](#business-insights)
- [Reports and Visualizations](#reports-and-visualizations)
- [Project Folder Structure](#project-folder-structure)
- [Installation and Execution](#installation-and-execution)
- [Security Notes](#security-notes)

---

## Project Overview

This project simulates a real-world banking analytics pipeline:

1. **Generate** realistic synthetic banking data with Python (Faker).
2. **Load** the data into an Oracle Database 26ai Free schema (5 related tables).
3. **Clean and validate** the data (duplicates, missing values, invalid records, outliers).
4. **Analyze** customers, accounts, transactions, loans, and branches with Pandas, SQL, and statistical methods.
5. **Deliver** automated business insights, Excel/CSV reports, and PNG charts.

The pipeline is orchestrated by a single master script (`main.py`) that runs the full reporting workflow automatically.

---

## Technologies Used

| Category | Technology |
|---|---|
| Language | Python 3.12 |
| Database | Oracle Database 26ai Free (FREEPDB1) |
| Dataframes & Numerics | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Database Drivers | python-oracledb, SQLAlchemy |
| Configuration | python-dotenv (`.env` file) |
| Data Generation | Faker |
| Reports | OpenPyXL (Excel), CSV |

---

## Database Architecture

Five related tables model a core banking system:

```text
BRANCHES ─┬─< CUSTOMERS ─┬─< ACCOUNTS ─┬─< TRANSACTIONS
          │              │              │
          └──────────────┴──────────────┴─< LOANS
```

| Table | Key Columns | Description |
|---|---|---|
| **BRANCHES** | BRANCH_ID, BRANCH_NAME, CITY, DISTRICT, OPENING_DATE, STATUS | 100 bank branches |
| **CUSTOMERS** | CUSTOMER_ID, FIRST_NAME, LAST_NAME, GENDER, DATE_OF_BIRTH, PHONE, EMAIL, CITY, DISTRICT, BRANCH_ID, REGISTRATION_DATE, STATUS | 50,000 customers linked to branches |
| **ACCOUNTS** | ACCOUNT_ID, CUSTOMER_ID, ACCOUNT_TYPE, OPENING_DATE, BALANCE, STATUS | 70,000 accounts with balances |
| **TRANSACTIONS** | TRANSACTION_ID, ACCOUNT_ID, TRANSACTION_DATE, TRANSACTION_TYPE, AMOUNT, CHANNEL, STATUS | 300,000 transactions across types and channels |
| **LOANS** | LOAN_ID, CUSTOMER_ID, LOAN_TYPE, LOAN_AMOUNT, INTEREST_RATE, ISSUE_DATE, DUE_DATE, LOAN_STATUS, IS_DEFAULTED | 20,000 loans with default tracking |

All connections are managed through `db_connection.py` (direct `oracledb` connection + SQLAlchemy engine for Pandas `read_sql`).

---

## Dataset Information

Synthetic banking data — **440,100 total records** across five tables:

| Table | Records |
|---|---:|
| Branches | 100 |
| Customers | 50,000 |
| Accounts | 70,000 |
| Transactions | 300,000 |
| Loans | 20,000 |
| **Total** | **440,100** |

> This data is fully synthetic and generated with `Faker`. It contains **no real customer banking information**.

---

## Data Analysis Workflow

### 1. Data Generation & Loading
- `generate_branches.py`, `generate_customers.py`, `generate_accounts.py`, `generate_transactions.py`, `generate_loans.py` — create synthetic records.
- `load_customers.py` — bulk-loads data into Oracle.

### 2. Data Cleaning & Quality
- `data_cleaning.py` — detects duplicates, missing values, invalid records, and IQR-based outliers.
- `automated_quality_report.py` — produces an automated data quality report.

### 3. Core Analysis
- `customer_analysis.py` — demographics: age, gender, city distribution.
- `account_analysis.py` — account types, balances, statistics.
- `transaction_analysis.py` — transaction types, channels, volumes.
- `loan_analysis.py` / `loan_statistics.py` — loan portfolio and default analysis.
- `branch_analysis.py` — branch-wise performance.

### 4. Advanced Analytics
- `statistical_analysis.py` — descriptive statistics.
- `correlation_analysis.py` — correlation matrix (balance vs. transaction behavior).
- `outlier_analysis.py` — outlier detection with boxplots.
- `transaction_trend.py` — time-series transaction trends.

### 5. Reporting & Automation
- `business_insights.py` — consolidated business insight summary.
- `export_reports.py` — Excel/CSV report export.
- `save_charts.py` — automated chart generation (PNG).
- `main.py` — **master script** that runs the full reporting pipeline in sequence.

---

## Business Insights

| Metric | Value |
|---|---:|
| Total Customers | 50,000 |
| Total Accounts | 70,000 |
| Total Transactions | 300,000 |
| Total Transaction Amount | ≈ 29.94 Billion |
| Total Loan Amount | ≈ 50.39 Billion |
| Defaulted Loans | 3,945 (≈ 19.7% default rate) |
| Data Quality Issues | 0 duplicates, 0 missing values, 0 invalid records |

Analysis covers customer segmentation, deposit concentration by account type, transaction channel mix, and loan default risk — the core questions a banking analyst would answer.

---

## Reports and Visualizations

### Reports (`reports/`)
| File | Contents |
|---|---|
| `banking_analysis.xlsx` | Full multi-sheet analysis workbook |
| `banking_summary.csv` | Key banking KPIs |
| `data_quality_report.xlsx` / `.csv` | Data quality metrics per table |

### Charts (`reports/charts/`)
| Chart | Focus |
|---|---|
| `account_balance.png` | Balance distribution |
| `account_type.png` | Account type mix |
| `customers_by_city.png` | Geographic distribution |
| `loan_amount.png` | Loan amount distribution |
| `loan_status.png` | Loan status breakdown |
| `transaction_channel.png` | Channel usage |
| `transaction_type.png` | Transaction type mix |

---

## Project Folder Structure

```text
Banking-Data-Analytics/
├── .env.example              # Environment variable template (safe to commit)
├── .gitignore                # Excludes .env, venv/, __pycache__, IDE files
├── README.md
├── requirements.txt          # Pinned Python dependencies
│
├── db_connection.py          # Reusable Oracle + SQLAlchemy connection module
├── main.py                   # Master pipeline orchestrator
│
├── # Data generation & loading
├── generate_branches.py
├── generate_customers.py
├── generate_accounts.py
├── generate_transactions.py
├── generate_loans.py
├── load_customers.py
│
├── # Data cleaning & quality
├── data_cleaning.py
├── automated_quality_report.py
│
├── # Analysis scripts
├── customer_analysis.py
├── account_analysis.py
├── transaction_analysis.py
├── transaction_trend.py
├── loan_analysis.py
├── loan_statistics.py
├── branch_analysis.py
├── business_insights.py
├── statistical_analysis.py
├── correlation_analysis.py
├── outlier_analysis.py
│
├── # Reporting & checks
├── export_reports.py
├── save_charts.py
├── final_database_check.py
├── final_report_check.py
├── final_security_check.py
│
├── # Connection tests
├── test_connection.py
├── test_db_connection.py
├── test_env.py
├── test_sqlalchemy.py
│
└── reports/
    ├── banking_analysis.xlsx
    ├── banking_summary.csv
    ├── data_quality_report.xlsx
    ├── data_quality_report.csv
    └── charts/
        ├── account_balance.png
        ├── account_type.png
        ├── customers_by_city.png
        ├── loan_amount.png
        ├── loan_status.png
        ├── transaction_channel.png
        └── transaction_type.png
```

---

## Installation and Execution

### Prerequisites
- Python 3.12+
- Oracle Database 26ai Free (local instance with service `FREEPDB1`)

### 1. Clone the repository
```bash
git clone https://github.com/rohulkuddusrobi/banking_data_analyst.git
cd banking_data_analyst
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure database credentials
Copy the template and fill in your own values (never commit `.env`):
```bash
copy .env.example .env
```
`.env`:
```ini
ORACLE_USER=your_db_user
ORACLE_PASSWORD=your_db_password
ORACLE_DSN=localhost:1521/FREEPDB1
```

### 5. (Optional) Generate and load the dataset
```bash
python generate_branches.py
python generate_customers.py
python generate_accounts.py
python generate_transactions.py
python generate_loans.py
```

### 6. Run the full analysis pipeline
```bash
python main.py
```

Or run any individual analysis script directly:
```bash
python business_insights.py
```

Reports and charts are written to the `reports/` folder.

---

## Security Notes

- **No credentials are stored in source code.** All database connections read `ORACLE_USER`, `ORACLE_PASSWORD`, and `ORACLE_DSN` from environment variables via `python-dotenv`.
- `.env` is excluded by `.gitignore` and is **never** committed.
- `.env.example` documents the required variables with placeholder values only.
- This repository contains **synthetic data only** — no real customer information.

---

> **Note:** This project is built for educational and portfolio purposes using synthetic banking data.
#   b a n k i n g _ d a t a _ a n a l y s t  
 