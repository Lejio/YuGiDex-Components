from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from sidebar.SideBar import SideBar
import sys


class MainWindow(QMainWindow):
    
    def __init__(self):
        
        super(MainWindow, self).__init__()
        
        self.setGeometry(100, 100, 800, 800)
        self.setMinimumSize(400, 400)
        
        self.topBar = QWidget()
        self.topBar.setFixedHeight(30)
        # self.topBar.setStyleSheet("""
        #                    background-color: #f397d6;
        #                    """)
        self.mainContent = QWidget()
        # self.mainContent.setStyleSheet("""
        #                                background-color: #f397d6;
        #                                """)
        self.mainContentLayout = QHBoxLayout()
        self.mainContentLayout.setSpacing(0)
        self.mainContentLayout.setContentsMargins(0, 0, 0, 0)
        
        self.sideBar = SideBar(height=self.height())
        # self.sideBar.setStyleSheet("""
        #                            background-color: #f42272;
        #                            """)
        self.content = QWidget()
        self.setStyleSheet("""
                            background-color: #fcfffc;
                            """)
        
        self.mainContentLayout.addWidget(self.sideBar)
        self.mainContentLayout.addWidget(self.content)
        self.mainContent.setLayout(self.mainContentLayout)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.topBar)
        self.mainLayout.addWidget(self.mainContent)
        
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        
        self.setCentralWidget(self.mainWidget)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    window.show()
    
    app.exec()