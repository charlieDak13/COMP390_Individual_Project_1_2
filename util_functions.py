import meteor_data_class
from pathlib import Path
from datetime import datetime
from xlwt import Workbook

"""
This function prints the welcome message to the program.
"""


def print_welcome_message():
    print('Welcome to the Meteorite Sorting Program!\n'
          'This program prints out user specified tables based on the categories and parameters passed into it.')
    print('Written by Charlie Dakai in December 2023\n')


"""
This function checks the user input and if it is either "<q" or "<Q" then it returns true, otherwise returns false
"""


def check_for_break(userInput):
    if userInput == "<Q" or userInput == "<q":
        print('Exiting the program. Goodbye!')
        return True
    else:
        return False


"""
This function prints the file name which is inputted in the parameter
"""


def print_file_name(fileName):
    print()
    print('Target File: ', fileName)
    print()


"""
This function prints the mode which is inputted as a parameter
"""


def print_mode(mode_input):
    print()
    print('File Mode: ', mode_input)
    print()


"""
This function is very similar to the other check for break function earlier, 
but this one checks for "Q" instead of "<q" or "<Q"
"""


def check_for_break_category(enteredCategory):
    if enteredCategory == "Q":
        print('Exiting the program. Goodbye!')
        return True
    else:
        return False


"""
This function makes sure the list has 12 values in it. If there are any blank, it replaces them with the empty string
it returns a list of length 12.
"""


def check_list_length(inputList):
    for i in range(12):
        if len(inputList) < 12:
            inputList.append('')
        else:
            pass
    return inputList


"""
This function makes a meteor object with all the attributes from the list that is passed as a parameter
"""


def make_meteor_object(attributeList):
    return meteor_data_class.MeteorDataEntry(attributeList[0], attributeList[1], attributeList[2],
                                             attributeList[3],
                                             attributeList[4], attributeList[5], attributeList[6],
                                             attributeList[7],
                                             attributeList[8], attributeList[9], attributeList[10],
                                             attributeList[11])


"""
This function prints a table to the console. It first prints the headers and then takes each element of the list that is 
passed in and prints it so it is appropriately spaced and looks good
"""


def print_table(List):
    print('=' * 200)
    print(' ' * 2, 'Name', ' ' * 20, 'ID', ' ' * 5, 'NameType', ' ' * 2, 'recClass', ' ' * 14, 'Mass(g)', ' ' * 6,
          'Fall',
          ' ' * 4, 'Year', ' ' * 4, 'recLat', ' ' * 7, 'recLong', ' ' * 7, 'GeoLocation', ' ' * 13, 'States', ' ' * 4,
          'Countries')
    print('=' * 200)
    count = 1
    for i in range(len(List)):
        splitList = List[i].split('\t')
        print(f'{count:2} {splitList[0]:25} {splitList[1]:10}{splitList[2]:10}{splitList[3]:25}{splitList[4]:15}'
              f'{splitList[5]:10}{splitList[6]:10}{splitList[7]:15}{splitList[8]:15}{splitList[9]:30}{splitList[10]:10}'
              f'{splitList[11]:10}')
        count = count + 1


"""
This function takes an user input, then checks from this input if the user wants to quit the program, then checks if 
this input is a valid fileName, and if it is, returns this value, otherwise it runs the whole process again until a 
valid file name is provided.
"""


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


"""
This function takes an user input, then checks from this input if the user wants to quit the program, then checks if 
this input is contained in a list of all the valid modes, and if it is, returns this value, otherwise it runs the whole 
process again until a valid mode name is provided.
"""


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


"""
This function takes an user input,  then checks if 
this input is in a list of all the valid categories, and if it is, returns this value, otherwise it runs the whole 
process again until a valid category name is provided.
"""


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


"""
This function takes an user input, then checks from this input if the user wants to quit the program, then checks if 
this input is a digit since we are looking for a mass value, and if it is returns this value, otherwise it runs the 
whole process again until a valid input is provided.
"""


def check_lower_limit_mass():
    while True:
        lower_limit_mass = input('Enter the LOWER limit (inclusive) for the meteors mass(g) ("Q" to quit): ')
        if check_for_break_category(lower_limit_mass):
            return "break"
        if lower_limit_mass.isdigit():
            return lower_limit_mass
        else:
            print("ERROR: " + lower_limit_mass + " is not a valid entry")


"""
This function takes an user input, then checks from this input if the user wants to quit the program, then checks if 
this input is a digit since we are looking for a mass value, and if it is then it returns this value, otherwise it runs 
the whole process again until a valid input is provided.
"""


def check_upper_limit_mass():
    while True:
        upper_limit_mass = input('Enter the UPPER limit (inclusive) for the meteors mass(g) ("Q" to quit): ')
        if check_for_break_category(upper_limit_mass):
            return "break"
        if upper_limit_mass.isdigit():
            return upper_limit_mass
        else:
            print("ERROR: " + upper_limit_mass + " is not a valid entry")


"""
This function takes an user input, then checks from this input if the user wants to quit the program, then checks if 
this input is an integer since we are looking for a year, and if it is then it returns this value, otherwise it runs the 
whole process again until a valid input is provided.
"""


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


"""
This function takes an user input, then checks from this input if the user wants to quit the program, then checks if 
this input is an integer since we are looking for a year, and if it is then it returns this value, otherwise it runs the 
whole process again until a valid input is provided.
"""


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


"""
This function takes an user input,  then checks if this input is in a list of all the valid selections, and if it is, 
returns this value, otherwise it runs the whole process again until a valid category name is provided.
"""


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


"""
this function returns the current data and time which we use later for naming excel and text files.
"""


def get_clean_datetime_string():
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str


"""
This function takes in a file path and some data, and then opens this file in write mode and writes the inputted data 
into the filepath provided. If the file is not found an error will occur.
"""


def write_to_text_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            file.write("name	id	nametype	recclass	mass (g)	fall	year	reclat	reclong	"
                       "GeoLocation	States	Counties \n")
            file.write(data)
    except FileNotFoundError as e:
        print("ERROR: File not found")


"""
This function takes in a list and then loops through the list and takes every index of the list and holds it in a big 
string. It adds a tab character everytime something new is added. It also goes onto a new line for every meteorite and
its corresponding data.
"""


def list_to_tab_sep_string(given_list):
    big_list = ""
    for _ in range(len(given_list)):
        for i in range(1):
            big_list += (given_list[_] + "\t")
        big_list += "\n"
    return big_list


"""
This function creates a workbook, opens a new sheet in the workbook, prints the headers in the sheet, and takes all the 
data from the list passed in and formats it nicely in an excel file
"""


def filtered_results_to_excel(filtered_list):
    excel_workbook = Workbook()
    filtered_data_sheet = excel_workbook.add_sheet("FilteredMeteoriteData")
    index = 0
    name_list = ["name", "id", "nametype", "recclass", "mass (g)", "fall", "year", "reclat", "reclong",
                 "GeoLocation", "States", "Counties"]
    for attributes in name_list:
        # write top row of the Excel output sheet -- __.write(row, column, value)
        filtered_data_sheet.write(0, index, attributes)
        index = index + 1
    for index in range(len(filtered_list)):
        current_meteor = filtered_list[index]
        attribute_list = current_meteor.split("\t")
        for attr_index in range(len(attribute_list)):
            # write each row of the Excel output sheet -- __.write(row, column, value)
            filtered_data_sheet.write(index + 1, attr_index, attribute_list[attr_index])
    excel_workbook.save(get_clean_datetime_string()+'.xls')



