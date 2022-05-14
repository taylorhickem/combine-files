'''
combine csv files in the folder into a single file.
1) add the files into the folder
2) open a new cmd window
3) cd into the directory C:\...
4) run combine.py and add an optional filename, otherwise leave blank for all.csv
    \combine>python combine.py "nowthen_then_month_yyyy-mm month"
'''
import os
import sys
import pandas
import shutil
import utilities.fso as fso


CUR_DIR = os.path.dirname(os.path.abspath(__file__))
FILETYPE = 'csv'


def combine(filename='all'):
    files = fso.getFilesInFolder(CUR_DIR)
    if len(files) > 0:
        csv_files = [f for f in files if '.' + FILETYPE in f]
        if len(csv_files) > 0:
            header, lines = get_lines(
                CUR_DIR + '\\' + csv_files[0])
            for f in csv_files[1:]:
                h, file_lines = get_lines(
                    CUR_DIR + '\\' + f)
                lines = lines + file_lines
        if len(lines) > 0:
            f = open(CUR_DIR + '\\' + filename + '.csv', 'w')
            f.write(header + lines)
            f.close()
        flush(csv_files)


def get_lines(file_path):
    f = open(file_path, 'r')
    header = f.readline()
    lines = f.readlines()
    line_str = ''.join(lines)
    return header, line_str


def flush(files):
    for f in files:
        os.remove(CUR_DIR + '\\' + f)


def autorun():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        combine(filename)
    else:
        combine()


if __name__ == "__main__":
    autorun()