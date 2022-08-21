import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from mail_gonder_design import * #ui design'ın import edilmesi
from send_mail_class import Mail

if __name__ == '__main__':
            
    # Uİ Kurulumu
    app = QApplication(sys.argv) # uygulamayı oluşturduk
    win = QMainWindow() # pencere tanımlandı
    ui = Ui_MainWindow() # Ui elementlerine ulaştık
    ui.setupUi(win) # pencerede göstermek için kurduk
    win.show() # göster
    email = Mail()# Mail sınıfının nesnesi
    status = False
    def send_email ():
        
        mail = ui.senderMail_txt.text() # göndericinin mail adresi
        password = ui.senderPassword_txt.text() #göndericinin mail şifresi
        emails = ui.reciver_txt.text()
        subject = ui.subject_txt.text()
        content = ui.content_txt.toPlainText()
        
       
        try:
            email.sender_info(mail, password) # gönderen kişinin bilgilerini ayarlar.
            email.send(emails,subject,content)
            ui.statusbar.showMessage("mail gönderme işlemi başarı ile tamamlandı",8000)
        except Exception as error:
            ui.statusbar.showMessage("mail gönderme başarısız oldu"+ str(error))

    ui.sendMail_btn.clicked.connect(send_email)
    ui.sendMail_btn.setStatusTip("Yeni mail göndermek için tıklayınız (Bilgileri eksiksiz girdiğinizden emin olunuz)")


    sys.exit(app.exec_()) # uygulamayı sonlandır (koşul = çıkış yapılana kadar pencere açık kalır.)