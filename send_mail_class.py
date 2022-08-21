import smtplib 
from email.message import EmailMessage
'''
For outlook:
SMTP server: smtp-mail.outlook.com
SMTP Port: 587
'''
class Mail:
    def __init__(self):
        self.smtp_port = 587 # smtp port default
        self.smtp_server = "smtp-mail.outlook.com" # smtp server default
        self.main_mail = ""
        self.main_password = ""
    def sender_info(self,mail,password):
        self.main_mail = mail
        self.main_password = password
      
    def send(self,emails,subject,content):
        msg = EmailMessage()
        msg['Subject'] = subject # Subject of Email
        msg['From'] = self.main_mail
        msg['To'] = emails # Reciver of the Mail
        msg.set_content(content) # Email body or Content
        with smtplib.SMTP(self.smtp_server,self.smtp_port) as smtp:#Added mails SMTP Server
            smtp.starttls()
            smtp.login(self.main_mail,self.main_password) #This command Login SMTP Library using your MAIL
            smtp.send_message(msg) #This Sends the message
            smtp.quit()
