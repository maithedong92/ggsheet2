SERVER = "mail.namanmarket.com.vn"
FROM = "dong.mt@namanmarket.com.vn"
TO = ["binh.tt@namanmarket.com.vn", "sales@namanmarket.com.vn"] # must be a list

SUBJECT = "Subject"
TEXT = "Your Text"

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()