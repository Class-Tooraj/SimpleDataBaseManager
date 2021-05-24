__author__ = "Tooraj_Jahangiri"
__email__ = "toorajjahangiri@gmail.com"


# IMPORT
from os import path
import os.path as iPath
import sqlite3

# IMPORT CORE
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog

# IMPORT UI
try:
    from gui.__dbmanager import Ui_MainWindow as _mainWindow
    from PySide6.QtWidgets import QMainWindow as _base

except ImportError:

    from PySide6.QtUiTools import loadUiType
    _path = iPath.dirname(__file__)
    _base , _mainWindow = loadUiType(iPath.join(_path, "widgets/mainWindow.ui"))

print(f"{_base= }\t{_mainWindow= }\n{type(_base).__name__= }\t{type(_mainWindow).__name__= }")

# --- BACKEND ---

locate = iPath.dirname(__file__)

# MAIN WINDOW CLASS
class MainWindow(_base, _mainWindow):
    """
    """
    CURRENT_PATH = locate
    FILE_PATH:str = None
    FORMAT: str = None

    def __init__(self, *args, **kwargs) -> None:
        """
        """
        # Initialize
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.dialogFiles = QFileDialog(self)

        self.timer: QTimer = QTimer(self)
        self.__actions()

        self.db_sqlite = sqlite3

    def __actions(self) -> None:
        """
        """
        # File Menu
        self.actionNew.triggered.connect(self.__new)
        self.actionOpen.triggered.connect(self.__open)
        self.actionSave.triggered.connect(self.__save)
        self.actionSaveAs.triggered.connect(self.__saveAs)
        self.actionExit.triggered.connect(self.__exit)
        # Table Menu
        self.actionAddRow.triggered.connect(self.__addRow)
        self.actionAddColumn.triggered.connect(self.__addColumn)
        self.actionDelRow.triggered.connect(self.__delRow)
        self.actionDelColumn.triggered.connect(self.__delColumn)
        # Help Menu
        self.actionAbout.triggered.connect(self.__about)

    def __new(self) -> None:
        """
        """
        self.__saveAs()
        
        if self.FORMAT == 'csv':
            with open(self.FILE_PATH, 'w') as f:
                f.close()
        
        if self.FORMAT == 'sqlite':
            self.db_sqlite.connect(self.FILE_PATH)

    def __open(self) -> None:
        """
        """
        filter: str = "Sqlite3 (*.db);;Csv (*.csv);;Custom Sqlite3 (*.*);;Custom Table (*.*)"
        path, form = self.dialogFiles.getOpenFileName(self, "Load Table", self.CURRENT_PATH, filter)
        self.FILE_PATH = path
        self.FORMAT = 'sqlite' if "Sqlite3" in form else 'csv'
        
        print(f"{path= }\t{form = }")

        if self.FORMAT == 'sqlite':
            self.loadSqlite()
        
        elif self.FORMAT == 'csv':
            self.loadSqlite()

    def __save(self) -> None:
        """
        """
        if self.FORMAT == 'sqlite':
            self.exportSqlite()
        
        elif self.FORMAT == 'csv':
            self.exportCsv()

    def __saveAs(self) -> None:
        """
        """
        filter: str = "Sqlite3 (*.db);;Csv (*.csv);;Custom Sqlite3 (*.*);;Custom Table (*.*)"
        path, form = self.dialogFiles.getSaveFileName(self, "Save Table", self.CURRENT_PATH, filter)
        self.FILE_PATH = path
        self.FORMAT = 'sqlite' if "Sqlite3" in form else 'csv'
        
        print(f"{path= }\t{form = }")

        if self.FORMAT == 'sqlite':
            self.exportSqlite()
        
        elif self.FORMAT == 'csv':
            self.exportCsv()

    def __addRow(self) -> None:
        """
        """
        newRow = self.tableWidget.currentRow() + 1
        self.tableWidget.insertRow(newRow)

    def __addColumn(self) -> None:
        """
        """
        newColumn = self.tableWidget.currentColumn() + 1
        self.tableWidget.insertColumn(newColumn)

    def __delRow(self) -> None:
        """
        """
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def __delColumn(self) -> None:
        """
        """
        self.tableWidget.removeColumn(self.tableWidget.currentColumn())


    def __about(self) -> None:
        """
        """
        pass

    def __exit(self) -> None:
        """
        """
        self.close()

    def loadSqlite(self) -> None:
        """
        """
        conn = self.db_sqlite.connect(self.FILE_PATH)
        tableName = conn.execute("SELECT name FROM sqlite_master WHERE type = ? AND name NOT LIKE ?", ('table', 'sqlite_%'))
        print(f"{tableName= }", *tableName)
    
    def loadCsv(self) -> None:
        """
        """
        pass

    def exportSqlite(self) -> None:
        """
        """
        pass

    def exportCsv(self) -> None:
        """
        """
        pass




# create sqlite test db
def create_sqlite():
    mypath = iPath.join(locate, "test.db")
    conn = sqlite3.connect(mypath)
    tble = (
        "CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, name TEXT)",
        "CREATE TABLE IF NOT EXISTS Magic (id INTEGER PRIMARY KEY, user TEXT)",
        )
    for i in tble:
        conn.execute(i)
    
    user = (
        (1, "Tooraj"),
        (2, "Iraj"),
    )
    magic = (
        (1, "1234562"),
        (2, "5556663"),
    )
    
    for i in user:
        script = "INSERT INTO User VALUES (?, ?)"
        conn.execute(script, i)
  
    for i in magic:
        script = "INSERT INTO Magic VALUES (?, ?)"
        conn.execute(script, i)

#create_sqlite()
