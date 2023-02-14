import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np
from tabulate import tabulate
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('breakfast_survey')

# connect Pandas to Google Sheets
# code taken from GitHub user Asha Ponnada
data = SHEET.worksheet('bkdata').get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)
df.head()

# Colorama colours for the terminal
red = Fore.RED  # colour for error messages
yellow = Fore.YELLOW  # colour for instructions
green = Fore.GREEN  # colour for inputs
cyan = Fore.CYAN  # colour for tables
bright = Style.BRIGHT
reset = Style.RESET_ALL  # resets the colours


def clear_terminal():
    """
    This function clears the terminal
    """
    # code take from Stackoverflow user poke
    os.system('cls' if os.name == 'nt' else 'clear')


def route_selection(df_raw):
    """
    This function allows the user to select if they want
    to view results or take the survey
    """
    while True:
        print(yellow + "To view the survey results, type '1' below." + reset)
        print(yellow + "To take the survey, type '2' below.\n" + reset)

        route_choice = input(
            green + "Type your choice here then press enter:\n" + reset
        )

        # selection statement to validate user input choice
        if route_choice == '1':
            clear_terminal()
            results_selection(df_raw)
            break
        if route_choice == '2':
            clear_terminal()
            display_survey()
            break

        print(red + 'Invalid choice. Please try again' + reset)
        print(red + "You must enter a number such as '1'.\n" + reset)


# SURVEY ANALYSIS FUNCTIONS

def results_selection(df_raw):
    """
    This function allows the user to select if they would like to
    view results by gender or age group
    """
    while True:
        print(yellow + "\nPlease select from the following options:\n" + reset)
        print("1 - View results by Gender")
        print("2 - View results by Age Group\n")

        analysis_type = input(
            green + "Type your choice here then press enter:\n" + reset
        )

        # selection statement to validate user input choice
        if analysis_type == '1':
            clear_terminal()
            question_selection(df_raw, groupby_col='gender')
            break
        if analysis_type == '2':
            clear_terminal()
            question_selection(df_raw, groupby_col='age group')
            break

        print(red + 'Invalid choice. Please try again.' + reset)
        print(red + "You must enter a number such as '1'.\n" + reset)


def question_selection(df_raw, groupby_col):
    """
    This function allows the user to selected which question
    they would like to see the results for
    """
    while True:
        print(
            yellow
            + "\nSelect a question from the following options:\n"
            + reset
        )
        print("1 - Do you eat breafast?")
        print("1.1 - Why do you not eat breakfast?")
        print("2 - How many days per week do you eat breakfast?")
        print("3 - Where do you eat breakfast?")
        print("4 - At what time do you eat breakfast?")
        print("5 - What do you drink with breakfast?")
        print("6 - What do you eat for breakfast?\n")

        print("To retart the program, type 'exit'\n")

        choice = input(
            green + "Type your choice here then press enter:\n" + reset
        )

        # selection statement to validate user input choice
        if choice == '1':
            clear_terminal()
            print(cyan + bright + "Do you eat breafast?" + reset)
            display_percentages(df_raw, groupby_col, '1')

        elif choice == '1.1':
            clear_terminal()
            print(cyan + bright + "Why do you not eat breakfast?" + reset)
            display_percentages(df_raw, groupby_col, '1.1')

        elif choice == '2':
            clear_terminal()
            print(
                cyan + bright + "How many days per week do you eat breakfast?"
                + reset
            )
            display_percentages(df_raw, groupby_col, '2')

        elif choice == '3':
            clear_terminal()
            print(cyan + bright + "Where do you eat breakfast?" + reset)
            display_percentages(df_raw, groupby_col, '3')

        elif choice == '4':
            clear_terminal()
            print(cyan + bright + "At what time do you eat breakfast?" + reset)
            display_percentages(df_raw, groupby_col, '4')

        elif choice == '5':
            clear_terminal()
            print(cyan + bright + "What do you drink with breakfast?" + reset)
            display_percentages(df_raw, groupby_col, '5')

        elif choice == '6':
            clear_terminal()
            print(cyan + bright + "What do you eat for breakfast?" + reset)
            display_percentages(df_raw, groupby_col, '6')

        elif choice in ('exit', 'EXIT'):
            clear_terminal()
            route_selection(df)

        else:
            print(red + "Invalid choice. Please try again." + reset)
            print(
                red + "Enter the question number such as '1' or '1.1'."
                + reset
            )
            print(red + "To restart the program, type 'exit' .\n" + reset)

    return choice


