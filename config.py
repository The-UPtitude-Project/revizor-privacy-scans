import os, sys
from datetime import date
from openpyxl import Workbook


# Configuration settings:
CASE_SENSITIVE = False
HOMEPAGE_ONLY = True
NEW_URL_STARTING_ROW = 2

# LIMIT THE NUMBER OF PAGES TO SCRAPE
SHOULD_LIMIT = True # make this false if you want to scrape all the webpages
PAGE_LIMIT = 50 

# date today:
date_today = (date.today()).strftime("%Y-%m-%d")

# Check the name of the company we are scanning posts for:
if len(sys.argv) > 1:
    COMPANY_NAME = sys.argv[1]
else:
    COMPANY_NAME = None

HOST = "http://20.197.32.234"
PORT = "8000"

# the path:
path = "/home/revizor-project"


# Input file settings:
if COMPANY_NAME:
    FILE_PATH = f"{path}/input/privacy-scans/{COMPANY_NAME}/inventory.xlsx"
else:
    FILE_PATH = f"{path}/input/privacy-scans/all/inventory.xlsx"


INPUT_SHEET = 'Input'
INPUT_COLUMNS = ['URL']


# Output data settings:
output_path = f"{path}/output/privacy-scans"

# if not os.path.exists(output_path):
#     os.makedirs(output_path)

if COMPANY_NAME:
    OUTPUT_PATH = f"{output_path}/{COMPANY_NAME}/"
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    OUTPUT_FILE = f"{output_path}/{COMPANY_NAME}/output.xlsx"
else:
    OUTPUT_PATH = f"{output_path}/all/"
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    OUTPUT_FILE = f"{output_path}/all/output.xlsx"


if not os.path.exists(OUTPUT_FILE):
    workbook = Workbook()
    # workbook.active.title = 'Webpages'
    workbook.save(OUTPUT_FILE)



