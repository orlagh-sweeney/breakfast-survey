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
print(df)

def calculate_gender_results():
    """
    This function calculates the genders results
    """
    male_tot = df['gender'].str.contains('Male').sum()
    female_tot = df['gender'].str.contains('Female').sum()
    # print(female_tot)
    male = df[df['gender'] == 'Male']
    female = df[df['gender'] == 'Female']

    # calculate question 1
    male_yes = df[(df['question 1'] == 'Yes') & (df['gender'] == 'Male')]\
        .value_counts().sum()

    female_yes = df[(df['question 1'] == 'Yes') & (df['gender'] == 'Female')]\
        .value_counts().sum()

    female_percent = (female_yes / female_tot) * 100
    male_percent = (male_yes / male_tot) * 100

    # calculate question 2
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
    
    female_1_percent = (female_1 / female_tot) * 100
    female_2_percent = (female_2 / female_tot) * 100
    female_3_percent = (female_3 / female_tot) * 100
    female_4_percent = (female_4 / female_tot) * 100
    female_5_percent = (female_5 / female_tot) * 100
    female_6_percent = (female_6 / female_tot) * 100
    female_7_percent = (female_7 / female_tot) * 100

    male_1_percent = (male_1 / male_tot) * 100
    male_2_percent = (male_2 / male_tot) * 100
    male_3_percent = (male_3 / male_tot) * 100
    male_4_percent = (male_4 / male_tot) * 100
    male_5_percent = (male_5 / male_tot) * 100
    male_6_percent = (male_6 / male_tot) * 100
    male_7_percent = (male_7 / male_tot) * 100



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
    calculate_gender_results()


main()