def display_percentages(df_raw, groupby_col, question_num):
    """
    This function calculates percentages of each possible answer
    based on groupby_col i.e. if the users chooses to view results
    by gender or age group.
    """
    # Pandas and Numpy are used in this function
    # after question 1.1 show results only for people who eat breakfast
    if question_num not in ['1', '1.1']:
        df_raw = df_raw[df_raw['question 1'] == 'Yes']
    elif question_num == '1.1':
        df_raw = df_raw[df_raw['question 1'] == 'No']

    # calculate percentage based on groupby_col and qustion_num
    question_col = f"question {question_num}"
    df_group = df_raw.groupby([groupby_col, question_col]).size().reset_index()
    df_group.rename(columns={0: 'counts'}, inplace=True)
    label_total_by_group = f'total_by_{groupby_col}'
    df_group[label_total_by_group] = \
        df_group.groupby(groupby_col)['counts'].transform(sum)
    df_group['percentage'] = np.round(
        df_group['counts'] / df_group[label_total_by_group] * 100
        )
    df_group['percentage'] = df_group['percentage'].apply(
        lambda x: f'{int(x)}%'
    )

    # convert table to wide format
    wide_table = pd.pivot(
        df_group,
        index=groupby_col,
        columns=question_col,
        values='percentage'
    )

    # removes empty columns and replaces null values with 0%
    if "" in wide_table.columns:
        wide_table.drop(columns="", inplace=True)
    wide_table.fillna('0%', inplace=True)

    # code from Stackoverflow user Romain
    print(
        cyan + bright + tabulate(wide_table, headers='keys', tablefmt='psql')
        + reset
    )


# SURVEY FUNCTIONS

def update_worksheet(user_answers):
    """
    Add user ID to the start of the user answers list
    by getting the index and adding 2
    Update Google Sheets with user answers by
    adding a new row the end of the sheet.
    """
    # Pandas is used here
    # add new user ID to user_answers before pushing to Google Sheets
    index = df.index.tolist().pop()
    user_id = index + 2
    user_answers.insert(0, user_id)

    # push data to Google Sheets
    worksheet = SHEET.worksheet("bkdata")
    worksheet.append_row(user_answers)


def end_program():
    """
    This displays a goodbye message and the
    option to restart the program
    """
    print(yellow + """\
 ## ##    ## ##    ## ##   ### ##   ### ##   ##  ##   ### ###
##   ##  ##   ##  ##   ##   ##  ##   ##  ##  ##  ##    ##  ##
##       ##   ##  ##   ##   ##  ##   ##  ##  ##  ##    ##
##  ###  ##   ##  ##   ##   ##  ##   ## ##    ## ##    ## ##
##   ##  ##   ##  ##   ##   ##  ##   ##  ##    ##      ##
##   ##  ##   ##  ##   ##   ##  ##   ##  ##    ##      ##  ##
 ## ##    ## ##    ## ##   ### ##   ### ##     ##     ### ###
    """ + reset)

    while True:
        print('Not ready to leave yet?')
        print("Type '1' below restart the program.\n")

        choice = input(
            green + "Type your choice here then press enter:\n" + reset
        )

        # selection statement to validate user input choice
        if choice == '1':
            clear_terminal()
            main(df)

        print(red + "Invalid choice. Please try again." + reset)
        print(red + "You must enter a number such as '1'.\n" + reset)

    return choice


def end_survey():
    """
    This displays a thank you message to the user and
    an option to view the survey results
    """
    while True:
        print('Your answers have been successfully submitted.')
        print('Thank you for taking the time to complete the survey.\n')
        print('Would you like to view the survey results?')
        print(yellow + 'To view the survey results, type 1.')
        print('To end the program, type 2.\n' + reset)

        choice = input(
            green + "Type your choice here then press enter:\n" + reset
        )

        # selection statement to validate user input choice
        if choice == '1':
            clear_terminal()
            results_selection(df)

        elif choice == '2':
            clear_terminal()
            end_program()
            break

        print(red + "Invalid choice. Please try again." + reset)
        print(red + "You must enter a number such as '1'.\n" + reset)

    return choice


def submit_survey(questions_answered, user_answers):
    """
    Displays the users answers and allows the user to submit
    their results or take the survey again
    """
    print('Thank you taking this survey.\n')
    print('Please review your answers then submit or retake the survey:\n')

    # displays questions answered by the user with the answer they gave
    iterator = zip(questions_answered, user_answers)

    for question_answered, user_answer in iterator:
        # if the answer is '' do not display the question
        if (user_answer == '') and (question_answered == ''):
            continue
        print(f"{question_answered}: {yellow}{user_answer}{reset}")

    while True:
        print(yellow + '\nTo submit your answers, type 1 below.')
        print('To re-take the survey, type 2 below.\n' + reset)
        choice = input(
            green + "Type your choice here then press enter:\n" + reset
        )

        # selection statement to validate user input choice
        if choice == '1':
            clear_terminal()
            update_worksheet(user_answers)
            end_survey()

        elif choice == '2':
            clear_terminal()
            display_survey()

        print(red + "Invalid choice. Please try again." + reset)
        print(red + "You must enter a number such as '1'.\n" + reset)

    return choice


