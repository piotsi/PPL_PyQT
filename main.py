import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Lab'
        self.windowWidth = 800
        self.windowHeight = 600
        self.setGeometry(300, 100, 800, 600)

        self.menu = Menu(self)
        self.tabs = Tabs(self)

        self.setCentralWidget(self.tabs)
        self.show()

    def openImage(self):
        self.tabs.tab1.layout.removeWidget(self.tabs.image)
        fname = QFileDialog.getOpenFileName(self, 'Open file',
         '',"Image files (*.jpg *.jpeg *.gif *.png)")[0]
        self.pixmap = QPixmap(fname)
        self.tabs.image = QLabel(self)
        self.tabs.image.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())

        if self.pixmap.width() < self.windowWidth:
            self.setFixedWidth(self.windowWidth)
        if self.pixmap.height() < self.windowHeight:
            self.setFixedHeight(self.windowHeight)

        self.tabs.image.setAlignment(Qt.AlignTop)
        self.tabs.image.setPixmap(self.pixmap)
        self.tabs.tab1.layout.addWidget(self.tabs.image)

    def clearText(self):
        self.tabs.textBox.setText('')
    
    def openText(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
         '',"Text files (*.txt)")[0]
        if fname == '':
            return
        self.tabs.currentFname = fname
        with open(fname, 'r') as f:
            self.tabs.textBox.setText(f.read())
    
    def saveText(self):
        with open(self.tabs.currentFname, 'w') as f:
            f.write(str(self.tabs.textBox.toPlainText()))

    def saveAsText(self):
        fname = QFileDialog.getSaveFileName(self, 'Open file',
         '',"Text files (*.txt)")[0]
        if fname == '':
            return
        self.tabs.currentFname = fname
        with open(fname, 'w') as f:
            f.write(str(self.tabs.textBox.toPlainText()))

    def clearInputs(self):
        self.tabs.fieldA.setText('')
        self.tabs.fieldB.setText('')
        self.tabs.fieldC.setValue(0)

    def updateOutput(self):
        self.tabs.fieldABC.setText(self.tabs.fieldA.text() + self.tabs.fieldB.text() + str(self.tabs.fieldC.text()))
    
class Menu(QMenuBar):
    def __init__(self, parent):
        super(QMenuBar, self).__init__(parent)
        self.menuBar = QMenuBar(self)
        self.menuBar.setNativeMenuBar(False)
        parent.setMenuBar(self.menuBar)
        self.parent = parent
        
        self.initActions()
        self.initMenu1()
        self.initMenu2()
        self.initMenu3()
        self.initMenu4()

    def initMenu1(self):
        fileMenu = QMenu("File", self)
        self.menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.exitActionM1) 

    def initMenu2(self):
        task1Menu = QMenu("Task 1", self)
        self.menuBar.addMenu(task1Menu)
        task1Menu.addAction(self.openActionM2)

    def initMenu3(self):
        task2Menu = QMenu("Task 2", self)
        self.menuBar.addMenu(task2Menu)
        task2Menu.addAction(self.clearActionM3)
        task2Menu.addAction(self.openActionM3)
        task2Menu.addAction(self.saveActionM3)
        task2Menu.addAction(self.saveAsActionM3)

    def initMenu4(self):
        task3Menu = QMenu("Task 3", self)
        self.menuBar.addMenu(task3Menu)
        task3Menu.addAction(self.clearActionM4)

    def initActions(self):
        self.exitActionM1 = QAction("&Exit", self)
        self.exitActionM1.triggered.connect(qApp.quit)
            
        self.openActionM2 = QAction("&Open", self)
        self.openActionM2.setShortcut('Ctrl+G')
        self.openActionM2.triggered.connect(self.parent.openImage)
        
        self.clearActionM3 = QAction("&Clear", self)
        self.clearActionM3.setShortcut('Ctrl+W')
        self.clearActionM3.triggered.connect(self.parent.clearText)

        self.openActionM3 = QAction("&Open", self)
        self.openActionM3.setShortcut('Ctrl+O')
        self.openActionM3.triggered.connect(self.parent.openText)

        self.saveActionM3 = QAction("&Save", self)
        self.saveActionM3.setShortcut('Ctrl+S')
        self.saveActionM3.triggered.connect(self.parent.saveText)

        self.saveAsActionM3 = QAction("&Save as", self)
        self.saveAsActionM3.setShortcut('Ctrl+K')
        self.saveAsActionM3.triggered.connect(self.parent.saveAsText)

        self.clearActionM4 = QAction("&Clear", self)
        self.clearActionM4.setShortcut('Ctrl+Q')
        self.clearActionM4.triggered.connect(self.parent.clearInputs)

class Tabs(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.parent = parent

        self.layout = QGridLayout()
        self.tabwidget = QTabWidget()
        self.tabwidget.resize(300, 300)

        self.layout.addWidget(self.tabwidget, 0, 0)
        self.setLayout(self.layout)

        self.initTab1()
        self.initTab2()
        self.initTab3()
    
    def initTab1(self):
        self.currentFname = "file.txt"
        self.tab1 = QWidget()
        self.tabwidget.addTab(self.tab1, "Task 1")
        self.tab1.layout = QGridLayout(self)
        self.image = QLabel(self)
        self.tab1.layout.addWidget(self.image)

        self.tab1.setLayout(self.tab1.layout)

    def initTab2(self):
        self.tab2 = QWidget()
        self.tabwidget.addTab(self.tab2, "Task 2")

        self.tab2.layout = QGridLayout(self)
        self.textBox = QTextEdit()
        self.tab2.layout.addWidget(self.textBox, 0,0,1,2)

        self.saveButton = QPushButton("&Save")
        self.tab2.layout.addWidget(self.saveButton, 1,0,1,1)
        self.saveButton.clicked.connect(self.parent.saveText)

        self.clearButton = QPushButton("&Clear")
        self.tab2.layout.addWidget(self.clearButton, 1,1,1,1)
        self.tab2.setLayout(self.tab2.layout)
        self.clearButton.clicked.connect(self.parent.clearText)

    def initTab3(self):
        self.tab3 = QWidget()
        self.tabwidget.addTab(self.tab3, "Task 3")
        self.tab3.layout = QFormLayout(self)
    
        self.fieldA = QLineEdit()
        self.fieldB = QLineEdit()
        self.fieldC = QSpinBox()
        self.fieldC.setRange(-2147483648, 2147483647)
        self.fieldABC = QLineEdit()
        self.fieldABC.setReadOnly(True)

        self.tab3.layout.addRow("Field A", self.fieldA)
        self.tab3.layout.addRow("Field B", self.fieldB)
        self.tab3.layout.addRow("Field C", self.fieldC)
        self.tab3.layout.addRow("Field A + B + C", self.fieldABC)        
        
        self.fieldA.textChanged.connect(self.parent.updateOutput)
        self.fieldB.textChanged.connect(self.parent.updateOutput)
        self.fieldC.textChanged.connect(self.parent.updateOutput)

        self.tab3.setLayout(self.tab3.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.setStyle('Windows')
    sys.exit(app.exec_())
