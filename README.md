# Breakfast Survey and Analysis

## Table of Contents
1. [User Experience](#user-experience-ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Colour Scheme](#colour-scheme)
    - [Data Model](#data-model)
    - [Flowchart](#flowchart)
2. [Features](#features)
    - [Take Survey or View Analysis](#take-survey-or-view-analysis)
    - [View Analysis by Gender or Age Group](#view-analysis-by-gender-or-age-group)
    - [Question Selection](#question-selection)
    - [Return to the Beginning](#return-to-beginning)
    - [Take Survey](#take-survey)
    - [Input Answers](#input-answers)
3. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
4. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Feature Testing](#feature-testing)
    - [Bugs](#bugs)
6. [Deployment](#deployment)
6. [Credit](#credit)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
7. [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Project Goals
- Analyse survey results.
- Collect survey responses.
- Display results in a format that is easy for the user to read.
- Use input validation for user input.
- Store survey data in Google Sheets.

### User Stories
- As a user, I want to understand what the program is for and how to use it.
- As a user, I want to be able to choose whether to take the survey or view results.
- As a user, I want to be able to choose what questions I view the data for.
- As a user, I want to be able to take the survey.
- As a user, I want to be able to review my answers before submitting or take the survey again.
- As a user, I want to be able to exit or restart the program. 

### Colour Scheme
Colorama has been used to apply colour to the terminal to make it more readable. 
- Instructions are displayed in yellow.
- Inputs are displayed in green.
- Error messages are displayed in red.
- Tables are displayed in cyan.

### Data Model
The program uses Google Sheets to store data in columns. The worksheet has a column that applies a unique user ID for each user and a column for each survey question. 

The program uses a series of functions to display the survey results; results_selections asks the user if they want to view results by Gender or Age Group, then question_selection asks the user to choose which question they want view results for. This information is then passed into display_percentages which uses Pandas to analyse the data and calculate percentages which are presented in table format to the user. 

When taking the survey, the users answers are stored in a variable called user_answers which updates each time a question is answered. After the last question is answered the user is asked to review and submit their results or take the quiz again. If the user clicks the submit the data is pushed to the Google Sheets worksheet. 

If a user answers no to 'Do you eat breakfast?', the survey ends after they explain why. Furthermore, their data is not used when analysing the remaining questions, meaning that questions 5-9 are only analysed based on people who eat breafast. 

### Flowchart
[Lucid](https://lucid.app/documents#/dashboard) was used in the planning stage of the project to plan the logic and data flow. 

## Features

### Take Survey or View Analysis
### View Analysis by Gender or Age Group
### Question Selection
### Return to Beginning
### Take Survey 
### Input Answers


## Technologies Used
### Languages
- Python

### Frameworks, Libraries and Programmes
- [Lucid](https://lucid.app/documents#/dashboard): this was used to create a flowchart in the planning stage of the project.
- [Colorama](https://pypi.org/project/colorama/): this was used to add colour to the terminal to improve UX and readibility.
- [Tabulate](https://pypi.org/project/tabulate/): this was used to display data in tables. 
- [Pandas](https://pypi.org/project/pandas/): this was used to analyse survey data.
- [Numpy](https://pypi.org/project/numpy/): this was used to analyse survey data.
- [Gspread](https://docs.gspread.org/en/v5.7.0/): this is the API for the Google Sheets which stores the survey data. 
- [Gitpod](https://www.gitpod.io/): this was used to write, commit and to push the code to GitHub. 
- [GitHub](https://github.com/): this was used to store the project and for version control.
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.

## Testing
### Testing User Stories
- As a user, I want to understand what the program is for and how to use it.
    - The program tells me that it is a survey about breakfast and gives instructions on how to proceed.
- As a user, I want to be able to choose whether to take the survey or view results.
    - The program gives me the option to view the survey results or take the survey,
- As a user, I want to be able to choose what questions I view the data for.
    - The sruvey allows me to choose which question to view results for and easily switch between questions.
- As a user, I want to be able to take the survey.
    - The program gives me the option to take the survey at the beginning and displays each question.
- As a user, I want to be able to review my answers before submitting or take the survey again.
    - After answering the questions the program shows my answers then asks me if I want to submit or take the survey again. 
- As a user, I want to be able to exit or restart the program. 
    - The program gives me the options to exit the program while viewing results or after taking the survey.

### Code Validation
The codes passes through the Code Institute PEP8 Linter with no errors. 

### Feature Testing
I have manually tested the following features in Gitpod and in the Code Institute Heroku terminal:
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Welcome Message | When the program first runs the welcome message and route selection options are displayed. | PASS
Route Selection | When '1' is typed in the terminal, results_selection is called and the user is asked how they want to view the results. When '2' is typed in the terminal, display_survey is called and the user is brought to the survey. | PASS 
Route Selection Validation | If the user types anything other than '1' or '2' they are shown an error message and asked to try again. | PASS
Results Selection | When '1' is typed in the terminal, the program loads data on Gender. When '2' is typed in the terminal, the program loads data on Age Group. | PASS
Results Selection Validation | If the user types anything other than '1' or '2' they are shown an error message and asked to try again. | PASS
Results Question Selection | If the user types anything form (1, 1.1, 2, 3, 4, 5 or 6) they are shown the data for the correct question. If they type 'exit' or 'EXIT' the program ends and they return to Route Selection area. | PASS
Results Question Selection Validation | If the user types anything other than (1, 1.1, 2, 3, 4, 5, 6, exit or EXIT) they are shown an error message and asked to try again. | PASS
Display Survey | The survey loads each question with the correct set of answers options. | PASS
Survey Answer Selection Validation | If the users enters an invalid input they are shown an error message and asked to try again. The error message displays a list of numbers from which they can choose. | PASS
If 'Do you eat breafast?' = 'No' | The user is presented with a follow up question, 'Why do you not eat breakfast', after this the survey ends. | PASS
If 'Do you east breakfast? = 'Yes' | The survey skips the question 'Why do you not eat breakfast' and continues the survey until the end. | PASS
Survey Ends: Display Questions | Once the user has answered all the questions the survey ends and they are shown their answers. The correct selection of questions and answers are displayed. | PASS
Survey Ends: Submit or Retake | The users is asked to review and submit their answers or if they want to retake the survey.  If the users types '1' their results are submitted, if the user types '2' the survey reloads. | PASS
Survey Ends Validation | If the user types anything other than '1' or '2' they are shown an error message and asked to try again. | PASS
Submit Results | When the user submits their results the update_worksheet function is called and the data is pushed to Google Sheets. Empty data is handled appropriately by leaving the relevant column/columns empty. | PASS
End Survey | When the user submits their answers the end_survey function is called. They are asked if they want to view the survey results by typing '1' or end the program by typing '2'.  | PASS
End Survey Validation | If the user types anything other than '1' or '2' they are shown an error message and asked to try again. | PASS
End Program | If the users chooses to end the program, the end_program function is called which displays a goodbye message and an option to retart the program by typing '1'. | PASS
End Program Validation | If the user types anything other than '1' they are shown an error message and asked to try again. | PASS
Restart Program | If the user choose to restart the program, the main function is called and the user is brought back to the beginning of the program | PASS

### Bugs
1. Answering survey questions: 
- When the user submitted their answer to a survey question, there was an error when comparing and validating user input with the valid answers. To validate and store the users survey answers, the program compares the users input with the enumerate values assigned the answer option which are stored in a variable called Valid. The enumerate value is an integer and the user input from the terminal is a string which was causing an error when validating. To fix this I converted the enumerate values to a string before appending these values to the Valid list. 
2. Exit 'View Results':
- When the user was finished viewing results and wanted to exit this function, the 'exit' or 'EXIT' inputs were not working. I changed the code from "else choice = “exit” or ‘EXIT’" to "else choice in (‘exit’ ‘EXIT)" which solved the issue. The user is now able to exit this section of the program. 

## Deployment

## Credit
### Content
Content was written by the developer. 

### Media
[ASCII generator](https://ascii-generator.site/t/) - this was used to create the welcome and goodbye messages. 

### Code
[Stackoverflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) were used throughout the development to educate myself and to seek help and clarification on features. In particular I used the following sources:
- Printing a Pandas dataframe: answer by Stackoverflow user [Romain](https://stackoverflow.com/a/31885295).
- How to enumerate a list: answer by Stackoverflow user [Leejay Schmidt](https://stackoverflow.com/a/34754025).
- How to clear the terminal: answer by Stackoverflow user [poke](https://stackoverflow.com/a/2084628).

Documentation and PyPI resources for Pandas, Numpy, Tabulate and Colorama were referred to throughout the development to learn how to use these libraries:
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [Pandas - PyPI](https://pypi.org/project/pandas/)
- [Numpy](https://numpy.org/doc/stable/index.html)
- [Numpy - PyPI](https://pypi.org/project/numpy/)
- [Tabulate - PyPI](https://pypi.org/project/tabulate/) 
- [Colorama - PyPI](https://pypi.org/project/colorama/) 

To validate user input for survey answers in the question_and_log_results function I used a solution from [Tutorial Eyehunt by Rohit](https://tutorial.eyehunts.com/python/python-while-loop-input-validation-example-code/).

## Acknowledgements
- Thank you to my mentor Marcel for his feedback and suggestions at each stage of the project.
- Thank you to Code Institute for providing me with the tools and skills to complete this project. 