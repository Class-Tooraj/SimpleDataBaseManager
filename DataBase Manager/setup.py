__author__ = "Tooraj_Jahangiri"
__email__ = "toorajjahangiri@gmail.com"

# IMPORT
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon_db_manager.ico']
package = ['gui']

# TARGET
_TARGET = Executable(
    script = "main.py",
    target_name= "DataBaseManager.exe" ,
    base = "Win32GUI",
    icon = "icon_db_manager.ico",
)

_OPTIONS: dict = {
    'build_exe': {'include_files': files, 'packages': package}
}

# SETUP CX FREEZE
setup(
    name = "DataBaseManager",
    version = "1.00-R",
    description = "Tools > Simple Tools Manager 'Sqlite3' and 'Csv' Converting 'Sqlite3' Table To 'Csv' Table.",
    author = "Tooraj Jahangiri",
    options = _OPTIONS,
    executables = [_TARGET],
)

"""
use terminal(cmd) and type : 'python setup.py build'
output main.exe
"""