def display_survey():
    """
    This function iterates through a dictionary and pushes questions
    and answer options to the user based on their previous answers.
    If the user answers 'Yes' to question 3, question 4 is skipped
    If the user answers 'No' to question 3, they answer question 5
    then the survey ends.
    """
    q_and_o = {
        1: {
            'question': 'Select your age aroup',
            'options': ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
        },
        2: {
            'question': 'Select your gender',
            'options': ['Male', 'Female']
        },
        3: {
            'question': 'Do you eat breakfast',
            'options': ['Yes', 'No']
        },
        4: {
            'question': 'If not, why do you not eat breakfast?',
            'options': ['Not hungry', 'No time', 'Other']
        },
        5: {
            'question': 'How many days per week do you eat breakfast?',
            'options': ['1', '2', '3', '4', '5', '6', '7']
        },
        6: {
            'question': 'Where do you eat breakfast?',
            'options': ['Home', 'Work', 'On the way to work']
        },
        7: {
            'question': 'At what time do you eat breakfast?',
            'options': ['6am-7am', '7am-8am', '8am-9am', '9am-10am',
                        '10am-11am']
        },
        8: {
            'question': 'What do you drink with breakfast?',
            'options': ['Coffee', 'Tea', 'Juice']
        },
        9: {
            'question': 'What do you eat for breakfast?',
            'options': ['Cereal', 'Yoghurt',
                        'Toast', 'Eggs', 'Protein shake']
        },
    }

    user_answers = []
    questions_answered = []

    for question_num, question_dict in q_and_o.items():
        question = question_dict['question']
        options = question_dict['options']

        if question_num <= 3:
            user_answers = question_and_log_results(
                question, options, user_answers, questions_answered
                )

        if question_num == 4:
            # adds an empty string to user_answers to avoid an error
            # when pushing the data to google sheets later
            if user_answers[-1] == 'Yes':
                user_answers.append('')
                questions_answered.append('')
                continue
            # ends the survey if question 4 was answered
            else:
                user_answers = question_and_log_results(
                    question, options, user_answers, questions_answered
                    )
                break

        if question_num >= 5:
            user_answers = question_and_log_results(
                question, options, user_answers, questions_answered
                )

    clear_terminal()
    submit_survey(questions_answered, user_answers)


def question_and_log_results(
    question,
    options,
    user_answers,
    questions_answered
):
    """
    This function displays the questions and answer options to the user
    It validates users input and stores answers from the user
    """
    # stores valid input options using the enumerate values
    valid = []
    print(yellow + f'\n{question}\n' + reset)
    # allocates a number to the answer options for the user to choose from
    # enumerate code from Stackoverflow user Leejay Schmidt
    for (i, option) in enumerate(options, start=1):
        i = str(i)
        valid.append(i)
        print(f"{i}: {option}")
    answer = input(green + '\nType your answer choice here:\n' + reset)
    # validates user input against the enumerate values
    # code uses solution from Tutorial Eyehunt by Rohit.
    while answer not in valid:
        print(
            red + f'Invalid choice, you must enter a number from: {valid}'
            + reset
        )
        answer = input(green + 'Type your answer choice here:\n' + reset)
    # uses the index of the answer option in the q_and_o dictionary to
    # get the string value and append it to users_answers
    index = int(answer)
    logged_answer = options[index-1]
    print(logged_answer)
    user_answers.append(logged_answer)
    print(user_answers)
    questions_answered.append(question)

    return user_answers


def welcome():
    """
    Displays a welcome message and introduction to the survey
    """
    print(yellow + """\
                             #        #                   #
 ####                        #       ###                  #
 #   #                       #  #    #                   ###
 ####   # #     ##     ###   # #    ###     ###   ####    #
 #   #  ## #   # ##   #  #   ###     #     #  #   ##      # #
 #   #  #      ##     #  #   #  #    #     #  #     ##    # #
 ####   #       ###    ####  #  #    #      ####  ####     #

         ##
        #  #
         #     #  #   # #    #  #    ##    #  #
          #    #  #   ## #   #  #   # ##   #  #
        #  #   #  #   #       ##    ##     ## #
         ##     ###   #       ##     ###     ##
                                           #  #
                                            ##
    """ + reset)
    print(
        """
Welcome to the Breakfast Survey! \n
This survey analyses breakfast eating habits based on gender and age. The
program allows you to view the survey results or add to the data by completing
the survey. \n
To submit an answer to a survey question, or to complete an action such as the
ones highlighted in yellow below, you must type the number or word that has
been assigned to the action or question answer. Then press enter to submit.
        """
    )


# MAIN FUNCTION

def main(df_raw):
    """
    Run all program functions
    """
    welcome()
    route_selection(df_raw)


main(df_raw=df)
