# Sales Analytics System

This project is a Python-based Sales Analytics System that reads sales transaction data, cleans and validates it, performs sales analysis, integrates external product data using an API, enriches sales records, and generates a comprehensive sales report.

---

## Project Structure

```
sales-analytics-system/
├── data/
│   ├── sales_data.txt
│   └── enriched_sales_data.txt
├── output/
│   └── sales_report.txt
├── utils/
│   ├── file_handler.py
│   ├── data_processor.py
│   ├── api_handler.py
│   └── report_generator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Features

- Handles file encoding issues (UTF-8, Latin-1, CP1252)
- Cleans and validates sales data
- Performs sales analysis:
  - Total sales
  - Region-wise sales
  - Top products by revenue
  - Customer analysis
  - Daily sales trend
  - Peak sales day
  - Low-performing products
- Integrates product data using the DummyJSON API
- Enriches sales data with API information
- Generates a detailed sales report

---

## Requirements

- Python 3.10 or above
- requests library

Install dependencies using:

```
pip install -r requirements.txt
```

---

## How to Run

1. Clone the repository:
```
git clone https://github.com/<your-username>/sales-analytics-system
```

2. Navigate to the project directory:
```
cd sales-analytics-system
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the application:
```
python main.py
```

---

## Output

- Enriched sales data is saved to:
```
data/enriched_sales_data.txt
```

- Sales report is generated at:
```
output/sales_report.txt
```

---

## Notes

- Ensure the repository remains public until evaluation is complete.
- Delete all `__pycache__` folders before submission.
- All file paths are relative to the project root.

---

## Author

Devanshi
