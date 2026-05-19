# web-scraping-project-batch4
Final Capstone Project
---


# Mobile Phone Web Scraping Project

## Project Overview

This project is a Python-based web scraping application that extracts mobile phone product information from:

[Unique Mobile Collection](https://unique.com.mm/collections/mobile-phone?utm_source=chatgpt.com)

The scraper automatically collects:

* Product Name
* Product Price
* Product Stock Status

The extracted data is cleaned, organized, and exported into Excel files for analysis and learning purposes.

---

## Technologies Used

The project is built using the following Python libraries:

* `requests` → Retrieve webpage data
* `BeautifulSoup (bs4)` → Parse HTML content
* `pandas` → Store and export structured data
* `datetime` → Generate timestamps for file naming
* `tqdm` → Show scraping progress bar

---

## Required Libraries

Install the required libraries before running the project:

```bash id="1bj4cv"
pip install requests beautifulsoup4 pandas html5lib tqdm
```

Or install using:

```bash id="0jkcjr"
pip install -r requirements.txt
```

---

## Main Features

* Automatic pagination URL generation
* Product information extraction
* Product price cleaning and formatting
* Inventory status detection
* Page-level Excel export
* Final combined dataset export
* Progress tracking using tqdm

---

## Project Workflow

1. Generate URLs for all pages
2. Request webpage data
3. Extract product information using BeautifulSoup
4. Clean and organize the data
5. Store data in pandas DataFrames
6. Export data into Excel files

---

## How to Run the Project

Run the following command:

```bash id="q4ztnj"
python main.py
```

---

## Example Output

| Product Name       |   Price | Status    |
| ------------------ | ------: | --------- |
| iPhone 15          | 3200000 | In Stock  |
| Samsung Galaxy A55 | 1200000 | Low Stock |

---

## Learning Outcomes

This project helps practice:

* Web scraping with Python
* HTML parsing
* Pagination scraping
* Data cleaning and preprocessing
* Exception handling
* Working with pandas DataFrames
* Exporting data into Excel files

---

## Educational Purpose

This project was created strictly for educational and learning purposes only.

The objective is to practice Python programming, web scraping, and data processing techniques. The scraped data is not intended for commercial use or redistribution.

All website data belongs to its respective owner:
[Unique Myanmar](https://unique.com.mm?utm_source=chatgpt.com)

Please use web scraping responsibly and follow the website’s terms and conditions.

---

## Author

**Su Myat Noe**
Student at Python Myanmar Institute
