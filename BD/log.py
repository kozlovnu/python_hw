from datetime import datetime

def write_log(data, mode):
    if mode == 'import':
        with open('log.csv','a') as file:
            file.write(f'Record data at {datetime.now()}: {data} \n')
    elif mode == 'export':
        with open('log.csv','a') as file:
            file.write(f'Read data at {datetime.now()}: {data} \n')
    elif mode == 'delete':
        with open('log.csv', 'a') as file:
            file.write(f'Deleted data at {datetime.now()}: {data} \n')
    else:
        pass