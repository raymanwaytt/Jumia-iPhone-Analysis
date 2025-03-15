# Jumia iPhone Catalog Analysis

## Overview

This project analyzes iPhone listings on Jumia Nigeria to understand pricing trends, model popularity, and storage preferences. The dataset was scraped on **March 13, 2025**, and contains over **300 listings**. 

Using **Python** for web scraping and **Power BI** for visualization, this report provides key insights into Nigeria's iPhone market, including price distributions, popular models, and storage capacity preferences.

---
![Power BI Dashboard](https://raw.githubusercontent.com/raymanwaytt/Jumia-iPhone-Analysis/master/visualization/dashboard.png)


## Key Findings

### 1. iPhone Prices
- **Average Price:** ₦1,040,861
- **Most Expensive:** ₦4,000,000 (iPhone 15 Pro Max, 512GB)
- **Cheapest:** ₦257,990 (iPhone 8, 64GB)
- **Common Price Range:** ₦770,000 – ₦1,200,000
- **Odd Trend:** All iPhone XR models (64GB and 128GB) are priced at exactly ₦760,000.

### 2. Most Listed iPhone Models
- **iPhone 12 Pro** – 50 listings
- **iPhone 13 Pro Max** – 39 listings
- **iPhone 13** – 36 listings
- **iPhone 12** – 31 listings
- **iPhone 14 Pro Max** – 24 listings
- **iPhone 15 Pro Max** – 16 listings

### 3. Storage Preferences
- **128GB** – 152 listings (48%)
- **256GB** – 112 listings (36%)
- **64GB** – 39 listings (mostly older models like iPhone 11 and XR)
- **512GB & 1TB** – 12 listings combined (all iPhone 15 series)

Nigerians favor **128GB and 256GB** models over ultra-high storage options.

---

## Insights for Buyers & Sellers

### If You’re Buying:
- **Best Value:** iPhone 12 or 13 series within the ₦770,000 – ₦1,200,000 range.
- **Budget Option:** iPhone 8 or XR, but at ₦760,000, the XR may not be the best deal.
- **High-End:** iPhone 15 Pro Max models cost **₦4M+,** making them a premium purchase.

### If You’re Selling:
- **High-Demand Models:** iPhone 12 Pro, 13 Pro Max, and 13.
- **Competitive Pricing:** Avoid overpricing older models (e.g., iPhone XR at ₦760,000).
- **Rare Storage Options:** If selling 512GB or 1TB models, target premium buyers since stock is low.

---

## Methodology

### Data Collection
- Scraped iPhone listings from **Jumia Nigeria** using **Python (requests, BeautifulSoup)**.
- No CAPTCHA issues or major barriers encountered.

### Data Cleaning
- Processed and cleaned with **Pandas**.
- Extracted model names and storage sizes using **Regex**.
- Standardized inconsistent text formatting.

### Visualization
- Created  **Power BI dashboard** to analyze pricing, model frequency, and storage trends.
View the full visualization here (open with Power BI):
![Power BI Dashboard](https://raw.githubusercontent.com/raymanwaytt/Jumia-iPhone-Analysis/master/visualization/dashboard.pbix)

---

##  Repository Structure

Jumia-iPhone-Analysis/
│-- data/
│   ├── cleaned_jumia.csv
│
│-- scripts/      
│   ├── jumia_scraper.py     # Web scraping script (BeautifulSoup & requests)
│   ├── data_cleaning.ipynb  # Data cleaning (Pandas & REGEX)
│
│-- visualization/
│   ├── dashboard.pbix       # Power BI report file
│   ├── dashboard.png        # Dashboard preview
│
│-- README.md                # Project documentation
│-- requirements.txt          # Python dependencies


---

## Next Steps
- **Price Tracking:** Monitor trends over time to see if high-end models depreciate.
- **Expand to Other Brands:** Compare iPhones with Samsung and Tecno models.

---

## Data Source
- [**Jumia Nigeria iPhone Listings**](https://www.jumia.com.ng/ios-phones/apple/#catalog-listing) (Scraped on **March 13, 2025**)