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
