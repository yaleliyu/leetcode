

file_path = 'D:\\tmp\\unreceived_signed_pkg.dat'
data = ''
import csv
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    prev = ''
    cur = ''
    for row in reader:
        if prev == '':
            prev = row
            continue

        if row[:2] == '20' or row[:2]  == '19':
      #      data += prev + '\n'
            prev = row
        else:
       #     data += prev + row + '\n'
            prev = ''



print('over')
