from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(
    "credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1t7iOjmWEitEz6_E1g-YqqB7UiWM5OzVvmlAJCQQqiEY"
sheet = client.open_by_key(sheet_id)

values_list = sheet.sheet1.col_values(1)
current_row = len(values_list) + 1

sheet.sheet1.update_cell(current_row, 1, str(datetime.now()))

values_list = sheet.sheet1.col_values(1)

print(values_list)
