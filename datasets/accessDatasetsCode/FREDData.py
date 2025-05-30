import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

dotenv_path = "/Users/guhamahesh/VSCODE/dialogue/FinFluxes/api/.env"
load_dotenv(dotenv_path)
api_key = os.getenv("FRED_API_KEY")
pd.set_option('display.max_columns', None)


def interestRate(type):
    map = {"federalfundsrate": "FEDFUNDS", "DiscountRate": "INTDSRUSM193N",
           "TreasurySecurities": "WSHOMCB", "FedReserveBalanceSheet": "WALCL"}

    code = map[type.replace(" ", "")]

    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={code}&api_key={api_key}&file_type=json"
    response = requests.get(url)
    jsondata = response.json()
    df = pd.DataFrame(jsondata["observations"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.rename(columns={'value': f'{type}_value'})

    return df.dropna(subset=[f'{type}_value'])


def exports():

    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=NETEXP&api_key={api_key}&file_type=json"
    response = requests.get(url)
    jsondata = response.json()
    df = pd.DataFrame(jsondata["observations"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.rename(columns={'value': f'exports_value'})
    print(url)
    return df.dropna(subset=['exports_value'])


def conversions(currency):

    currency_fred_codes = {
        "Euro (EUR)": "DEXUSEU",         # USD per 1 Euro
        "British Pound (GBP)": "DEXUSUK",  # USD per 1 British Pound
        "Japanese Yen (JPY)": "DEXJPUS",  # JPY per 1 USD (note: inverse)
        "Canadian Dollar (CAD)": "DEXCAUS",  # CAD per 1 USD (inverse)
        "Swiss Franc (CHF)": "DEXSZUS",  # CHF per 1 USD
        "Australian Dollar (AUD)": "DEXUSAL",  # USD per 1 AUD
        "Chinese Yuan (CNY)": "DEXCHUS",  # CNY per 1 USD
        "Indian Rupee (INR)": "DEXINUS",  # INR per 1 USD
        "Mexican Peso (MXN)": "DEXMXUS",  # MXN per 1 USD
        "Brazilian Real (BRL)": "DEXBZUS",  # BRL per 1 USD
        "Russian Ruble (RUB)": "DEXRUS",  # RUB per 1 USD
        "South Korean Won (KRW)": "DEXKOUS",  # KRW per 1 USD
        "Swedish Krona (SEK)": "DEXSDUS",  # SEK per 1 USD
        "Norwegian Krone (NOK)": "DEXNOUS",  # NOK per 1 USD
        "Singapore Dollar (SGD)": "DEXSIUS",  # SGD per 1 USD
        "Hong Kong Dollar (HKD)": "DEXHKUS",  # HKD per 1 USD
        "New Zealand Dollar (NZD)": "DEXUSNZ",  # USD per 1 NZD
        "South African Rand (ZAR)": "DEXSFUS",  # ZAR per 1 USD
        "Turkish Lira (TRY)": "DEXTUUS",  # TRY per 1 USD
        "Israeli Shekel (ILS)": "DEXISUS",  # ILS per 1 USD
    }
    code = currency_fred_codes[currency]
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={code}&api_key={api_key}&file_type=json"
    response = requests.get(url)
    jsondata = response.json()
    df = pd.DataFrame(jsondata["observations"])

    # Clean values
    df["exchange_value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["exchange_value"])

    # Convert to Period[M] to remove day
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")

    # Drop duplicate months
    df = df.drop_duplicates(subset="month", keep="first")

    # Filter date range
    df = df[(df["month"] >= "2003-01") & (df["month"] <= "2024-02")]

    return df[["month", "exchange_value"]]
