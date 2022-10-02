import csv

table = ['last_name', 'name', 'phone_number', 'post', 'salary']


def request_data():
    request = input('Enter the value of search: ')
    with open('data.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for line in file.readlines():
            if request in line:
                dict_result = dict(zip(table, line.split(',')))
                for key , value in dict_result.items():
                    print(f'{key}: {value}')
    return request