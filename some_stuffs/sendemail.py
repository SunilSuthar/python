import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("from", "password")
server.sendmail("from", "to", "Mail From Python")

