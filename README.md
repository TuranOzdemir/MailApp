# MailApp
This application allows you to send e-mails to different e-mail addresses using your outlook account.if you want to send mail with your outlook account using python in your own application. You can look into the send_mail_class I created or use it as is. Also, if you want to use an e-mail account other than outlook, go now and look into the code, you can do it with a few changes. But I have to remind you that the Gmail account was not available when I was writing this code, but with the new update, you need to get an application password and use this password in smtp, you can check the "https://exerror.com/smtplib-smtpauthenticationerror-username-and-password-not-accepted/" address for more information.

Note: You dont need to install smtplib, it's installed with python

I use QtDesigner for the ui and use a converter to convert ui to python. if you want to redesign and convert, you can use the code below 
"""
from PyQt5 import uic

with open("mail_gonder_design.py","w",encoding='utf-8') as fout:
    uic.compileUi("mail_gonder_design.ui", fout)
"""
