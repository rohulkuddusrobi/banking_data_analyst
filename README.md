# Banking Data Analytics & Business Intelligence Project

An end-to-end Banking Data Analytics project built using **Python, SQL, and Oracle Database 26ai Free**. This project simulates a real-world banking environment using **440,100 synthetic records** across five relational tables.

The project covers data generation, database management, data cleaning, exploratory data analysis, statistical analysis, business insights, and automated reporting.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Objectives](#project-objectives)
- [Technology Stack](#technology-stack)
- [Database Architecture](#database-architecture)
- [Dataset Information](#dataset-information)
- [Analytics and Workflow](#analytics-and-workflow)
- [Key Business Insights](#key-business-insights)
- [Reports and Visualizations](#reports-and-visualizations)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Security and Data Disclaimer](#security-and-data-disclaimer)
- [Future Improvements](#future-improvements)

---

## Project Overview

This project demonstrates how banking data can be transformed into meaningful business insights through a complete analytics workflow.

It simulates a banking database containing customers, accounts, transactions, branches, and loans.

The workflow includes:

1. Generating synthetic banking data using Python and Faker.
2. Storing structured data in Oracle Database 26ai Free.
3. Cleaning and validating datasets.
4. Performing SQL-based data extraction and Python-based analysis.
5. Conducting statistical analysis and identifying trends.
6. Generating business insights, Excel/CSV reports, and charts.

The reporting workflow is automated through a master Python script: `main.py`.

## Project Objectives

- Analyze customer demographics and account distribution.
- Understand transaction behavior and banking channel usage.
- Evaluate loan portfolios and loan default patterns.
- Identify data quality issues and statistical outliers.
- Generate meaningful banking KPIs and business insights.
- Build a reusable analytics and reporting workflow.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python 3.12 |
| Database | Oracle Database 26ai Free |
| Query Language | SQL |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Database Connectivity | python-oracledb, SQLAlchemy |
| Data Generation | Faker |
| Configuration | python-dotenv |
| Reporting | Excel, OpenPyXL, CSV |
| Development Environment | VS Code |

## Database Architecture

The project uses five related relational tables connected through primary and foreign keys.

```text
                  BRANCHES
                      |
                      | 1:N
                      |
                  CUSTOMERS
                   /      \
                1:N        1:N
                 /          \
            ACCOUNTS       LOANS
                |
                | 1:N
                |
           TRANSACTIONS
```

### Database Tables

| Table | Records | Description |
|---|---:|---|
| BRANCHES | 100 | Banking branch information |
| CUSTOMERS | 50,000 | Customer profiles and demographics |
| ACCOUNTS | 70,000 | Customer bank accounts and balances |
| TRANSACTIONS | 300,000 | Banking transactions and activity |
| LOANS | 20,000 | Loan portfolio and default information |
| **Total** | **440,100** | **Complete synthetic dataset** |

Database service: `FREEPDB1`

Database connectivity is managed through `db_connection.py`.

## Dataset Information

The project uses a fully synthetic banking dataset generated with Python and Faker.

**Total records: 440,100**

The dataset includes:

- Customer demographics
- Account types and balances
- Transaction amounts, dates, types, channels, and statuses
- Branch locations and information
- Loan amounts, interest rates, repayment status, and default indicators

No real customer banking information is used.

## Analytics and Workflow

### 1. Data Generation and Loading

Scripts:
- `generate_branches.py`
- `generate_customers.py`
- `generate_accounts.py`
- `generate_transactions.py`
- `generate_loans.py`
- `load_customers.py`

### 2. Data Cleaning and Quality Assessment

Scripts:
- `data_cleaning.py`
- `automated_quality_report.py`

Activities:
- Missing value detection
- Duplicate detection
- Invalid record checks
- Outlier identification
- Data quality reporting

### 3. Core Banking Analytics

| Script | Analysis |
|---|---|
| `customer_analysis.py` | Customer demographics and segmentation |
| `account_analysis.py` | Account types and balance distribution |
| `transaction_analysis.py` | Transaction types, amounts, and channels |
| `loan_analysis.py` | Loan portfolio analysis |
| `loan_statistics.py` | Loan statistical analysis |
| `branch_analysis.py` | Branch-wise performance |
| `business_insights.py` | Consolidated business insights |

### 4. Advanced Statistical Analysis

| Script | Purpose |
|---|---|
| `statistical_analysis.py` | Descriptive statistics |
| `correlation_analysis.py` | Correlation analysis |
| `outlier_analysis.py` | Statistical outlier detection |
| `transaction_trend.py` | Transaction trends over time |

### 5. Reporting and Automation

- `export_reports.py` — exports Excel and CSV reports.
- `save_charts.py` — generates analytical charts.
- `main.py` — executes the reporting and analytics workflow.

## Key Business Insights

The following results were generated from the synthetic banking dataset.

| Business Metric | Result |
|---|---:|
| Total Customers | 50,000 |
| Total Accounts | 70,000 |
| Total Transactions | 300,000 |
| Total Transaction Amount | Approximately 29.94 Billion |
| Total Loan Amount | Approximately 50.39 Billion |
| Defaulted Loans | 3,945 |
| Loan Default Rate | Approximately 19.7% |

### Business Analysis Areas

- Customer demographics and geographic distribution
- Account type distribution and balance analysis
- Transaction type and channel performance
- Loan portfolio distribution
- Loan default risk analysis
- Banking data quality assessment

*Note: These metrics are calculated from synthetic data and are intended for educational and analytical demonstration.*

## Reports and Visualizations

All generated reports are stored in the `reports/` directory.

### Excel and CSV Reports

| File | Description |
|---|---|
| `banking_analysis.xlsx` | Multi-sheet banking analysis report |
| `banking_summary.csv` | Banking KPI summary |
| `data_quality_report.xlsx` | Detailed data quality report |
| `data_quality_report.csv` | Data quality metrics |

### Analytical Charts

The following charts are generated automatically:

| Chart | Purpose |
|---|---|
| `customers_by_city.png` | Customer geographic distribution |
| `account_type.png` | Account type distribution |
| `account_balance.png` | Account balance distribution |
| `transaction_type.png` | Transaction type distribution |
| `transaction_channel.png` | Transaction channel usage |
| `loan_status.png` | Loan status distribution |
| `loan_amount.png` | Loan amount distribution |

## Project Structure

```text
Banking-Data-Analytics/
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
│
├── db_connection.py
├── main.py
│
├── generate_branches.py
├── generate_customers.py
├── generate_accounts.py
├── generate_transactions.py
├── generate_loans.py
├── load_customers.py
│
├── data_cleaning.py
├── automated_quality_report.py
│
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
├── export_reports.py
├── save_charts.py
│
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
    │
    └── charts/
        ├── account_balance.png
        ├── account_type.png
        ├── customers_by_city.png
        ├── loan_amount.png
        ├── loan_status.png
        ├── transaction_channel.png
        └── transaction_type.png
```

## Installation and Setup

### Prerequisites

- Python 3.12 or later
- Oracle Database 26ai Free
- Oracle service: `FREEPDB1`
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/rohulkuddusrobi/banking_data_analyst.git
cd banking_data_analyst
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

Configure your own database credentials in `.env`:

```ini
ORACLE_USER=your_db_user
ORACLE_PASSWORD=your_db_password
ORACLE_DSN=localhost:1521/FREEPDB1
```

Never upload your actual `.env` file to GitHub.

### 5. Generate the Dataset (Optional)

Run the data generation scripts in the following order:

```bash
python generate_branches.py
python generate_customers.py
python generate_accounts.py
python generate_transactions.py
python generate_loans.py
```

Load the generated data into Oracle using the appropriate loading workflow.

### 6. Run the Analytics Pipeline

```bash
python main.py
```

You can also run individual analysis scripts:

```bash
python business_insights.py
python customer_analysis.py
python account_analysis.py
python transaction_analysis.py
python loan_analysis.py
```

Generated reports and charts are saved in the `reports/` directory.

## Security and Data Disclaimer

- Database credentials are managed through environment variables.
- `.env` is excluded through `.gitignore`.
- `.env.example` contains placeholder credentials only.
- The dataset is entirely synthetic.
- No real banking customer information is included.

This project is intended for educational, analytical, and portfolio purposes. It does not represent actual banking operations or customer records.

## Future Improvements

- Develop an interactive Power BI banking dashboard.
- Add advanced banking KPI visualizations.
- Build automated data refresh workflows.
- Extend customer segmentation and loan risk analytics.
- Introduce predictive analytics for banking business intelligence.

## Author

**Rohul Kuddus Robi**

CSE Student | Aspiring Data Analyst & BI Analyst

- GitHub: [rohulkuddusrobi](https://github.com/rohulkuddusrobi)
- Project Repository: [Banking Data Analytics](https://github.com/rohulkuddusrobi/banking_data_analyst)

---

**If you find this project useful, feel free to explore the repository!**
