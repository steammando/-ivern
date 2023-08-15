from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/jin/git/ivern/ivern-393003-be3c49a9d796.json', scope) # 나중에 서버키 위치로 변경해야함
gc = gspread.authorize(credentials)

gc1 = gc.open("ivern project").worksheet('parts_gatcha')
gc2 = gc1.get_all_values()

# @TODO 현재 시트의 모든 내용을 불러오는데 카테고리별로 불러올 수 있도록 변경 필요
def open_sheet(sheet_name):
    sheet = gc.open("ivern project").worksheet(sheet_name)
    result = sheet.get_all_values()
    return(result)