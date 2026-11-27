# Mest Stores – Printers Web Scraper

A Python web scraping project built to extract printer product information from the Mest Stores website.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- CSV

## Target Website
https://meststores.com/product-category/printers/

## Extracted Data
The scraper collects the following product information:

- Product Description
- Current Price
- Original Price / Discount Price
- Product Rating
- Product URL
- Product Image URL

## Features
- Scrapes printer products across multiple pages.
- Uses Requests to retrieve webpage HTML.
- Uses BeautifulSoup to parse HTML and extract product information.
- Stores the extracted data in a CSV file.
- Saves all products in a structured format using Python dictionaries.

## Output
The extracted data is saved in:

`all products.csv`

The CSV file can be opened using Microsoft Excel or other spreadsheet applications.

## Project Purpose
This project demonstrates practical web scraping skills using Python, Requests, and BeautifulSoup on a real e-commerce website.
