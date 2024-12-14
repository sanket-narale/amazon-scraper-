import sqlite3
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def store_in_database(input_file, db_file):
    """
    Store preprocessed data in a SQLite database.
    """
    try:
        logging.info("Storing data in SQLite database...")
        df = pd.read_csv(input_file)

        conn = sqlite3.connect(db_file)
        df.to_sql("products", conn, if_exists="replace", index=False)
        conn.close()

        logging.info(f"Data stored successfully in {db_file}")
    except Exception as e:
        logging.error(f"Error storing data in database: {e}")

if __name__ == "__main__":
    store_in_database("../data/cleaned_data.csv", "../data/amazon_products.db")
