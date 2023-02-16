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
RED = Fore.RED  # colour for error messages
YELLOW = Fore.YELLOW  # colour for instructions
GREEN = Fore.GREEN  # colour for inputs
CYAN = Fore.CYAN  # colour for tables
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL  # resets the colours


def clear_terminal():
    """
    This function clears the terminal
    """
    # code take from Stackoverflow user poke
    os.system('cls' if os.name == 'nt' else 'clear')


def route_selection(df_raw):
    """
    This function requests input from the user to indicate
    if they want to view survey results or take the survey.
    The loop runs repeatedly until input is valid.
    """
    while True:
        print(YELLOW + "To view the survey results, type '1' below." + RESET)
        print(YELLOW + "To take the survey, type '2' below.\n" + RESET)

        route_choice = input(
            GREEN + "Type your choice here then press enter:\n" + RESET
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

        print(RED + 'Invalid choice. Please try again' + RESET)
        print(RED + "You must enter a number such as '1'.\n" + RESET)


# SURVEY ANALYSIS FUNCTIONS

def results_selection(df_raw):
    """
    This function requests input from the user to indicate
    if they would like to view results by gender or age group.
    The loop runs repeatedly until input is valid.
    """
    while True:
        print(YELLOW + "\nPlease select from the following options:\n" + RESET)
        print("1 - View results by Gender")
        print("2 - View results by Age Group\n")

        analysis_type = input(
            GREEN + "Type your choice here then press enter:\n" + RESET
        )

        # selection statement to validate user input choice
        # passes user choice to question_selection
        if analysis_type == '1':
            clear_terminal()
            question_selection(df_raw, groupby_col='gender')
            break
        if analysis_type == '2':
            clear_terminal()
            question_selection(df_raw, groupby_col='age group')
            break

        print(RED + 'Invalid choice. Please try again.' + RESET)
        print(RED + "You must enter a number such as '1'.\n" + RESET)


def question_selection(df_raw, groupby_col):
    """
    This function requests input from the user to indicate which
    question they would like to see the results for.
    The loop runs repeatedly while displaying the results until
    the user chooses to exit.
    """
    while True:
        print(
            YELLOW
            + "\nSelect a question from the following options:\n"
            + RESET
        )
        print("1 - Do you eat breafast?")
        print("1.1 - Why do you not eat breakfast?")
        print("2 - How many days per week do you eat breakfast?")
        print("3 - Where do you eat breakfast?")
        print("4 - At what time do you eat breakfast?")
        print("5 - What do you drink with breakfast?")
        print("6 - What do you eat for breakfast?\n")

        print("To restart the program, type 'exit'\n")

        choice = input(
            GREEN + "Type your choice here then press enter:\n" + RESET
        )

        # selection statement to validate user input choice
        # passes question number choice to display_percentages
        if choice == '1':
            clear_terminal()
            print(CYAN + BRIGHT + "Do you eat breafast?" + RESET)
            display_percentages(df_raw, groupby_col, '1')

        elif choice == '1.1':
            clear_terminal()
            print(CYAN + BRIGHT + "Why do you not eat breakfast?" + RESET)
            display_percentages(df_raw, groupby_col, '1.1')

        elif choice == '2':
            clear_terminal()
            print(
                CYAN + BRIGHT + "How many days per week do you eat breakfast?"
                + RESET
            )
            display_percentages(df_raw, groupby_col, '2')

        elif choice == '3':
            clear_terminal()
            print(CYAN + BRIGHT + "Where do you eat breakfast?" + RESET)
            display_percentages(df_raw, groupby_col, '3')

        elif choice == '4':
            clear_terminal()
            print(CYAN + BRIGHT + "At what time do you eat breakfast?" + RESET)
            display_percentages(df_raw, groupby_col, '4')

        elif choice == '5':
            clear_terminal()
            print(CYAN + BRIGHT + "What do you drink with breakfast?" + RESET)
            display_percentages(df_raw, groupby_col, '5')

        elif choice == '6':
            clear_terminal()
            print(CYAN + BRIGHT + "What do you eat for breakfast?" + RESET)
            display_percentages(df_raw, groupby_col, '6')

        elif choice in ('exit', 'EXIT'):
            clear_terminal()
            route_selection(df)

        else:
            print(RED + "Invalid choice. Please try again." + RESET)
            print(
                RED + "Enter the question number such as '1' or '1.1'."
                + RESET
            )
            print(RED + "To restart the program, type 'exit' .\n" + RESET)


def display_percentages(df_raw, groupby_col, question_num):
    """
    Receives groupby_col and question_num data based on the users
    selection.
    Calculates percentages of each possible answer to a question.
    Prints a table with the results.
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

    # prints table with results
    # code from Stackoverflow user Romain
    print(
        CYAN + BRIGHT + tabulate(wide_table, headers='keys', tablefmt='psql')
        + RESET
    )


# SURVEY FUNCTIONS

def update_worksheet(user_answers):
    """
    Adds a user ID to the start of the user_answers list
    by getting the index and adding 2.
    Updates Google Sheets with user answers by
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
    Displays a goodbye message.
    Requests input from the user to restart the program.
    The loop runs repeatedly until input is valid.
    """
    print(YELLOW + """\
 ## ##    ## ##    ## ##   ### ##   ### ##   ##  ##   ### ###
##   ##  ##   ##  ##   ##   ##  ##   ##  ##  ##  ##    ##  ##
##       ##   ##  ##   ##   ##  ##   ##  ##  ##  ##    ##
##  ###  ##   ##  ##   ##   ##  ##   ## ##    ## ##    ## ##
##   ##  ##   ##  ##   ##   ##  ##   ##  ##    ##      ##
##   ##  ##   ##  ##   ##   ##  ##   ##  ##    ##      ##  ##
 ## ##    ## ##    ## ##   ### ##   ### ##     ##     ### ###
    """ + RESET)

    while True:
        print('Not ready to leave yet?')
        print(YELLOW + "Type '1' below restart the program.\n" + RESET)

        choice = input(
            GREEN + "Type your choice here then press enter:\n" + RESET
        )

        # selection statement to validate user input choice
        if choice == '1':
            clear_terminal()
            main(df)

        print(RED + "Invalid choice. Please try again." + RESET)
        print(RED + "You must enter a number such as '1'.\n" + RESET)


def end_survey():
    """
    This displays a thank you message to the user.
    Requests input from the user to either view the survey results
    or end the program.
    The loop runs repeatedly until input is valid.
    """
    while True:
        print('Your answers have been successfully submitted.')
        print('Thank you for taking the time to complete the survey.\n')
        print('Would you like to view the survey results?')
        print(YELLOW + 'To view the survey results, type 1.')
        print('To end the program, type 2.\n' + RESET)

        choice = input(
            GREEN + "Type your choice here then press enter:\n" + RESET
        )

        # selection statement to validate user input choice
        if choice == '1':
            clear_terminal()
            results_selection(df)

        elif choice == '2':
            clear_terminal()
            end_program()
            break

        print(RED + "Invalid choice. Please try again." + RESET)
        print(RED + "You must enter a number such as '1'.\n" + RESET)


def submit_survey(questions_answered, user_answers):
    """
    Receives and displays the users survey answers.
    Requests input from the user to submit their answers or
    to take the survey again.
    The loop runs repeatedly until input is valid.
    """
    print('Thank you taking this survey.\n')
    print('Please review your answers then submit or retake the survey:\n')

    # displays questions answered by the user with the answer they gave
    iterator = zip(questions_answered, user_answers)

    for question_answered, user_answer in iterator:
        # if the answer is '' do not display the question
        if (user_answer == '') and (question_answered == ''):
            continue
        print(f"{question_answered}: {YELLOW}{user_answer}{RESET}")

    while True:
        print(YELLOW + '\nTo submit your answers, type 1 below.')
        print('To re-take the survey, type 2 below.\n' + RESET)
        choice = input(
            GREEN + "Type your choice here then press enter:\n" + RESET
        )

        # selection statement to validate user input choice
        if choice == '1':
            clear_terminal()
            update_worksheet(user_answers)
            end_survey()

        elif choice == '2':
            clear_terminal()
            display_survey()

        print(RED + "Invalid choice. Please try again." + RESET)
        print(RED + "You must enter a number such as '1'.\n" + RESET)


def display_survey():
    """
    This function iterates through a dictionary and pushes questions
    and answer options to the user based on their previous answers:
    If the user answers 'Yes' to question 3, question 4 is skipped.
    If the user answers 'No' to question 3, they answer question 4
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
            'question': 'Do you eat breakfast?',
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

    # stores user answers and questions answered
    user_answers = []
    questions_answered = []

    for question_num, question_dict in q_and_o.items():
        question = question_dict['question']
        options = question_dict['options']

        if question_num <= 3:
            user_answers, questions_answered = question_and_log_results(
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
                user_answers, questions_answered = question_and_log_results(
                    question, options, user_answers, questions_answered
                    )
                break

        if question_num >= 5:
            user_answers, questions_answered = question_and_log_results(
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
    Receives questions and answers to be displayed to the user.
    Requests and validates input from the user.
    Stores answers from the user.
    """
    # stores valid input options using the enumerate values
    valid = []
    print(YELLOW + f'\n{question}\n' + RESET)
    # allocates a number to the answer options for the user to choose from
    # enumerate code from Stackoverflow user Leejay Schmidt
    for (i, option) in enumerate(options, start=1):
        i = str(i)
        valid.append(i)
        print(f"{i}: {option}")
    answer = input(
        GREEN + '\nType your choice here then press enter:\n' + RESET
    )
    # validates user input against the enumerate values
    # code uses solution from Tutorial Eyehunt by Rohit.
    while answer not in valid:
        print(
            RED + f'Invalid choice, you must enter a number from: {valid}'
            + RESET
        )
        answer = input(
            GREEN + 'Type your answer choice here then press enter:\n' + RESET
        )
    # uses the index of the answer option in the q_and_o dictionary to
    # get the string value and append it to users_answers
    index = int(answer)
    logged_answer = options[index-1]
    user_answers.append(logged_answer)
    questions_answered.append(question)

    clear_terminal()
    return user_answers, questions_answered


def welcome():
    """
    Displays a welcome message and introduces the survey
    """
    print(YELLOW + """\
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
    """ + RESET)
    print(
        """
Welcome to the Breakfast Survey! \n
This survey analyses breakfast habits based on gender and age. The
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
