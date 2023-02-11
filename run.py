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

data = SHEET.worksheet('bkdata').get_all_values()

headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)
df.head()
# print(df)

red = Fore.RED  # colour for error messages
yellow = Fore.YELLOW  # colour for instructions
green = Fore.GREEN  # colour for inputs
cyan = Fore.CYAN  # colour for tables
bright = Style.BRIGHT
reset = Style.RESET_ALL  # resets the colours


def clear_terminal():
    """
    This function clears the terminal
    Code taken from Stackoverflow solution by user 'Poke'
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def route_selection(df):
    """
    This function allows the user to select if they want
    to view results or take the survey
    """
    while True:
        print(yellow + "To view the survey results type '1' below." + reset)
        print(yellow + "To take the survey type '2' below.\n" + reset)

        route_choice = input(green + "Type your choice here then press enter:\n" + reset)

        # selection statement to validate user input choice
        if route_choice == '1':
            clear_terminal()
            results_selection(df)
            break
        if route_choice == '2':
            clear_terminal()
            display_survey()
            break

        print(red + 'Invalid choice. Please try again.\n' + reset)


def results_selection(df):
    """
    This function allows the user to select in which form they
    would like to view the results
    """
    while True:
        print(yellow + "\nPlease select from the following options:\n" + reset)
        print("1 - View results by Gender")
        print("2 - View results by Age Group\n")

        analysis_type = input(green + "Type your choice here then press enter:\n" + reset)

        # selection statement to validate user input choice
        if analysis_type == '1':
            clear_terminal()
            question_selection(df, groupby_col='gender')
            break
        if analysis_type == '2':
            clear_terminal()
            question_selection(df, groupby_col='age group')
            break

        print(red + 'Invalid choice. Please try again.\n' + reset)


def question_selection(df_raw, groupby_col):
    """
    This function allows the user to selected which question
    they would like to set the results for
    """
    while True:
        print(yellow + "\nSelect a question from the following options:\n" + reset)
        print("1 - Do you eat breafast?")
        print("1.1 - Why do you not eat breakfast?")
        print("2 - How many days per week do you eat breakfast?")
        print("3 - Where do you eat breakfast?")
        print("4 - At what time do you eat breakfast?")
        print("5 - What do you drink with breakfast?")
        print("6 - What do you eat for breakfast?\n")

        print("To return to the beginning, type 'exit'\n")

        choice = input(green + "Type your choice here then press enter:\n" + reset)

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
            print(cyan + bright + "How many days per week do you eat breakfast?" + reset)
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

        elif choice == 'exit' or 'EXIT':
            clear_terminal()
            route_selection(df)

        else:
            print(red + "Invalid choice. Please try again.\n" + reset)

    return choice


def display_percentages(df_raw, groupby_col, question_num):
    """
    This function calculates the total numbers of males
    """
    if question_num not in ['1', '1.1']:
        df_raw = df_raw[df_raw['question 1'] == 'Yes']
    elif question_num == '1.1':
        df_raw = df_raw[df_raw['question 1'] == 'No']
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

    wide_table = pd.pivot(
        df_group,
        index=groupby_col,
        columns=question_col,
        values='percentage'
    )

    if "" in wide_table.columns:
        wide_table.drop(columns="", inplace=True)
    wide_table.fillna('0%', inplace=True)
    print(cyan + bright + tabulate(wide_table, headers='keys', tablefmt='psql') + reset)


def update_worksheet(user_answers):
    """
    Add user ID to the start of the user answers list.
    Update the google sheet with user answers by
    adding a new row the the sheet.
    """
    index = df.index.tolist().pop()
    user_id = index + 2
    user_answers.insert(0, user_id)

    worksheet = SHEET.worksheet("bkdata")
    worksheet.append_row(user_answers)


def end_survey(questions_answered, user_answers):
    """
    Displays the users answers and allows the user to submit
    their results or take the survey again
    """
    print('Thank you taking our survey. Please review your answers then submit or retake the survey:')

    for question_answered, user_answer in zip(questions_answered, user_answers):
        print(f"{question_answered}: {user_answer}")
        if user_answer == '':
            continue

    print(yellow + '\nTo submit your answers, type 1 below.')
    print('To re-take the survey, type 2 below.\n' + reset)
    choice = input(green + "Type your choice here then press enter:\n" + reset)

    if choice == '1':
        update_worksheet(user_answers)
    elif choice == '2':
        clear_terminal()
        display_survey()

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
            'options': ['Cereal', 'Porridge', 'Yoghurt with granola/fruit',
                        'Toast', 'Eggs', 'Protein shake/meal replacement',
                        'Other']
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
            if user_answers[-1] == 'Yes':
                user_answers.append('')
                continue
            else:
                user_answers = question_and_log_results(
                    question, options, user_answers, questions_answered
                    )
                break

        if question_num >= 5:
            user_answers = question_and_log_results(
                question, options, user_answers, questions_answered
                )

    end_survey(questions_answered, user_answers)


def question_and_log_results(question, options, user_answers, questions_answered):
    """
    This function displays the questions and options to the user
    and logs the answers from the user
    """
    valid = []
    print(yellow + f'\n{question}\n' + reset)
    for (i, option) in enumerate(options, start=1):
        valid.append(i)
        print(f"{i}: {option}")
    answer = input(green + '\nType your answer choice here:\n' + reset)
    while int(answer) not in valid:
        print(red + f'Invalid choice, you must enter a number from: {valid}' + reset)
        answer = input(green + 'Type your answer choice here:\n' + reset)
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
    print(Fore.YELLOW +
        """\
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
    """
    + Style.RESET_ALL)

    print(
        """
Welcome to the Breakfast Survey.\n
This survey analyses breakfast eating habits based on gender and age.\n
You can view the results or add to the data by completing the survey.
        """
    )


def main(df):
    """
    Run all program functions
    """
    welcome()
    route_selection(df)


main(df=df)
