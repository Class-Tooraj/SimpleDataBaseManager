__author__ = "Tooraj_Jahangiri"
__email__ = "toorajjahangiri@gmail.com"

# IMPORT
from typing import Iterable, Generator
from itertools import product

maker: Iterable = product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=3)
value_column: Iterable = (''.join(i) for i in maker)

def row() -> Generator:
    line: list[str] = []
    limit: len = 75
    for it in value_column:
        if len(line) < limit:
            line.append(it)
            line.append('\t')
        else:
            line.append('\n')
            yield line
            line.clear()

rows: Iterable = (''.join(i) for i in row())

with open("big_csv.csv", 'w') as f:
    for line in rows:
        f.write(line)
        