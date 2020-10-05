#tao 1 spreadsheet moi bang tai khoan service va share voi tai khoan chinh

#import thu vien google spread
import gspread
#goi api xac thuc tai khoan bla bla bla
gc = gspread.service_account()

#lenh bat dau tu day

#mo file bang key
sh = gc.open_by_key('1nLxY3qyJU53nCggLd70bTa44m0HuULkBLMjmxuJwlNQ')
#chon sheet bang ten
worksheet = sh.worksheet("Trang tính3")

#get all values as list of list
list_of_lists = worksheet.get_all_values()
print(list_of_lists)