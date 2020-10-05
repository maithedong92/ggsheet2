#tao 1 spreadsheet moi bang tai khoan service va share voi tai khoan chinh

#import thu vien google spread
import gspread
#goi api xac thuc tai khoan bla bla bla
gc = gspread.service_account()

#lenh bat dau tu day


#tao sheet moi bang servicer account
sh = gc.create('A new spreadsheet')


#chia se sheet voi acc chinh. kiem tra thu muc chia se trong ggdrive, co the su dung role owner
sh.share('2susulucky@gmail.com', perm_type='user', role='writer')

#in noi dung cua sheet1 o A1
print(sh.sheet1.get('A1'))