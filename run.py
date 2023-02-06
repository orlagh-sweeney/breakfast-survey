import gspread
from google.oauth2.service_account import Credentials
import plotext as plt
from prettytable import PrettyTable
import pandas as pd
import numpy as np
import calculate

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


def route_selection():
    """
    This function allows the user to select if they want
    to view results or take the survey
    """
    while True:
        print("To view the survey results type '1' below.")
        print("To take the survey type '2' below.")

        route_choice = input("Type your choice here then press enter:\n")

        if route_choice == '1':
            results_selection()
            break
        if route_choice == '2':
            print('Take survey')
            break

        print('Invalid choice. Please try again.\n')


def results_selection():
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

        if analysis_type == '1':
            print('View gender results')
            break
        if analysis_type == '2':
            print('View age group survey')
            break
        if analysis_type == '3':
            print('View summary')
            break

        print('Invalid choice. Please try again.\n')


def question_selection():
    """
    This function allows the user to selected which question
    they would like to set the results for
    """
    while True:
        print("Please select a question from the following options.")
        print("1 - Do you eat breafast?")
        print("2 - How many days per week do you eat breakfast?")
        print("3 - Where do you eat breakfast?")
        print("4 - At what time do you eat breakfast?")
        print("5 - What do you drink with breakfast?")
        print("6 - What do you eat for breakfast?\n")

        choice = input("Type your choice here then press enter:\n")

        if choice == '1':
            print('Q1')

        elif choice == '2':
            print('Q2')

        elif choice == '3':
            print('Q3')

        elif choice == '2':
            print('Q4')

        elif choice == '6':
            print('Q5')

        elif choice == '6':
            print('Q6')

        else:
            print("Invalid choice. Please try again.\n")

    return choice


def get_total_males():
    """
    This function calculates the total numbers of males
    """
    male_total = df['gender'].str.contains('Male').sum()
    return male_total


def get_total_females():
    """
    This function calculates the total number of females
    """
    female_total = df['gender'].str.contains('Female').sum()
    return female_total


