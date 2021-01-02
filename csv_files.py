import csv

# Open the file
data = open('example.csv',encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# Refprmat it into a python object`s list of lists
data_lines = list(csv_data)

print(data_lines[1])

all_names = []

for line in data_lines[1:]:
    all_names.append(line[0])

print(all_names)

file_to_output = open('to_save_file.csv',mode='w',newline='')

csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])

csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()