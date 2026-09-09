files_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'data.csv'
]

unique_file = []
duplicate_file = []

for i in range(len(files_list)):

    if files_list[i] not in unique_file:
        unique_file.append(files_list[i])

    else:
        if files_list[i] not in duplicate_file:
            duplicate_file.append(files_list[i])

if len(duplicate_file) > 0:
    print(duplicate_file)
else:
    print("There are No Duplicate File")