def get_yes_females():
    """
    This function get the total number of females
    who eat breakfast
    """
    female_yes = df[(df['question 1'] == 'Yes') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    return female_yes


def get_yes_males():
    """
    This function get the total number of females
    who eat breakfast
    """
    male_yes = df[(df['question 1'] == 'Yes') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    return male_yes


def calculate_q1_gender_results(male_total, female_total, female_yes, male_yes):
    """
    This function calculates the gender results for question 1
    """
    female_percent = calculate.percentage(female_yes, female_total)
    print(f"{female_percent}% of females eat breakfast\n")

    male_percent = calculate.percentage(male_yes, male_total)
    print(f"{male_percent}% of males eat breakfast\n")


def calculate_q2_gender_results(male_total, female_total):
    """
    This function calculates the genders results for question 2
    """
    print("Percentage of males and femles who eat breakfast on a given \
number of days per week\n")

    female_1 = df[(df['question 2'] == '1') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    male_1 = df[(df['question 2'] == '1') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_2 = df[(df['question 2'] == '2') & (df['gender'] == 'Feale')]\
        .value_counts().sum()
    male_2 = df[(df['question 2'] == '2') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_3 = df[(df['question 2'] == '3') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    male_3 = df[(df['question 2'] == '3') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_4 = df[(df['question 2'] == '4') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    male_4 = df[(df['question 2'] == '4') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_5 = df[(df['question 2'] == '5') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    male_5 = df[(df['question 2'] == '5') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_6 = df[(df['question 2'] == '6') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    male_6 = df[(df['question 2'] == '6') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_7 = df[(df['question 2'] == '7') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    male_7 = df[(df['question 2'] == '7') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    f1_p = calculate.percentage(female_1, female_total)
    f2_p = calculate.percentage(female_2, female_total)
    f3_p = calculate.percentage(female_3, female_total)
    f4_p = calculate.percentage(female_4, female_total)
    f5_p = calculate.percentage(female_5, female_total) 
    f6_p = calculate.percentage(female_6, female_total)
    f7_p = calculate.percentage(female_7, female_total)

    m1_p = calculate.percentage(male_1, male_total)
    m2_p = calculate.percentage(male_2, male_total)
    m3_p = calculate.percentage(male_3, male_total)
    m4_p = calculate.percentage(male_4, male_total)
    m5_p = calculate.percentage(male_5, male_total)
    m6_p = calculate.percentage(male_6, male_total)
    m7_p = calculate.percentage(male_7, male_total)

    table = PrettyTable()
    table.field_names = ["No. of Days Per Week", "1", "2", "3", "4", "5", "6", "7"]
    table.add_row([
        "Female",
        f"{f1_p}%",
        f"{f2_p}%",
        f"{f3_p}%",
        f"{f4_p}%",
        f"{f5_p}%",
        f"{f6_p}%",
        f"{f7_p}%",
        ])
    table.add_row([
        "Male",
        f"{m1_p}%",
        f"{m2_p}%",
        f"{m3_p}%",
        f"{m4_p}%",
        f"{m5_p}%",
        f"{m6_p}%",
        f"{m7_p}%",
        ])

    print(table)


def calculate_q3_gender_results(male_total, female_total):
    """
    This function calculates the gender results for question 1
    """
    male_work = df[(df['question 3'] == 'Work') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_home = df[(df['question 3'] == 'Home') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_way = df[(df['question 3'] == 'On the way to work') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_work = df[(df['question 3'] == 'Work') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    female_home = df[(df['question 3'] == 'Home') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    female_way = df[(df['question 3'] == 'On the way to work') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    mw_p = calculate.percentage(male_work, male_total)
    mh_p = calculate.percentage(male_home, male_total)
    mo_p = calculate.percentage(male_way, male_total)

    fw_p = calculate.percentage(female_work, female_total)
    fh_p = calculate.percentage(female_home, female_total)
    fo_p = calculate.percentage(female_way, female_total)

    table = PrettyTable()
    table.field_names = [
        "Breakfast Location",
        "At Home",
        "At Work",
        "On the way to work",
        ]
    table.add_row([
        "Female",
        f"{fw_p}%",
        f"{fh_p}%",
        f"{fo_p}%",
    ])
    table.add_row([
        "Male",
        f"{mw_p}%",
        f"{mh_p}%",
        f"{mo_p}%",
    ])

    print(table)


# # def welcome():
# #     """
# #     Displays a welcome message and introduction to the survey
# #     """
# #     print(
# #         """\
# #                              #        #                   #
# #  ####                        #       ###                  #
# #  #   #                       #  #    #                   ###
# #  ####   # #     ##     ###   # #    ###     ###   ####    #
# #  #   #  ## #   # ##   #  #   ###     #     #  #   ##      # #
# #  #   #  #      ##     #  #   #  #    #     #  #     ##    # #
# #  ####   #       ###    ####  #  #    #      ####  ####     #


# #          ##
# #         #  #
# #          #     #  #   # #    #  #    ##    #  #
# #           #    #  #   ## #   #  #   # ##   #  #
# #         #  #   #  #   #       ##    ##     ## #
# #          ##     ###   #       ##     ###     ##
# #                                            #  #
# #                                             ##
# #     """
# #     )

# #     print(
# #         """
# #         Welcome to the Breakfast Survey.\n
# #         This survey analyses breakfast eating habits based on gender and age.\n
# #         You can view the results, read a summary or add to the data by
# #         completing the survey.
# #         """
# #     )


def main():
    """
    Run all program functions
    """
    # welcome()
    route_selection()
    male_total = get_total_males()
    male_yes = get_yes_males()
    female_total = get_total_females()
    female_yes = get_yes_females()
    calculate_q1_gender_results(male_total, female_total, female_yes, male_yes)
    calculate_q2_gender_results(male_total, female_total)
    calculate_q3_gender_results(male_total, female_total)


main()
