import csv
import pandas as pd
from bill import Bill


class FileReader:

    def __init__(self, people_filename, bills_filename):
        self.people_txt = people_filename
        self.bills_csv = bills_filename

    def people_read(self):
        with open(self.people_txt, encoding='utf-8') as f:
            people = f.read().splitlines()
        return people

    def get_all_bills(self, file):
        bills = []
        with open(file, encoding='utf-8') as f:
            bills_raw = f.read().splitlines()
            for bill_raw in bills_raw:
                bills.append(bill_raw.split())
        return bills

    def read_csv_bills(self, file):
        bills = []
        df = pd.read_csv('bills.csv')
        for i in range(len(df)):
            date = df.iloc[i, 0]
            issuer = df.iloc[i, 1]
            ammount = self._sanitize_to_float(df.iloc[i, 2])
            description = df.iloc[i, 3]
            excluded_raw = df.iloc[i, 4]
            people_excluded = [] if (
                pd.isna(excluded_raw)) else excluded_raw.split(sep=',')
            bill = Bill(date, issuer, ammount, description, people_excluded)
            bills.append(bill)
        return bills

    def _sanitize_to_float(self, ammount_str):
        sanitized_float = ammount_str.replace('$', '').replace(' ', '')
        if sanitized_float[-3] == ',':  # argentinian currency format
            sanitized_float = sanitized_float.replace(
                '.', '').replace(',', '.')
        return float(sanitized_float)
