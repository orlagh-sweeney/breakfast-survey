import gspread
from google.oauth2.service_account import Credentials
import plotext as plt
from prettytable import PrettyTable

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('breakfast_survey')


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


def main():
    """
    Run all program functions
    """
    welcome()


main()
