from _ast import Break

import write
import read
import log



def ask_user():
    while True:
        choise = input('What do you want - import, export or delete data?\n Enter exit to exit\n')
        if choise == 'import':
            # write.get_data()
            log.write_log(write.get_data(), 'import')
        elif choise == 'export':
            # read.request_data()
            log.write_log(read.request_data(), 'export')
        elif choise == 'exit':
            break
        else:
            print('Unknown command')