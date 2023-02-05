import gspread
from google.oauth2.service_account import Credentials
import plotext as plt
from prettytable import PrettyTable
import pandas as pd

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


def calculate_q1_gender_results(male_total, female_total):
    """
    This function calculates the gender results for question 1
    """
    male_yes = df[(df['question 1'] == 'Yes') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_yes = df[(df['question 1'] == 'Yes') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_percent = round((female_yes / female_total) * 100)
    print(f"{female_percent}% of females eat breakfast\n")
    male_percent = round((male_yes / male_total) * 100)
    print(f"{male_percent}% of males eat breakfast\n")


def calculate_q2_gender_results(male_total, female_total):
    """
    This function calculates the genders results for question 2
    """
    print("Percentage of males and femles who eat breakfast on a given \
number of days per week\n")

    female_1 = df[(df['question 2'] == '1') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_1 = df[(df['question 2'] == '1') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_2 = df[(df['question 2'] == '2') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_2 = df[(df['question 2'] == '2') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_3 = df[(df['question 2'] == '3') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_3 = df[(df['question 2'] == '3') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_4 = df[(df['question 2'] == '4') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_4 = df[(df['question 2'] == '4') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_5 = df[(df['question 2'] == '5') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_5 = df[(df['question 2'] == '5') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_6 = df[(df['question 2'] == '6') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_6 = df[(df['question 2'] == '6') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_7 = df[(df['question 2'] == '7') & (df['gender'] == 'Male')]\
        .value_counts().sum()
    male_7 = df[(df['question 2'] == '7') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    f1_p = (female_1 / female_total) * 100
    f2_p = (female_2 / female_total) * 100
    f3_p = (female_3 / female_total) * 100
    f4_p = (female_4 / female_total) * 100
    f5_p = (female_5 / female_total) * 100
    f6_p = (female_6 / female_total) * 100
    f7_p = (female_7 / female_total) * 100

    m1_p = (male_1 / male_total) * 100
    m2_p = (male_2 / male_total) * 100
    m3_p = (male_3 / male_total) * 100
    m4_p = (male_4 / male_total) * 100
    m5_p = (male_5 / male_total) * 100
    m6_p = (male_6 / male_total) * 100
    m7_p = (male_7 / male_total) * 100

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
    male_way = df[(df['question 3'] == 'Way') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_work = df[(df['question 3'] == 'Work') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    female_home = df[(df['question 3'] == 'Home') & (df['gender'] == 'Female')]\
        .value_counts().sum()
    female_way = df[(df['question 3'] == 'Way') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    mw_p = (male_work / male_total) * 100
    mh_p = (male_home / male_total) * 100
    mo_p = (male_way / male_total) * 100

    fw_p = (female_work / female_total) * 100
    fh_p = (female_home / female_total) * 100
    fo_p = (female_way / female_total) * 100

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


# def welcome():
#     """
#     Displays a welcome message and introduction to the survey
#     """
#     print(
#         """\
#                              #        #                   #
#  ####                        #       ###                  #
#  #   #                       #  #    #                   ###
#  ####   # #     ##     ###   # #    ###     ###   ####    #
#  #   #  ## #   # ##   #  #   ###     #     #  #   ##      # #
#  #   #  #      ##     #  #   #  #    #     #  #     ##    # #
#  ####   #       ###    ####  #  #    #      ####  ####     #


#          ##
#         #  #
#          #     #  #   # #    #  #    ##    #  #
#           #    #  #   ## #   #  #   # ##   #  #
#         #  #   #  #   #       ##    ##     ## #
#          ##     ###   #       ##     ###     ##
#                                            #  #
#                                             ##
#     """
#     )

#     print(
#         """
#         Welcome to the Breakfast Survey.\n
#         This survey analyses breakfast eating habits based on gender and age.\n
#         You can view the results, read a summary or add to the data by
#         completing the survey.
#         """
#     )


def main():
    """
    Run all program functions
    """
    # welcome()
    route_selection()
    male_total = get_total_males()
    female_total = get_total_females()
    calculate_q1_gender_results(male_total, female_total)
    calculate_q2_gender_results(male_total, female_total)
    calculate_q3_gender_results(male_total, female_total)


main()
