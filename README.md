# 🌍 API Scraper Project COVID & Crypto ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green)
![API](https://img.shields.io/badge/API-Integration-orange)
![CSV](https://img.shields.io/badge/Output-CSV-yellow)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📖 Overview

This project demonstrates a simple **ETL (Extract, Transform, Load) Pipeline** built using Python.

The script connects to two public APIs, extracts selected data points, performs data cleaning and transformation, and exports the processed data into timestamped CSV files.

The project showcases fundamental **Data Engineering concepts** including API integration, data extraction, transformation, and file-based storage.

---

## 🎯 APIs Used

### 🦠 COVID-19 Data API

API Endpoint:

```text
https://disease.sh/v3/covid-19/countries
```

Extracted Fields:

* Country
* Cases
* Today Cases
* Deaths
* Today Deaths
* Recovered
* Active Cases

### 💰 CoinGecko Crypto API

API Endpoint:

```text
https://api.coingecko.com/api/v3/coins/markets
```

Extracted Fields:

* Coin ID
* Symbol
* Current Price
* Market Cap
* Total Volume
* Price Change Percentage (24h)

---

## ✨ Features

✅ Connects to multiple REST APIs

✅ Extracts business-relevant data fields

✅ Processes and cleans JSON responses

✅ Renames columns for better readability

✅ Generates timestamped output files

✅ Stores processed data in CSV format

✅ Simple and scalable ETL workflow

---

## 🏗️ Pipeline Architecture

```text
API Sources
     │
     ▼
Data Extraction
     │
     ▼
Data Cleaning
     │
     ▼
Column Renaming
     │
     ▼
CSV Export
     │
     ▼
Timestamped Output Files
```

---

## 🔄 Data Processing Workflow

### 1️⃣ Extract

* Connect to public APIs
* Fetch JSON responses
* Select required fields

### 2️⃣ Transform

* Remove unnecessary attributes
* Rename columns
* Standardize data structure

### 3️⃣ Load

* Export processed data
* Save datasets as CSV files
* Append timestamp to file names

---

## 📊 Extracted Data

### 🦠 COVID-19 Dataset

| Column Name |
| ----------- |
| country     |
| cases       |
| todayCases  |
| deaths      |
| todayDeaths |
| recovered   |
| active      |

### 💰 Cryptocurrency Dataset

| Column Name                 |
| --------------------------- |
| id                          |
| symbol                      |
| current_price               |
| market_cap                  |
| total_volume                |
| price_change_percentage_24h |

---

## 🧹 Data Transformation

The script performs basic data transformation including:

* Selecting required fields
* Renaming columns
* Structuring tabular data
* Preparing datasets for analytics
* Generating timestamped outputs

### Example Column Renaming

#### COVID Dataset

| Original Column | Renamed Column  |
| --------------- | --------------- |
| country         | Country         |
| cases           | Total_Cases     |
| todayCases      | New_Cases       |
| deaths          | Total_Deaths    |
| todayDeaths     | New_Deaths      |
| recovered       | Recovered_Cases |
| active          | Active_Cases    |

#### Crypto Dataset

| Original Column             | Renamed Column       |
| --------------------------- | -------------------- |
| id                          | Coin_ID              |
| symbol                      | Symbol               |
| current_price               | Current_Price        |
| market_cap                  | Market_Cap           |
| total_volume                | Trading_Volume       |
| price_change_percentage_24h | Price_Change_24H (%) |

---

## 📁 Output Files

The processed datasets are exported as timestamped CSV files.

Example:

```text
covid_data_20260605_153000.csv
crypto_data_20260605_153000.csv
```

---

## 🛠️ Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Requests     | API Communication    |
| Pandas       | Data Processing      |
| Datetime     | Timestamp Generation |
| CSV          | Data Storage         |
| Git & GitHub | Version Control      |

---

## 📂 Project Structure

```text
project/
│
├── API_Scraper.py
├── output/
│   ├── covid_data_YYYYMMDD_HHMMSS.csv
│   └── crypto_data_YYYYMMDD_HHMMSS.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### Clone Repository

```bash
git clone https://github.com/your-username/covid-crypto-etl-pipeline.git
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python API_Scraper.py
```

---

## 📈 Sample Output

Generated CSV files:

```text
covid_data_20260605_153000.csv
crypto_data_20260605_153000.csv
```

---

## 🚀 Future Enhancements

* Store data in AWS S3
* Load data into Snowflake
* Automate execution using Apache Airflow
* Add Docker support
* Implement logging and monitoring
* Add data quality checks

---

## 📌 Learning Outcomes

This project demonstrates:

* REST API Integration
* JSON Data Processing
* Data Cleaning & Transformation
* CSV File Generation
* Timestamp Management
* Basic ETL Pipeline Development
* Python-Based Data Engineering Workflows

---

## 🌐 Author

[![GitHub](https://img.shields.io/badge/GitHub-ubaidsaghir-181717?logo=github&logoColor=white)](https://github.com/ubaidsaghir)

