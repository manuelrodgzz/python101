import csv
from os import path

def read_csv():
    file_path = path.relpath('assets/students.csv')

    with open(file_path, newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0

        columns_str = ''
        row_str = ''

        for row in csv_reader:
            if(line_count) == 0:
                for column in row:
                    columns_str += f'      {column}       | '
                line_count += 1
                print(columns_str)
            else:

                for column in row:
                    row_str += f'      {column}       '

            print(row_str)
            row_str = ''


if __name__ == '__main__':
    read_csv()