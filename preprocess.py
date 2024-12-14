import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def preprocess_data(input_file, output_file):
    """
    Clean and preprocess the scraped data.
    """
    try:
        logging.info("Starting data preprocessing...")
        df = pd.read_csv(input_file)

        # Handle missing values
        df.fillna("Unknown", inplace=True)

        # Normalize columns
        df["Price"] = pd.to_numeric(df["Price"].str.replace(",", ""), errors="coerce")
        df["Rating"] = pd.to_numeric(df["Rating"].str.extract(r"(\d\.\d)")[0], errors="coerce")
        df["Reviews"] = pd.to_numeric(df["Reviews"].str.replace(",", ""), errors="coerce")

        # Drop duplicates and save
        df.drop_duplicates(inplace=True)
        df.to_csv(output_file, index=False)

        logging.info(f"Cleaned data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    preprocess_data("../data/raw_data.csv", "../data/cleaned_data.csv")
