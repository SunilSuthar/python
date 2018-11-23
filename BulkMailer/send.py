import smtplib, sys


class Mailer:

	def __init__(self,username,password):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.ehlo()
		self.server.login(username, password)

	def send(self, toEmail, message):
		self.server.sendmail('',toEmail,message)


###########################################################################

username=''
password=''

messageFile = 'message.txt'
emailFile = 'emails.txt'

mailer= Mailer(username,password)

message=open(messageFile).read()
with open(emailFile) as emailFileOpener:
	emails = emailFileOpener.readlines()

for email in emails:
	mailer.send(email,message)
	print('Sent:',email)

print('\ndone')
input('press any key to exit')
