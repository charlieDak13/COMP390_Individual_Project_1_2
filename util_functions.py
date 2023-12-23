import meteor_data_class
from pathlib import Path
from datetime import datetime


def print_welcome_message():
    print('Welcome to the Meteorite Sorting Program!\n'
          'This program prints out user specified tables based on the categories and parameters passed into it.')
    print('Written by Charlie Dakai in December 2023\n')


def check_for_break(userInput):
    if userInput == "<Q" or userInput == "<q":
        print('Exiting the program. Goodbye!')
        return True
    else:
        return False


def print_file_name(fileName):
    print()
    print('Target File: ', fileName)
    print()


def print_mode(mode_input):
    print()
    print('File Mode: ', mode_input)
    print()


def check_for_break_category(enteredCategory):
    if enteredCategory == "Q":
        print('Exiting the program. Goodbye!')
        return True
    else:
        return False


def check_list_length(inputList):
    for i in range(12):
        if len(inputList) < 12:
            inputList.append('')
        else:
            pass
    return inputList


def make_meteor_object(attributeList):
    return meteor_data_class.MeteorDataEntry(attributeList[0], attributeList[1], attributeList[2],
                                             attributeList[3],
                                             attributeList[4], attributeList[5], attributeList[6],
                                             attributeList[7],
                                             attributeList[8], attributeList[9], attributeList[10],
                                             attributeList[11])


# def filter_mass(mass, name, holdingList):
#     if float(get_lower_limit()) < float(mass) < float(get_upper_limit()):
#         list.append(meteor_object.name + ', ' + meteor_object.mass)


def print_mass_table(massList):
    print('=' * 40)
    print(' ' * 2, 'Name', ' ' * 21, 'Mass (g)', ' ' * 16)
    print('=' * 40)
    count = 1
    for i in range(len(massList)):
        splitMass = massList[i].split(',')
        print(f'{count:2} {splitMass[0]:25} {splitMass[1]:10}')
        count = count + 1


def print_year_table(yearList):
    year_count = 1
    print('=' * 40)
    print(' ' * 2, 'Name', ' ' * 20, 'Year', ' ' * 16)
    print('=' * 40)
    for i in range(len(yearList)):
        splitYear = yearList[i].split(',')
        print(f'{year_count:2} {splitYear[0]:25} {splitYear[1]:5}')
        year_count = year_count + 1


def check_file_name():
    while True:
        file = input('Enter a valid file name (ex. "file_name.txt") with its file extension if applicable |or| \n'
                     'Enter "<q" or "<Q" to quit the program: ')
        if check_for_break(file):
            return "break"
        path = Path(file)
        if path.is_file():
            print_file_name(file)
            return file
        else:
            print("ERROR: TARGET FILE " + "\"" + file + "\"" " IS NOT VALID")
            # break out not wokring until valid file provided


def check_mode_type():
    while True:
        mode = input('Please enter a mode to open the file in.\n'
                     "'r':" ' open for reading (default)\n'
                     "'w':" ' open for writing, truncating the file first. (WARNING: this mode will '
                     'delete the contents of an existing file\n'
                     "'x':" ' open for exclusive creation, failing if the file already exists\n'
                     "'a':" ' open for writing, appending to the end of file if it exists\n'
                     "'b':" ' binary mode\n'
                     "'t':" ' text mode (default)\n'
                     "'+':" ' open for updating (reading and writing)\n'
                     'Enter <q or <Q to quit the program: ')
        if check_for_break(mode):
            return "break"
        mode_types_list = ['r', 'w', 'x', 'a', 'b', 't', '+']
        if mode_types_list.__contains__(mode):
            print_mode(mode)
            return mode
        else:
            print("ERROR: " + mode + " is not a valid mode")


def check_category():
    while True:
        category = input('What attribute would u like to filter the data on?\n'
                         '1. meteor MASS (g)\n'
                         '2. The YEAR the meteor fell\n'
                         '3. QUIT\n'
                         '>>')
        category_list = ['1', '2', '3']
        if category_list.__contains__(category):
            return category
        else:
            print("ERROR: " + category + " is not a valid category")


def check_lower_limit_mass():
    while True:
        lower_limit_mass = input('Enter the LOWER limit (inclusive) for the meteors mass(g) ("Q" to quit): ')
        if check_for_break_category(lower_limit_mass):
            return "break"
        if lower_limit_mass.isdigit():
            return lower_limit_mass
        else:
            print("ERROR: " + lower_limit_mass + " is not a valid entry")


def check_upper_limit_mass():
    while True:
        upper_limit_mass = input('Enter the UPPER limit (inclusive) for the meteors mass(g) ("Q" to quit): ')
        if check_for_break_category(upper_limit_mass):
            return "break"
        if upper_limit_mass.isdigit():
            return upper_limit_mass
        else:
            print("ERROR: " + upper_limit_mass + " is not a valid entry")


def check_lower_year():
    while True:
        lower_year = input('Enter the LOWER limit for the meteors YEAR (inclusive) (Q to quit): ')
        if check_for_break_category(lower_year):
            return "break"
        try:
            int_value = int(lower_year)
            return lower_year
        except ValueError:
            print("ERROR: " + lower_year + " is not a valid year")


def check_upper_year():
    while True:
        upper_year = input('Enter the UPPER limit for the meteors YEAR (inclusive) (Q to quit): ')
        if check_for_break_category(upper_year):
            return "break"
        try:
            int_value = int(upper_year)
            return upper_year
        except ValueError:
            print("ERROR: " + upper_year + " is not a valid year")


def check_data_selection():
    while True:
        data_selection = input("How would you like to output the filtered results?\n"
                               "1. On Screen (In Terminal)\n"
                               "2. To a TEXT file\n"
                               "3. To an EXCEL file\n"
                               "4. QUIT\n"
                               ">>")
        data_option_list = ["1", "2", "3", "4"]
        if data_option_list.__contains__(data_selection):
            return data_selection
        else:
            print("ERROR: " + data_selection + " is not a valid option")


def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str


def write_to_text_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            file.write("name	id	nametype	recclass	mass (g)	fall	year	reclat	reclong	"
                       "GeoLocation	States	Counties \n")
            file.write(data)
    except FileNotFoundError as e:
        print("ERROR: File not found")


def list_to_tab_sep_string(given_list):
    big_list = ""
    for _ in range(len(given_list)):
        for i in range(2):
            big_list += (given_list[_] + "   ")
        big_list += "\n"
    return big_list


