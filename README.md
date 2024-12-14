**Amazon Product Scraper and Data Visualization**

**📋 Overview**

This project is a comprehensive pipeline for scraping product data from Amazon, cleaning and preprocessing the data, storing it in a relational database, and visualizing trends. It demonstrates the full cycle of web scraping, data processing, and visualization.

**🏗️ Features**
Web Scraping: Extracts product name, price, rating, and number of reviews using Selenium.
Data Preprocessing: Cleans raw data (handles missing values, normalizes formats, and removes duplicates).
Data Storage: Stores cleaned data in an SQLite database for structured access.
Interactive Visualizations: Generates insights using Matplotlib and Seaborn (e.g., price distribution, most-reviewed products).
End-to-End Deliverables: Includes scripts, a database file, a report.

**⚙️ Installation and Setup**
1. Clone the Repository
   git clone https://github.com/sanket-narale/amazon-scraper-
.git
cd amazon-scraper
2. Set Up the Environment
   pip install -r requirements.txt
3. Install WebDriver
   Download the ChromeDriver for your browser version.
Place it in your PATH or the project folder.

**🏃‍♂️ Usage**
1. Scrape Data
Run the scraper.py script to scrape product data from Amazon:
cd scraping
python scraper.py

2. Preprocess Data
   python preprocess.py

3. Store in Database
   python database.py

4. Generate Visualizations
   jupyter notebook visualizations/trends.ipynb

**📦 Project Deliverables**

Codebase: All Python scripts for scraping, preprocessing, and database handling.
Database: SQLite file (amazon_products.db) with structured data.
Visualizations: Screenshots and charts demonstrating trends.
Report: Comprehensive report explaining the pipeline and insights.

**🛠️ Technologies Used**
Programming Language: Python
Libraries: Selenium, Pandas, Matplotlib, Seaborn
Database: SQLite
Visualization: Matplotlib, Seaborn
Web Scraping: Selenium
