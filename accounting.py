import os, sys

app_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{app_path}/lib/")

from modules.accounting import Accounting

if __name__ == "__main__":
    accounting = Accounting()
    accounting.collate_bank_data()
