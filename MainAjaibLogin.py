# - * - coding: utf-8 - * -

# Implementasi formulir yang dihasilkan dari membaca file ui 'untitled.ui'
#
# Dibuat oleh: generator kode UI PyQt5 5.9.2
#
# PERINGATAN! Semua perubahan yang dibuat dalam file ini akan hilang!

dari PyQt5 impor QtCore, QtGui, QtWidgets

kelas  Ui_MainWindow ( objek ):
    def  setupUi ( self , MainWindow ):
        MainWindow.setObjectName ( " MainWindow " )
        MainWindow.resize ( 462 , 423 )
        icon = QtGui.QIcon ()
        icon.addPixmap (QtGui.QPixmap ( " ../../Downloads/hack.png " ), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon (ikon)
        self .centralwidget = QtWidgets.QWidget (MainWindow)
        self .centralwidget.setObjectName ( " centralwidget " )
        self .label_2 = QtWidgets.QLabel ( self .centralwidget)
        self .label_2.setGeometry (QtCore.QRect ( 11 , 161 , 177 , 17 ))
        self .label_2.setObjectName ( " label_2 " )
        self .label_3 = QtWidgets.QLabel ( self .centralwidget)
        self .label_3.setGeometry (QtCore.QRect ( 10 , 210 , 159 , 17 ))
        self .label_3.setObjectName ( " label_3 " )
        self .lineEdit_2 = QtWidgets.QLineEdit ( self .centralwidget)
        self .lineEdit_2.setGeometry (QtCore.QRect ( 200 , 160 , 261 , 21 ))
        self .lineEdit_2.setObjectName ( " lineEdit_2 " )
        self .lineEdit_3 = QtWidgets.QLineEdit ( self .centralwidget)
        self .lineEdit_3.setGeometry (QtCore.QRect ( 200 , 210 , 261 , 21 ))
        self .lineEdit_3.setObjectName ( " lineEdit_3 " )
        self .label_4 = QtWidgets.QLabel ( self .centralwidget)
        self .label_4.setGeometry (QtCore.QRect ( 140 , 110 , 191 , 21 ))
        palet = QtGui.QPalette ()
        brush = QtGui.QBrush (QtGui.QColor ( 239 , 41 , 41 ))
        brush.setStyle (QtCore.Qt.SolidPattern)
        palette.setBrush (QtGui.QPalette.Active, QtGui.QPalette.Text, sikat)
        brush = QtGui.QBrush (QtGui.QColor ( 239 , 41 , 41 ))
        brush.setStyle (QtCore.Qt.SolidPattern)
        palette.setBrush (QtGui.QPalette.Inactive, QtGui.QPalette.Text, sikat)
        brush = QtGui.QBrush (QtGui.QColor ( 190 , 190 , 190 ))
        brush.setStyle (QtCore.Qt.SolidPattern)
        palette.setBrush (QtGui.QPalette.Disabled, QtGui.QPalette.Text, sikat)
        self .label_4.setPalette (palet)
        font = QtGui.QFont ()
        font.setItalic ( True )
        self .label_4.setFont (font)
        self .label_4.setObjectName ( " label_4 " )
        self .label_5 = QtWidgets.QLabel ( self .centralwidget)
        self .label_5.setGeometry (QtCore.QRect ( 10 , 260 , 159 , 17 ))
        self .label_5.setObjectName ( " label_5 " )
        self .lineEdit_4 = QtWidgets.QLineEdit ( self .centralwidget)
        self .lineEdit_4.setGeometry (QtCore.QRect ( 200 , 260 , 261 , 21 ))
        self .lineEdit_4.setObjectName ( " lineEdit_4 " )
        self .pushButton_2 = QtWidgets.QPushButton ( self .centralwidget)
        self .pushButton_2.setGeometry (QtCore.QRect ( 240 , 350 , 81 , 41 ))
        self .pushButton_2.setAutoFillBackground ( Salah )
        self .pushButton_2.setStyleSheet ( " QPushButton { \ n "
"     background-color: rgb (114, 159, 207); \ n "
" } " )
        self .pushButton_2.setObjectName ( " pushButton_2 " )
        self .label_6 = QtWidgets.QLabel ( self .centralwidget)
        self .label_6.setGeometry (QtCore.QRect ( 10 , 360 , 159 , 17 ))
        self .label_6.setObjectName ( " label_6 " )
        self .lineEdit_5 = QtWidgets.QLineEdit ( self .centralwidget)
        self .lineEdit_5.setGeometry (QtCore.QRect ( 160 , 360 , 61 , 21 ))
        self .lineEdit_5.setObjectName ( " lineEdit_5 " )
        self .label_7 = QtWidgets.QLabel ( self .centralwidget)
        self .label_7.setGeometry (QtCore.QRect ( 150 , 10 , 171 , 31 ))
        font = QtGui.QFont ()
        font.setFamily ( " Courier 10 Pitch " )
        self .label_7.setFont (font)
        self .label_7.setObjectName ( " label_7 " )
        self .label_8 = QtWidgets.QLabel ( self .centralwidget)
        self .label_8.setGeometry (QtCore.QRect ( 10 , 310 , 159 , 17 ))
        self .label_8.setObjectName ( " label_8 " )
        self .lineEdit_6 = QtWidgets.QLineEdit ( self .centralwidget)
        self .lineEdit_6.setGeometry (QtCore.QRect ( 200 , 310 , 261 , 21 ))
        self .lineEdit_6.setObjectName ( " lineEdit_6 " )
        self .pushButton_3 = QtWidgets.QPushButton ( self .centralwidget)
        self .pushButton_3.setGeometry (QtCore.QRect ( 350 , 350 , 81 , 41 ))
        self .pushButton_3.setStyleSheet ( " QPushButton { \ n "
"     background-color: rgb (239, 41, 41); \ n "
" } " )
        self .pushButton_3.setObjectName ( " pushButton_3 " )
        self .widget = QtWidgets.QWidget ( self .centralwidget)
        self .widget.setGeometry (QtCore.QRect ( 11 , 56 , 451 , 41 ))
        self .widget.setObjectName ( " widget " )
        self .horizontalLayout = QtWidgets.QHBoxLayout ( self .widget)
        self .horizontalLayout.setContentsMargins ( 0 , 0 , 0 , 0 )
        self .horizontalLayout.setObjectName ( " horizontalLayout " )
        diri .label = QtWidgets.QLabel ( diri .widget)
        self .label.setObjectName ( " label " )
        self .horizontalLayout.addWidget ( self .label)
        self .lineEdit = QtWidgets.QLineEdit ( self .widget)
        self .lineEdit.setObjectName ( " lineEdit " )
        self .horizontalLayout.addWidget ( self .lineEdit)
        self .pushButton = QtWidgets.QPushButton ( self .widget)
        self .pushButton.setObjectName ( " pushButton " )
        self .horizontalLayout.addWidget ( self .pushButton)
        MainWindow.setCentralWidget ( self .centralwidget)
        self .menubar = QtWidgets.QMenuBar (MainWindow)
        self .menubar.setGeometry (QtCore.QRect ( 0 , 0 , 462 , 22 ))
        self .menubar.setObjectName ( " menubar " )
        MainWindow.setMenuBar ( self .menubar)

        self .retranslateUi (MainWindow)
        self .pushButton.clicked.connect ( self .lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName (MainWindow)
        MainWindow.setTabOrder ( self. LineEdit, self .pushButton)
        MainWindow.setTabOrder ( self .pushButton, self .lineEdit_2)
        MainWindow.setTabOrder ( self .lineEdit_2, self .lineEdit_3)
        MainWindow.setTabOrder ( self .lineEdit_3, self .lineEdit_4)
        MainWindow.setTabOrder ( self .lineEdit_4, self .lineEdit_6)
        MainWindow.setTabOrder ( self .lineEdit_6, self .lineEdit_5)
        MainWindow.setTabOrder ( self .lineEdit_5, self .pushButton_2)

    def  retranslateUi ( self , MainWindow ):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle (_translate ( " MainWindow " , " MainWindow " ))
        self .label_2.setText (_translate ( " MainWindow " , " Enter UserName of target " ))
        self .label_3.setText (_translate ( " MainWindow " , " Masukkan CSS dari UserName " ))
        self .label_4.setText (_translate ( " MainWindow " , " <! DOCTYPE HTML PUBLIC \" - // W3C // DTD HTML 4.0 // EN \ "  \" http://www.w3.org/TR/REC- html40 / strict.dtd \ " > \ n "
" <html> <head> <meta name = \" qrichtext \ " content = \" 1 \ " /> <jenis gaya = \" teks / css \ " > \ n "
" p, li {white-space: pre-wrap;} \ n "
" </ style> </ head> <body style = \" font-family: \ ' Ubuntu \' ; ukuran font: 11pt; font-weight: 400; font-style: italic; \ " > \ n "
" <p style = \" margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-block-indent: 0; text-indent: 0px; \ " > <span style = \" text-decoration: garis bawah; warna: # ef2929; \ " > Harap Isi semua detail </ span> </ p> </ body> </ html> " ))
        self .label_5.setText (_translate ( " MainWindow " , " Masukkan CSS Kata Sandi " ))
        self .pushButton_2.setText (_translate ( " MainWindow " , " Mulai " ))
        self .label_6.setText (_translate ( " MainWindow " , " Setel rate untuk setiap kunci " ))
        self .label_7.setText (_translate ( " MainWindow " , " <html> <head /> <body> <p align = \" center \ " > <span style = \" ukuran-huruf: 20pt; font-weight: 600 ; teks-dekorasi: garis bawah; warna: # 204a87; \ " > HACK-IT </ span> </ p> </ body> </ html> " ))
        self .label_8.setText (_translate ( " MainWindow " , " Masukkan CSS dari Kirim " ))
        self .pushButton_3.setText (_translate ( " MainWindow " , " STOP " ))
        self .label.setText (_translate ( " MainWindow " , " Enter URL " ))
        self .pushButton.setText (_translate ( " MainWindow " , " Clear " ))


jika  __name__  ==  " __main__ " :
    impor sys
    app = QtWidgets.QApplication (sys.argv)
    MainWindow = QtWidgets.QMainWindow ()
    ui = Ui_MainWindow ()
    ui.setupUi (MainWindow)
    MainWindow.show ()
    sys.exit (app.exec_ ())
