from oauth2client.service_account import ServiceAccountCredentials
import gspread
import re

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
# credentials = ServiceAccountCredentials.from_json_keyfile_name(
        # '/Users/jin/git/ivern/ivern-393003-be3c49a9d796.json', scope) # local test key
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '/home/ubuntu/ivern/google_sheet_key.json', scope)
gc = gspread.authorize(credentials)

def open_sheet(sheet_name):
    result = {}
    sheet = gc.open("ivern project").worksheet(sheet_name)
    # result[sheet_name] = sheet.get('A2:Z')
    result = sheet.get_all_values()
    return(result)

def read_all_sheet():
    result = {}
    sheet = gc.open("ivern project")
    sheet_list = sheet.worksheets()
    for s in sheet_list:
        values = s.get('A2:Z')
        result[s.title] = values
    return(result)