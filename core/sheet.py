from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/jin/git/ivern/ivern-393003-be3c49a9d796.json', scope) # 나중에 서버키 위치로 변경해야함
gc = gspread.authorize(credentials)

gc1 = gc.open("ivern project").worksheet('parts_gatcha')
gc2 = gc1.get_all_values()

def open_sheet(sheet_name):
    sheet = gc.open("ivern project").worksheet(sheet_name)
    result = sheet.get_all_values()
    return(result)