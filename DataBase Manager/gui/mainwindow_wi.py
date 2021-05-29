__author__ = "Tooraj_Jahangiri"
__email__ = "toorajjahangiri@gmail.com"


# IMPORT
import os.path as iPath
import sqlite3

# IMPORT TYPE HINT
from typing import Generator, Iterable

# IMPORT CORE
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox

# IMPORT UI
try:
    from gui.__dbmanager import Ui_MainWindow as _mainWindow
    from PySide6.QtWidgets import QMainWindow as _base

except ImportError as err:
    print(f"{err =}\t{type(err).__name__}")

    from PySide6.QtUiTools import loadUiType
    _path = iPath.dirname(__file__)
    _base , _mainWindow = loadUiType(iPath.join(_path, "widgets/mainWindow.ui"))

print(f"{_base= }\t{_mainWindow= }\n{type(_base).__name__= }\t{type(_mainWindow).__name__= }")

# --- BACKEND ---

locate = iPath.dirname(__file__)

# MAIN WINDOW CLASS
class MainWindow(_base, _mainWindow):
    """
    DataBase Manager MainWindow
    """
    VERSION: tuple[str, str, str] = ('1.00-R', 'Ready', ':)')

    CURRENT_PATH = locate
    FILE_PATH:str = None
    FORMAT: str = None

    SQL_TABLE_LOAD: str = None
    SQL_LOAD_COLUMN: str = None
    ALL_TABLE: list[str] = None
    CONN: sqlite3.Connection = None

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize DataBase Manager Simple Gui
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
        Connect Actions Signal
        """
        # File Menu
        self.actionNew.triggered.connect(self.__new)
        self.actionOpen.triggered.connect(self.__open)
        self.actionSave.triggered.connect(self.__save)
        self.actionSaveAs.triggered.connect(self.__saveAs)
        self.actionExit.triggered.connect(self.__exit)
      
        # Table Menu
        self.actionNewTable.triggered.connect(self.__newTable)
        self.actionLoadTable.triggered.connect(self.loadSqlite)
        self.actionSaveTable.triggered.connect(self.__save)
        self.actionAddRow.triggered.connect(self.__addRow)
        self.actionAddColumn.triggered.connect(self.__addColumn)
        self.actionDelRow.triggered.connect(self.__delRow)
        self.actionDelColumn.triggered.connect(self.__delColumn)
      
        # Help Menu
        self.actionAbout.triggered.connect(self.__about)

        # Signal Connect
        self.cmb_tableName.currentTextChanged.connect(self.__tableChange)

        # Button Connect
        self.btn_newTable.clicked.connect(self.__newTable)
        self.btn_loadTable.clicked.connect(self.loadSqlite)
        self.btn_saveTable.clicked.connect(self.__save)

    def __algorithm(self) -> None:
        """
        Set Algorithm Name And Set 'Enabled'
        """
        _name: dict = {'csv': "CSV", 'sqlite': "SQLITE-3", None: 'None'}
        self.lbl_algorithm.setText(_name[self.FORMAT])
        
        if self.FORMAT == 'csv':
           
            self.btn_loadTable.setEnabled(False)
            self.btn_saveTable.setEnabled(False)
            self.btn_newTable.setEnabled(False)
            self.cmb_tableName.setEnabled(False)

            self.actionNewTable.setEnabled(False)
            self.actionSaveTable.setEnabled(False)
            self.actionLoadTable.setEnabled(False)

            self.actionAddColumn.setEnabled(True)
            self.actionDelColumn.setEnabled(True)

        elif self.FORMAT == 'sqlite':
           
            self.btn_loadTable.setEnabled(True)
            self.btn_saveTable.setEnabled(True)
            self.btn_newTable.setEnabled(True)
            self.cmb_tableName.setEnabled(True)

            self.actionNewTable.setEnabled(True)
            self.actionSaveTable.setEnabled(True)
            self.actionLoadTable.setEnabled(True)

            self.actionAddColumn.setEnabled(False)
            self.actionDelColumn.setEnabled(False)

    def __newTable(self) -> None:
        """
        Clear Table for New One
        """
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)

    def __new(self) -> None:
        """
        New File
        """
        
        if self.FILE_PATH != None:
            saveQuestion = QMessageBox(self)
            act = saveQuestion.question(self, "Save Question", "Do You Want to Save Table ?", QMessageBox.Yes, QMessageBox.No)

            if act == saveQuestion.Yes:
                self.__save()
            else:
                saveQuestion.close()

        self.FILE_PATH = None
        self.ALL_TABLE = None
        self.FORMAT = None
        self.CONN = None
        self.__algorithm()
        self.cmb_tableName.clear()
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)

        self.__saveAs()

        if self.FORMAT == 'csv':
            if iPath.isfile(self.FILE_PATH) != True and self.FILE_PATH != '':
                with open(self.FILE_PATH, 'w') as f:
                    f.close()
        
        if self.FORMAT == 'sqlite':
            self.db_sqlite.connect(self.FILE_PATH)

    def __open(self) -> None:
        """
        Open Dialog
        """
        if self.FILE_PATH != None:
            saveQuestion = QMessageBox(self)
            act = saveQuestion.question(self, "Save Question", "Do You Want to Save Table ?", QMessageBox.Yes, QMessageBox.No)

            if act == saveQuestion.Yes:
                self.__save()
            else:
                saveQuestion.close()

        filter: str = "Sqlite3 (*.db);;Csv (*.csv);;Custom Sqlite3 (*.*);;Custom Table (*.*)"
        path, form = self.dialogFiles.getOpenFileName(self, "Load Table", self.CURRENT_PATH, filter)
        self.FILE_PATH = path
        self.FORMAT = 'sqlite' if "Sqlite3" in form else 'csv'
        
        #print(f"{path= }\t{form = }")
        if path != '':
            self.ALL_TABLE = None
            self.CONN = None
            self.__algorithm()
            self.cmb_tableName.clear()
            self.tableWidget.clear()
            
            if self.FORMAT == 'sqlite':
                self.addTableName()
            
            elif self.FORMAT == 'csv':
                self.loadCsv()
            
            self.__algorithm()

    def __save(self) -> None:
        """
        Save Table
        """
        if self.FILE_PATH != None:
            if self.FORMAT == 'sqlite':
                self.exportSqlite(self.FILE_PATH)
        
            elif self.FORMAT == 'csv':
                self.exportCsv(self.FILE_PATH)
        
        else:
            self.__saveAs()

    def __saveAs(self) -> None:
        """
        Save As Other Path Table
        """
        filter: str = "Sqlite3 (*.db);;Csv (*.csv);;Custom Sqlite3 (*.*);;Custom Table (*.*)"
        path, form = self.dialogFiles.getSaveFileName(self, "Save Table", self.CURRENT_PATH, filter)
        self.FILE_PATH = path
        self.FORMAT = 'sqlite' if "Sqlite3" in form else 'csv'
        
        #print(f"{path= }\t{form = }")
        if path != '':
            if self.FORMAT == 'sqlite':
                self.exportSqlite(path)
            
            elif self.FORMAT == 'csv':
                self.exportCsv(path)
            
            self.__algorithm()

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
        Sqlite Table Change
        """
        if self.FORMAT == 'sqlite':
            self.SQL_TABLE_LOAD = table

    def toTable(self, data) -> None:
        """
        Insert Data To Table
        """
        if self.FORMAT == 'csv':
            self.tableWidget.clear()
        
        self.tableWidget.setRowCount(0)

        sizeLines: list[int] = []
        for row, item in enumerate(data):
            sizeLines.append(len(item))
            self.tableWidget.insertRow(row)
            for column, it in enumerate(item):
                self.tableWidget.setItem(row, column, it)
            #print(f"{row= }\t{column= }\t{item= }")
        if self.FORMAT == 'csv':
            self.tableWidget.setColumnCount(max(sizeLines))
        
        del sizeLines, row, item, column, it

    def addTableName(self) -> None:
        """
        Add Table Name To ComboBox
        """
        self.cmb_tableName.clear()
        self.cmb_tableName.addItem('')

        self.CONN = self.db_sqlite.connect(self.FILE_PATH)
        get_tableName = self.CONN.execute("SELECT name FROM sqlite_master WHERE type = ? AND name NOT LIKE ?", ('table', 'sqlite_%'))
        self.ALL_TABLE: list[str] = [i[0] for i in get_tableName]

        script_get_pattern: str = "SELECT * FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
        self.SQL_LOAD_COLUMN: str = tuple(self.CONN.execute(script_get_pattern))[0][-1]
        print(f"{self.SQL_LOAD_COLUMN= }")
        
        for t in self.ALL_TABLE:
            self.cmb_tableName.addItem(t)

    def existsTable(self) -> bool:
        """
        If Exists Table 'True' Else 'False'
        """
        if self.ALL_TABLE is not None:
            if self.SQL_TABLE_LOAD in self.ALL_TABLE:
                script: str = f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{self.SQL_TABLE_LOAD}'"
                exists = bool(next(self.CONN.execute(script))[0])
                #print(f"{exists= }")
            
                return exists
        
        return False

    def setHeaders(self) -> None:
        """
        Set Table Header Lables
        """
        script = f"SELECT name FROM PRAGMA_TABLE_INFO('{self.SQL_TABLE_LOAD}');"
        getLabel: list = [l[0] for l in self.CONN.execute(script)]
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(getLabel))
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

    def loadSqlite(self) -> None:
        """
        Load Data From Sqlite3 DataBase
        """
        if self.SQL_TABLE_LOAD != None:
            saveQuestion = QMessageBox(self)
            act = saveQuestion.question(self, "Save Question", "Do You Want to Save Table ?", QMessageBox.Yes, QMessageBox.No)

            if act == saveQuestion.Yes:
                self.__save()
            else:
                saveQuestion.close()
        
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
        try:
            with open(self.FILE_PATH, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.removesuffix('\n')
                    #print(f"{line=}")
                    yield line.split('\t')
        except (FileNotFoundError, FileExistsError, IsADirectoryError, IOError) as errfile:
            raise errfile
        
        finally:
            f.close()
            del lines, f

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

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def getFromTable(self) -> Generator:
        """
        Get Data From Table
        """
        column_range: int = self.tableWidget.columnCount()
        row_range: int = self.tableWidget.rowCount()
        
        for row in range(0, row_range):
            line: list = []
            for column in range(0, column_range):
                value = self.tableWidget.item(row, column)
                if value in (None, "None", "NoneType"):
                    line.append('')
                
                else:
                    line.append(value.text())
           
            yield line
            line.clear()

    def updateSqliteTable(self) -> None:
        """
        Update Table Value
        """
        getColumn: tuple = tuple(self.tableWidget.horizontalHeaderItem(i).text() for i in range(0, self.tableWidget.columnCount()))
        #print(f"{getColumn= }")
        
        valS: str = ", ".join((f':{num}' for num in range(0, len(getColumn))))
        rows: Generator = self.getFromTable()
        
        toMap: dict = lambda x: {f"{i}": v for i, v in enumerate(x)}

        for row in rows:
            update_script: str = f"INSERT OR REPLACE INTO {self.SQL_TABLE_LOAD} VALUES({valS})"
            self.CONN.execute(update_script, toMap(row))
            self.CONN.commit()
            
            #print(f"updateRow >> {row= }")

    def addSqliteTable(self) -> None:
        """
        Create New Table In DataBase And Set Data
        """
        rows: Generator = self.getFromTable()
        
        column: tuple[str] = tuple(next(rows)) if self.SQL_LOAD_COLUMN is None else None
        
        script_create: str = f"CREATE TABLE IF NOT EXISTS {self.SQL_TABLE_LOAD}{column}" if self.SQL_LOAD_COLUMN is None else self.SQL_LOAD_COLUMN
        
        self.CONN.execute(script_create)
        
        columnValid: tuple = tuple(self.tableWidget.horizontalHeaderItem(i).text() for i in range(0, self.tableWidget.columnCount())) if column is None else tuple(column)
        valS: str = ", ".join(tuple(f':{num}' for num in range(0, len(columnValid))))
        script_insert: str = f"INSERT OR REPLACE INTO {self.SQL_TABLE_LOAD} VALUES ({valS})"
        
       # print(f"{script_insert=}")

        toMap: dict = lambda x: {f"{i}": v for i, v in enumerate(x)}

        for row in rows:
           # print(f"ROW > {num= }")
            self.CONN.execute(script_insert, toMap(row))
            self.CONN.commit()

    def exportSqlite(self, file_path: str) -> None:
        """
        Export Data To Sqlite DataBase to 'File_Path' Only Load Table Saved
        """
        if iPath.exists(file_path):
            if self.existsTable():
                self.updateSqliteTable()
            
            else:
                self.addSqliteTable()
        
        else:       # Create DataBase File
            if self.CONN is None:
                self.CONN = self.db_sqlite.connect(file_path)
                
                self.addSqliteTable()
            
            else:
                self.CONN.close()
                self.CONN = None
                self.CONN = self.db_sqlite.connect(file_path)
                
                self.addSqliteTable()

    def exportCsv(self, file_path: str) -> None:
        """
        Export Table To CSV File or Other File Table to 'File_Path'
        """
        get_header: list[str] = [self.tableWidget.horizontalHeaderItem(i) for i in range(0, self.tableWidget.columnCount())]
        valid: str = lambda x: x.text() if x is not None else '1'
        all_decimal: Iterable[bool] = [valid(header).isdecimal() for header in get_header]
        use_header: bool = False if False not in all_decimal else True

        del all_decimal, valid

        if use_header:
            get_header: tuple = tuple(it.text() for it in get_header)
            header_valid: str = "{}\n".format('\t'.join(get_header))

        getItem: Generator = (
            '\t'.join(row).rstrip()
            for row in self.getFromTable()
        )

        try:
            with open(file_path, 'w') as f:
                if use_header:
                    f.write(header_valid)
                f.write('\n'.join(getItem).rstrip())
        
        except (FileNotFoundError, FileExistsError, IsADirectoryError, IOError) as errfile:
            raise errfile
        
        finally:
            f.close()
            del getItem, f, get_header, header_valid, use_header

