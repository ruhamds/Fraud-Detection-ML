# data_loading.py
# Purpose: Load e-commerce and bank transaction datasets for fraud detection analysis.

import pandas as pd

def load_fraud_data(path=r"C:\Users\Antifragile\Desktop\Fraud_detection\data\Fraud_Data.csv"):
    """
    Load the e-commerce transaction dataset.
    Args:
        path (str): Path to the Fraud_Data.csv file.
    Returns:
        pandas.DataFrame: Loaded e-commerce transaction data.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loaded e-commerce data with {len(data)} records.")
        return data
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return None

def load_ip_to_country(path=r"C:\Users\Antifragile\Desktop\Fraud_detection\data\IpAddress_to_Country.csv"):
    """
    Load the IP address to country mapping dataset.
    Args:
        path (str): Path to the IpAddress_to_Country.csv file.
    Returns:
        pandas.DataFrame: Loaded IP address to country mapping data.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loaded IP to country data with {len(data)} records.")
        return data
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return None

def load_creditcard_data(path=r"C:\Users\Antifragile\Desktop\Fraud_detection\data\creditcard.csv"):
    """
    Load the bank transaction dataset.
    Args:
        path (str): Path to the creditcard.csv file.
    Returns:
        pandas.DataFrame: Loaded bank transaction data.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loaded credit card data with {len(data)} records.")
        return data
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return None

if __name__ == "__main__":
    Fraud_data = load_fraud_data()
    ipAddress_to_country = load_ip_to_country()
    creditcard_data = load_creditcard_data()
