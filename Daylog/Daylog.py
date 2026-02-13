import os
import datetime

import pytz
while True:
    print('This is a daylog generator.')

    print('1. Create a new daylog')
    print('2. View an existing daylog')
    print('3. Delete an existing daylog')  
    print('4. Exit')
    choice = input('Choose something you want: ')
    if choice == '1':

        print('Creating a new one')
        title = input('Title: ')

        info = input('Info: ')
####IMPORTANT: This part of the code leads to the correct path of the logs directory(very important)
        base_path = os.path.dirname(os.path.abspath(__file__)) # gets the current directory of the file

        logs_path = os.path.join(base_path, 'logs') # creates the path to the logs directory
        if not os.path.exists(logs_path):# checks if the logs directory exists or
            os.makedirs(logs_path) # create the daylogs directory if it does not exist
####IMPORTANT ENDS####
        if os.path.exists(f'{logs_path}/{title}.txt'):


            print('The daylog already exists. Please choose a different title.')

        else:
            with open(f'{logs_path}/{title}.txt', 'w') as f:
                current_time = datetime.datetime.now().replace(tzinfo = pytz.UTC)
                print(current_time)
                f.write(f'Title: {title}')
                f.write(f'\nDate and Time: {current_time}')

                f.write('\n')

                f.write(f'Information: {info}')
            print('Daylog created successfully.')
        print(' ')
    elif choice == '2':
        base_path = os.path.dirname(os.path.abspath(__file__)) # gets the current directory of the file
        logs_path = os.path.join(base_path, 'logs') # creates the path to the logs directory
        question = input('Which daylog do you want to view? ')

        if os.path.exists(f'{logs_path}/{question}.txt'):

            with open(f'{logs_path}/{question}.txt', 'r') as f:   
                print('  ')           
                print(f.read())                
                print('  ')
                f.close()
        else:
            print('That daylog does not exist.')

            print('  ')
    elif choice == '3':
        base_path = os.path.dirname(os.path.abspath(__file__)) # gets the current directory of the file
        logs_path = os.path.join(base_path, 'logs') # creates the path to the logs directory
        question = input('which daylog do you want to delete?')
        if os.path.exists(f'{logs_path}/{question}.txt'):
            os.remove(f'{logs_path}/{question}.txt')
            print('Daylog deleted successfully.')
            print('  ')
        else:
            print('That daylog does not exist.')
            print('  ')











    elif choice == '4':    
        print('Exiting the program.')       
        print('  ')
        break
    else:
        print('Invalid choice. Please try again.')
        
        print('  ')