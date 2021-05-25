__author__ = "Tooraj_Jahangiri"
__email__ = "toorajjahangiri@gmail.com"


# IMPORT
import os.path as iPath
import sqlite3

# IMPORT TYPE HINT
from typing import Generator, Iterable

# IMPORT CORE
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem

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

    SQL_TABLE_LOAD: str = None
    CONN: sqlite3.Connection = None

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

        # Signal Connect
        self.cmb_tableName.currentTextChanged.connect(self.__tableChange)

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
            self.addTableName()
        
        elif self.FORMAT == 'csv':
            self.loadCsv()

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

    def __tableChange(self, table: str) -> None:
        """
        """
        self.SQL_TABLE_LOAD = table
       # print(f"{self.SQL_TABLE_LOAD= }")
        self.loadSqlite()

    def addTableName(self) -> None:
        """
        Add Table Name To ComboBox
        """
        self.CONN = self.db_sqlite.connect(self.FILE_PATH)
        get_tableName = self.CONN.execute("SELECT name FROM sqlite_master WHERE type = ? AND name NOT LIKE ?", ('table', 'sqlite_%'))
        tableName: list[str] = [i[0] for i in get_tableName]
        
        #print(f"{tableName= }")
        
        for t in tableName:
            self.cmb_tableName.addItem(t)

    def existsTable(self) -> bool:
        """
        If Exists Table 'True' Else 'False'
        """
        if self.SQL_TABLE_LOAD is not None:
            script: str = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{self.SQL_TABLE_LOAD}'"
            exists = bool(next(self.CONN.execute(script))[0])
            #print(f"{exists= }")
            
            return exists

    def setHeaders(self) -> None:
        """
        Set Table Header Lables
        """
        script = f"SELECT name FROM PRAGMA_TABLE_INFO('{self.SQL_TABLE_LOAD}');"
        getLabel: list = [l[0] for l in self.CONN.execute(script)]
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(getLabel))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(getLabel)
        
        #print(f"{getLabel=}")

    def tableItemSql(self) -> Generator:
        """
        Generate New Row with TableWidgetItem From SQLITE3
        """
        #print("-- TABLEITEM --")
        script: str = f"SELECT * FROM {self.SQL_TABLE_LOAD}"
        getAll: Iterable = self.CONN.execute(script).fetchall()
       
        #print("GET ALL", *getAll)
       
        for row in getAll:
            newRow: list = [QTableWidgetItem(str(it)) for it in row]
            #print(f"{newRow= }")
            yield newRow

    def toTable(self, data) -> None:
        """
        Insert Data To Table
        """
        #print("--> TO TABLE <--")
        for row, item in enumerate(data):
            self.tableWidget.insertRow(row)
            for column, it in enumerate(item):
                self.tableWidget.setItem(row, column, it)
            #print(f"{row= }\t{column= }\t{item= }")

    def loadSqlite(self) -> None:
        """
        Load Data From Sqlite3 DataBase
        """
        
        if self.existsTable():
            self.setHeaders()
            self.tableItemSql()
            self.toTable(self.tableItemSql())

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

    def openCsv(self) -> Generator:
        """
        Open Csv Generate Row type List
        """
        with open(self.FILE_PATH, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.removesuffix('\n')
                yield line.split('\t')

    def tableItemCsv(self) -> Generator:
        """
        Generate item To tableWidgetItem
        """
        for line in self.openCsv():
            newRow = [QTableWidgetItem(str(it)) for it in line]
            yield newRow

    def loadCsv(self) -> None:
        """
        Load Csv File
        """
        self.toTable(self.tableItemCsv())

    def exportSqlite(self) -> None:
        """
        """
        pass

    def exportCsv(self) -> None:
        """
        """
        pass
