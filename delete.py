import csv

table = ['last_name', 'name', 'phone_number', 'post', 'salary']

def delete():
    request = input('Enter data to delete: \n')
    with open('data.csv', 'a') as file:
        reader = csv.reader(file, delimiter=',')
        for line in file.readlines():
            if request in line:
                writer = csv.writer(file)
                writer.writerow('')

    return request