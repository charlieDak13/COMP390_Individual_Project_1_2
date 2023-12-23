import meteor_data_class
import util_functions
from pathlib import Path

#   meteorite_landing_data.txt

# makes empty lists to hold filtered values
mass_list = []
year_list = []
# prints welcome message
util_functions.print_welcome_message()
# makes infinite loop so program always runs and continues until broken
while True:
    # lets user enter a file name or quit the program if desired
    file = util_functions.check_file_name()
    if file == "break":
        break
    # gives user mode options to enter or quit the program
    mode = util_functions.check_mode_type()
    # checks if user wants to break, otherwise continues
    if mode == "break":
        break
        # mode_input = util_functions.final_mode
    # gives user the option of categories to filter by and the option to quit
    category_input = util_functions.check_category()

    if category_input == "1":
        # sets lower limit and checks if user wants to quit
        lower_limit_input = util_functions.check_lower_limit_mass()
        if lower_limit_input == "break":
            break
        # sets upper limit and checks if user wants to quit
        upper_limit_input = util_functions.check_upper_limit_mass()
        if upper_limit_input == "break":
            break
        # runs program line for line with the upper and lower limits
        file = open(file, mode)
        with file as text_file:
            file.readline()
            for line in file:
                split_list = line.strip('\n').split('\t')
                util_functions.check_list_length(split_list)
                meteor_object = util_functions.make_meteor_object(split_list)
                
    # mass filter
                if meteor_object.mass == '':
                    continue
                elif float(lower_limit_input) < float(meteor_object.mass) < float(upper_limit_input):
                    mass_list.append(meteor_object.name + ', ' + meteor_object.mass)
        # prints tables and ends program after
        data_selection = util_functions.check_data_selection()
        if data_selection == "1":
            util_functions.print_mass_table(mass_list)
            break
        elif data_selection == "2":
            util_functions.write_to_text_file(util_functions.get_clean_datetime_string(),
                                              util_functions.list_to_tab_sep_string(mass_list))
            break
        elif data_selection == "3":
            continue
        elif data_selection == "4":
            break
    elif category_input == '2':
        # sets lower limit and checks if user wants to quit
        low_year_input = util_functions.check_lower_year()
        if util_functions.check_lower_year() == "break":
            break
        # sets upper limit and checks if user wants to quit
        high_year_input = util_functions.check_upper_year()
        if util_functions.check_upper_year() == "break":
            break
        # runs program line for line with the upper and lower limits
        file = open(file, mode)
        with file as text_file:
            file.readline()
            for line in file:
                split_list = line.strip('\n').split('\t')
                util_functions.check_list_length(split_list)
                meteor_object = util_functions.make_meteor_object(split_list)
        # year filter
                if meteor_object.year == '':
                    continue
                elif int(high_year_input) > int(meteor_object.year) >= int(low_year_input):
                    year_list.append(meteor_object.name + ',' + meteor_object.year)
        # prints year table and breaks after
        util_functions.print_year_table(year_list)
        break
    elif category_input == '3':
        # ends the program
        print('Exiting the program. Goodbye!')
        break









