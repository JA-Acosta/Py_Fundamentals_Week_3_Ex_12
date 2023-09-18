'''
>>> JAAR
>>> 09/18/2023
>>> Practicing Fundamentals Program 24
>>> Version 1
'''

'''
>>> Generates a program that opens a file, otherwise, it asks the user to enter a new file if that file doesn't exist. If the file does exist, the user is allowed to write to the file. Finally, the user is given the opportunity to enter a new file name.
'''

def user_response(question)->str :
    '''
    >>> Prints a question to console then asks the user to either enter yes or no. Otherwise, prompts the user to enter a new response to the question.

    >>> Param: (str) question
    >>> Return: (str) response
    '''
    while True :
        response = input(question).lower()
        if response == 'yes' or response == 'no' :
            return response
        else :
            print('Your input was invalid! Enter a new response.', end = '\n\t')

def file_handling(file_path) :
    '''
    >>> Prompts the user to enter a file name then attempts to open the fie=le. If the file exists, will open the file and print the file contents to the console. Otherwise, prints an error message. Also, if the file exists will ask the user if they want to append text to the end of the file.

    >>> Param: (str) file_path
    '''
    try :
        with open(file_path, 'r', newline = '') as fr :
            reader = fr.readlines()
            for line in reader :
                print(line)
    except FileNotFoundError :
        print('No file was found.')
    else :
        if user_response('Do you want to add to this file?: ') == 'yes' :
            with open(file_path, 'a', newline = '') as af:
                input_response = 'no'
                update = ''
                while input_response == 'no' :
                    update = input('Enter your update: ')
                    input_response = user_response(f'''
Your input was:
    \t{update}
Is your input correct?: ''')
                af.write(' ' + update)
    finally :
        print('\nDone!')

def main() :
    response = 'yes'
    while response == 'yes' :
        file_handling(input('To open a file, enter a file path: '))
        response = user_response('Do you want to work with another file?: ')

if __name__ == '__main__' :
    main()