import logging
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure `chromedriver` is installed

def scrape_amazon(search_query, output_file):
    """
    Scrape product data from Amazon and save it as a CSV.
    """
    try:
        logging.info("Starting Amazon scraper...")
        driver.get("https://www.amazon.in")
        time.sleep(2)

        # Perform search
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Collect product data
        product_data = []
        products = driver.find_elements(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item")

        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, "h2 a span").text
            except:
                name = "Unknown"

            try:
                price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
            except:
                price = "Unknown"

            try:
                rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
            except:
                rating = "Unknown"

            try:
                reviews = product.find_element(By.CSS_SELECTOR, "span.a-size-base").text
            except:
                reviews = "Unknown"

            product_data.append({
                "Name": name,
                "Price": price,
                "Rating": rating,
                "Reviews": reviews
            })

        # Save to CSV
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Price", "Rating", "Reviews"])
            writer.writeheader()
            writer.writerows(product_data)

        logging.info(f"Scraped data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_amazon("laptops", "../data/raw_data.csv")
