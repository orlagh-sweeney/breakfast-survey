# Breakfast Survey and Analysis
<image src="assets/readme-files/main-image.png" width="600px"></image><br>
This Breakfast Survey and Analysis project has been built to give users insights into breakfast habits of people based on Gender and Age Group. There are two core aspects to this program:
1. The option to view the results of the survey.
2. The option to take the survey to contribute to the data. 

This project was built as my 3rd portfolio project following completion of the Code Institute Python module. It uses mock data to demonstrate the program's functionality. 

The project can be viewed here: https://breakfast-survey.herokuapp.com/

## Table of Contents
1. [User Experience](#user-experience-ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Colour Scheme](#colour-scheme)
    - [Data Model](#data-model)
    - [Flowchart](#flowchart)
2. [Features](#features)
    - [Welcome & Take Survey or View Analysis](#welcome--take-survey-or-view-analysis)
    - [View Results by Gender or Age Group](#view-results-by-gender-or-age-group)
    - [Display Results by Question](#display-results-by-question)
    - [Take Survey](#take-survey)
    - [Review Answers: Submit or Retake](#review-answers-submit-or-retake)
    - [Update Worksheet and End Program](#update-worksheet-and-end-program)
    - [Goodbye](#goodbye)
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
The program uses Google Sheets to store data in columns. After the data is fetched, it is processed using a Pandas dataframe. The worksheet has a column that applies a unique user ID for each user and a column for each survey question.

The program uses a series of functions to display the survey results; results_selections asks the user if they want to view results by Gender or Age Group, then question_selection asks the user to choose which question they want to view results for. This information is then passed into display_percentages which uses Pandas to analyse the data and calculate percentages which are presented in table format to the user. 

When taking the survey, the users answers are stored in a variable called user_answers which updates each time a question is answered. After the last question is answered the user is asked to review and submit their results or take the quiz again. If the user clicks the submit the data is pushed to the Google Sheets worksheet. 

If a user answers 'no' to 'Do you eat breakfast?', the survey ends after they explain why. Furthermore, their data is not used when analysing the remaining questions, meaning that questions 5-9 are only analysed based on people who eat breafast. 

A screenshot of the Google Sheets worksheet can be found below:

<image src="assets/readme-files/google-sheets.png" width="600px"></image><br>

### Flowchart
[Lucid](https://lucid.app/documents#/dashboard) was used in the planning stage of the project to plan the logic and data flow. 
The flowchart does not include every validation as it would make the chart too cluttered, however every time user input is required validation has been used.
<image src="assets/readme-files/flowchart.png"></image>

## Features

### Welcome & Take Survey or View Analysis
<image src="assets/readme-files/welcome-message-route.png" width="600px"></image>
- This sections displays a welcome message to the user. 
- It explains to the user what the survey is about and gives instructions on how to use the program.
- It gives the user the option to view the survey results or to take the survey.

### View Results by Gender or Age Group
<image src="assets/readme-files/view-results-by.png" width="600px"></image>
- This section asks the user if they want to view the survey results by gender or age group.

### Display Results by Question
<image src="assets/readme-files/select-question-to-view.png" width="600px"></image>
<image src="assets/readme-files/display-results.png" width="600px"></image>
- This section prompts the user to select a question in order to see the results. 
- It displays the results in table format along with the relevant question.
- The user can switch between questions by typing the question number to load a new table.
- There is also the option to exit this section and return to the beginning of the program.

### Take Survey 
<image src="assets/readme-files/display-survey-questions.png" width="600px"></image>
- This section displays the survey questions and answer options to the user. 
- To submit an answer, the user must type the number assigned to the answer option.

### Review Answers: Submit or Retake
<image src="assets/readme-files/display-users-answers.png" width="600px"></image>
- This section displays the answer that the user gave for each question.
- The user is asked to review and submit their answers.
- The user also has the option to re-take the survey, in this case the survey reloads. 

### Update Worksheet and End Program
<image src="assets/readme-files/answers-submitted.png" width="600px"></image>
- This section informs the user that their survey answers were successfully submitted.
- In the background, the Google Sheets worksheet has been updated. 
- The user is then asked if they want to view the survey results or end the program.

### Goodbye
<image src="assets/readme-files/goodbye-message.png" width="600px"></image>
- This section displays a googbye message to the user.
- It also gives the option for the user to restart the program if they change their mind. 

## Technologies Used
### Languages
- Python

### Frameworks, Libraries and Programmes
- [Lucid](https://lucid.app/documents#/dashboard): this was used to create a flowchart in the planning stage of the project.
- [Colorama](https://pypi.org/project/colorama/): this was used to add colour to the terminal to improve UX and readibility.
- [Tabulate](https://pypi.org/project/tabulate/): this was used to display data in tables. 
- [Pandas](https://pypi.org/project/pandas/): this was used store and analyse survey data.
- [Numpy](https://pypi.org/project/numpy/): this was used to analyse survey data.
- [Gspread](https://docs.gspread.org/en/v5.7.0/): this is the API for Google Sheets which stores the survey data. 
- [Gitpod](https://www.gitpod.io/): this was used to write, commit and push the code to GitHub. 
- [GitHub](https://github.com/): this was used to store the project and for version control.
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.

## Testing
### Testing User Stories
- As a user, I want to understand what the program is for and how to use it.
    - The program tells me that it is a survey about breakfast and gives instructions on how to proceed.
- As a user, I want to be able to choose whether to take the survey or view results.
    - The program gives me the option to view the survey results or take the survey.
- As a user, I want to be able to choose what questions I view the data for.
    - The sruvey allows me to choose which question to view results for and easily switch between questions.
- As a user, I want to be able to take the survey.
    - The program gives me the option to take the survey at the beginning and displays each question.
- As a user, I want to be able to review my answers before submitting or take the survey again.
    - After answering the questions the program shows my answers and asks me if I want to submit them or take the survey again. 
- As a user, I want to be able to exit or restart the program. 
    - The program gives me the options to exit the program while viewing results or after taking the survey.

### Code Validation
The codes passes through the Code Institute PEP8 Linter with no errors.<br>
<image src="assets/readme-files/ci-pylint.png" width="600px"></image>

Examples of errors encountered during development are demonstrated below. All errors were resovled.
- Example 1: Lines too long <br> <image src="assets/readme-files/error-line-too-long.png" width="600px"></image>
- Example 2: Naming style errors <br><image src="assets/readme-files/error-naming-style.png" width="600px"></image>

### Feature Testing
I have manually tested the following features in Gitpod and in the Code Institute Heroku terminal:
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Welcome Message | When the program first runs, the welcome message and route selection options are displayed. | PASS
Route Selection | When '1' is typed in the terminal, results_selection is called and the user is asked how they want to view the results. When '2' is typed in the terminal, display_survey is called and the user is brought to the survey. | PASS 
Route Selection Validation | If the user types anything other than '1' or '2', they are shown an error message and asked to try again. | PASS
Results Selection | When '1' is typed in the terminal, the program loads data on Gender. When '2' is typed in the terminal, the program loads data on Age Group. | PASS
Results Selection Validation | If the user types anything other than '1' or '2', they are shown an error message and asked to try again. | PASS
Results Question Selection | If the user types anything from (1, 1.1, 2, 3, 4, 5 or 6), they are shown the data for the corresponding question. If they type 'exit' or 'EXIT', the program ends and they return to the Route Selection area. | PASS
Results Question Selection Validation | If the user types anything other than (1, 1.1, 2, 3, 4, 5, 6, exit or EXIT), they are shown an error message and asked to try again. | PASS
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
End Program | If the users chooses to end the program, the end_program function is called which displays a goodbye message and an option to restart the program by typing '1'. | PASS
End Program Validation | If the user types anything other than '1', they are shown an error message and asked to try again. | PASS
Restart Program | If the user chooses to restart the program, the main function is called and the user is brought back to the beginning of the program | PASS

### Bugs
1. Answering survey questions: 
- When the user submitted their answer to a survey question, there was an error when comparing and validating user input with the valid answers. To validate the users survey answers, the program compares the users input (1, 2, 3 etc.) with the enumerate values assigned to the answer option which are stored in a list called 'Valid' each time a new question loads. The enumerate value is an integer and the user input from the terminal is a string, this caused an error when validating. To fix this I converted the enumerate values to a string before appending these values to the 'Valid' list. 
2. Displaying the users survey answers:
- There was a bug when displaying the users survey answers in the terminal. This was due to omitting an empty string in the questions_anwswered list for question 4, and because the print statement was in the wrong line. These errors were fixed and the users answers are displayed as expected.
3. Exit 'View Results':
- When the user was finished viewing survey results and wanted to exit this function, the 'exit' or 'EXIT' inputs were not working so there was no way to exit the program. I changed the code from "else choice = “exit” or ‘EXIT’" to "else choice in (‘exit’ ‘EXIT)" which solved the issue. The user is now able to exit this section of the program. 

## Deployment
The program was developed in Gitpod. It was then commited and pushed to GitHub.
The finished project was deployed in Heroku using the Code Institute Python Terminal for display purposes. 
Deployment to Heroku was completed using the following steps: 
1. Run 'pip3 freeze > requirements.txt' in the terminal to add a list of dependencies to requirements.txt
2. Commit these changes and push to GitHub.
3. Open and login to [Heroku](https://id.heroku.com/login).
4. From the dashboard, click 'New', then click 'Create new app' from the dropdown menu. 
5. Enter the App name, choose a region, then click 'Create app'.
6. Navigate to the 'Settings' tab.
7. Within 'Settings', navigate to 'Convig Vars'. Click 'Reveal Config Vars'.
8. Two config vars need to be added using the following 'KEY' and 'VALUE' pairs:
    1. KEY = 'CREDS', VALUE = Copy and paste the entire contents of the creds.json file into this field. Then click 'Add'.
    2. KEY = 'PORT', VALUE = '8000'. Then click 'Add'.
9. Within 'Settings', navigate to 'Buildpack'. 
10. Click 'Add buildpack'. Select 'Python', then click 'Save changes'.
11. Click 'Add buildpack' again. Select 'nodejs', then click 'Save changes'.
    - Ensure that these buildpacks are in the correct order: Python on top and nodejs underneath. 
    - If they are in the wrong order, click and drag to fix this. 
12. Navigate to the 'Deploy' tab. 
13. Within 'Deploy', navigate to 'Deployment method'. 
14. Click on 'GitHub'. Navigate to 'Connect to GitHub' and click 'Connect to GitHub' 
15. Within 'Connect to GitHub', use the search function to find the repository to be deployed. Click 'Connect'.
16. Navigate to either 'Automatic Deploys' or 'Manual Deploys' to choose which method to deploy the application.
17. Click on 'Enable Automatic Deploys' or 'Deploy Branch' respectively, depending on chosen method. 
18. Once the app is finished building, a message saying 'Your app was successfully deployed' will appear.
19. Click 'View' to see the deployed app. 

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

To see how to correctly set up Pandas with Google Sheets I used solution by GitHub user [Asha Ponnada](https://github.com/Asha-ai/googlespredsheets/blob/master/googlesheet_as_pandasdf.ipynb).

## Acknowledgements
- Thank you to my mentor Marcel for his feedback and suggestions at each stage of the project.
- Thank you to Code Institute for providing me with the tools and skills to complete this project. 