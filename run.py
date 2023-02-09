import os
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
import pandas as pd
import numpy as np
from tabulate import tabulate

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


def clear_terminal():
    """
    This function clears the terminal
    Code taken from Stackoverflow solution: https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def route_selection(df):
    """
    This function allows the user to select if they want
    to view results or take the survey
    """
    while True:
        print("To view the survey results type '1' below.")
        print("To take the survey type '2' below.")

        route_choice = input("Type your choice here then press enter:\n")

        # selection statement to validate user input choice
        if route_choice == '1':
            results_selection(df)
            break
        if route_choice == '2':
            print('Take survey')
            break

        print('Invalid choice. Please try again.\n')


def results_selection(df):
    """
    This function allows the user to select in which form they
    would like to view the results
    """
    while True:
        print("Please select from the following options.")
        print("1 - View results by gender")
        print("2 - View results by age group")
        print("3 - View survey summary")

        analysis_type = input("Type your choice here then press enter:\n")

        # selection statement to validate user input choice
        if analysis_type == '1':
            question_selection(df, groupby_col='gender')
            break
        if analysis_type == '2':
            question_selection(df, groupby_col='age group')
            break
        if analysis_type == '3':
            print('View summary')
            break

        print('Invalid choice. Please try again.\n')


def question_selection(df_raw, groupby_col):
    """
    This function allows the user to selected which question
    they would like to set the results for
    """
    while True:
        print("Select a question from the following options:\n")
        print("1 - Do you eat breafast?")
        print("1.1 - Why do you not eat breakfast?")
        print("2 - How many days per week do you eat breakfast?")
        print("3 - Where do you eat breakfast?")
        print("4 - At what time do you eat breakfast?")
        print("5 - What do you drink with breakfast?")
        print("6 - What do you eat for breakfast?\n")

        print("To return to the beginning, type 'exit'\n")

        choice = input("Type your choice here then press enter:\n")

        # selection statement to validate user input choice
        if choice == '1':
            display_percentages(df_raw, groupby_col, '1')

        elif choice == '1.1':
            display_percentages(df_raw, groupby_col, '1.1')

        elif choice == '2':
            display_percentages(df_raw, groupby_col, '2')

        elif choice == '3':
            display_percentages(df_raw, groupby_col, '3')

        elif choice == '4':
            display_percentages(df_raw, groupby_col, '4')

        elif choice == '5':
            display_percentages(df_raw, groupby_col, '5')

        elif choice == '6':
            display_percentages(df_raw, groupby_col, '6')

        elif choice == 'exit':
            clear_terminal()
            route_selection(df)

        else:
            print("Invalid choice. Please try again.\n")

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
    print(tabulate(wide_table, headers='keys', tablefmt='psql'))


def display_survey():
    """
    Displays the survey 
    """
    questions = [
        'Please select your age aroup',
        'Please select your gender'
        'Do you eat breakfast',
        'If not, why do you not eat breakfast?',
        'How many days per week do you eat breakfast?',
        'Where do you eat breakfast?',
        'At what time do you eat breakfast?',
        'What do you drink with breakfast?',
        'What do you eat for breakfast?'
    ]

    options = [
        ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
        ['Male', 'Female',],
        ['Yes', 'No',],
        ['Not hungry', 'No time', 'Other'],
        ['1', '2', '3', '4', '5', '6', '7'],
        ['Home', 'Work', 'On the way to work'],
        ['6am-7am', '7am-8am', '8am-9am', '9am-10am', '10am-11am'],
        ['Coffee', 'Tea', 'Juice'],
        ['Cereal', 'Porridge', 'Yoghurt with granola/fruit', 'Toast', 'Eggs', 'Protein shake/meal replacement', 'Other']
    ]


def welcome():
    """
    Displays a welcome message and introduction to the survey
    """
    print(
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
    )

    print(
        """
Welcome to the Breakfast Survey.\n
This survey analyses breakfast eating habits based on gender and age.\n
You can view the results, read a summary or add to the data by
completing the survey.
        """
    )


def main(df):
    """
    Run all program functions
    """
    welcome()
    route_selection(df)


main(df=df)
