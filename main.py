import csv
import os

csv_files = os.listdir('src')
dataframes = {}
for file in csv_files:
  csv_array = csv.reader(open(f'src/{file}'))
  name = file.split('.')[0]
  dataframes[name] = list(csv_array)

print(dataframes)
