# Canadian Hospital & Childbirth Dashboard

## Overview
An end-to-end data analytics project using publicly available data from the 
Canadian Institute for Health Information (CIHI). The project involved cleaning 
raw Excel data using Python and building an interactive dashboard in Power BI.

## Tools Used
- Python (pandas) - data cleaning and transformation
- Power BI - dashboard and visualizations
- Data source: CIHI Discharge Abstract Database (DAD), 2024-2025

## What the Dashboard Shows
- National hospitalization rates per 100,000 population from 2020 to 2025
- Top inpatient diagnoses across Canadian provinces in 2024-2025
- Newborns born in hospital by province in 2024-2025

## Key Findings
- Giving birth is the single highest volume inpatient diagnosis nationally, 
  at 708K hospitalizations - 4x the next highest diagnosis
- Hospitalization rates rose sharply post-COVID (2020-2022) then plateaued 
  around 7,560 per 100,000
- Ontario accounts for the largest share of hospital births nationally at 143K, 
  followed by Quebec at 73K

## Files
- clean_data.py - Python script for data cleaning and CSV export
- table1_hospitalization_trends.csv - cleaned national trend data
- table2_diagnoses_by_province.csv - cleaned diagnosis data by province
- table6_newborns_by_province.csv - cleaned newborn data by province
- dashboard_screenshot.png - Power BI dashboard screenshot

## Data Source
Canadian Institute for Health Information (CIHI): Inpatient Hospitalization, Surgery and Newborn Statistics, 2024-2025
https://www.cihi.ca/en/access-data-and-reports/data-tables
